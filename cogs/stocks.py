import discord
from discord.ext import commands, tasks
from yahoo_fin import stock_info as si
import yfinance as yf
import asyncio
import requests
from tradingview_ta import TA_Handler, Interval
from datetime import datetime
import pytz
import time
import matplotlib.pyplot as plt
import os

from helper import create_embed, get_user_data, save_user_data, get_stock, save_stock, get_all_user_data
from constants import UPDATE_TICKERS, TICKER_PERIOD, TICKER_INTERVAL, MARKET_START, MARKET_END, TEMP_PATH, STOCK_CHART_PATH, MARKET_HOURS_EXISTS

def is_market_open():
    if not MARKET_HOURS_EXISTS:
        return True

    now = datetime.now(tz = pytz.timezone("US/Eastern"))
    day_to_minute = now.hour * 60 + now.minute # the amount of minutes since the midnight
    return MARKET_START <= day_to_minute < MARKET_END

def get_price(ticker: str, round_to: int = 2):
    try:
        price = round(si.get_live_price(ticker.lower()), round_to)
        if str(price) == "nan":
            stock = get_stock(ticker)
            return stock and round(stock["current_price"], 2) or None
        else:
            return price
    except:
        return None

def get_open(ticker: str, round_to: int = 2):
    try:
        ticker = ticker.upper()
        data = yf.download(tickers = ticker, period = TICKER_PERIOD, interval = TICKER_INTERVAL)
        price = round(dict(data)["Open"][0], round_to)
        return price 
    except:
        return None

def get_recommendation(symbol: str):
    symbol = symbol.upper()
    try:
        info = TA_Handler(symbol=symbol, screener="america", exchange="NASDAQ", interval=Interval.INTERVAL_1_DAY).get_analysis().summary
        return info
    except:
        try:
            info = TA_Handler(symbol=symbol, screener="crypto",exchange="binance",interval=Interval.INTERVAL_1_DAY).get_analysis().summary
            return info
        except:
            return None

class stocks(commands.Cog, description = "Stock market commands."):
    def __init__(self, client):
        self.client = client
        self.tickers = {
            "BTC": {
                "ticker": "BTC-USD",
                "round_to": 0,
            },
            "ETH": {
                "ticker": "ETH-USD",
                "round_to": 0,
            },
            "ADA": {
                "ticker": "ADA-USD",
                "round_to": 2,
            },
            "SPY": {
                "ticker": "SPY",
                "round_to": 2,
            },
        }
        self.update_tickers.start()

    def cog_unload(self):
        self.update_tickers.cancel()

    def cog_load(self):
        self.update_tickers.start()

    @tasks.loop()
    async def update_tickers(self):
        await self.client.wait_until_ready()
        while True:
            for nickname, info in self.tickers.items():
                try:
                    ticker = info["ticker"]
                    open_price = get_open(ticker, info["round_to"])
                    current_price = get_price(ticker, info["round_to"])

                    change = round(current_price - open_price, info["round_to"])
                    change_text = change < 0 and f"-${abs(change)}" or f"+${change}"
                    change_percent = round(change / open_price * 100, 2)
                    change_percent_text = change_percent < 0 and f"-{abs(change_percent)}" or f"+{change_percent}"

                    status = open_price and current_price < open_price and discord.Status.dnd or discord.Status.online
                    await self.client.change_presence(activity = discord.Game(name = f"{nickname}: ${current_price} | {change_percent_text}% | {change_text}"), status = status)
                except requests.exceptions.ConnectionError:
                    print("ERROR: Max retrieves with live tickers")
                except Exception as error_message:
                    print(error_message)
                await asyncio.sleep(UPDATE_TICKERS)

    @commands.command()
    async def getprice(self, context, ticker: str):
        ticker = ticker.upper()
        response = await context.send(embed = create_embed({
            "title": f"Loading share price of {ticker}...",
            "color": discord.Color.gold()
        }))

        try:
            share_price = get_price(ticker)
            if not share_price:
                await response.edit(embed=create_embed({
                    "title": f"Could not get share price of {ticker}",
                    "color": discord.Color.red()
                }))
                return

            await response.edit(embed = create_embed({
                "title": f"{ticker}: ${share_price}"
            }))
        except Exception as error_message:
            await response.edit(embed = create_embed({
                "title": f"Could not get share price of {ticker}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    @commands.command()
    async def recommend(self, context, ticker: str):
        ticker = ticker.upper()
        response = await context.send(embed=create_embed({
            "title": f"Loading recommendation for {ticker}...",
            "color": discord.Color.gold()
        }))

        try:
            recommendation = get_recommendation(ticker)
            if not recommendation:
                await response.edit(embed=create_embed({
                    "title": f"Could not load recommendation for {ticker}",
                    "color": discord.Color.red()
                }))
                return

            summary = recommendation["RECOMMENDATION"]
            color = discord.Color.dark_grey()
            if summary == "STRONG_BUY" or summary == "BUY":
                color = discord.Color.green()
            else:
                color = discord.Color.red()

            await response.edit(embed=create_embed({
                "title": f"{ticker}: {summary}",
                "color": color
            }, {
                "Buy": recommendation["BUY"],
                "Neutral": recommendation["NEUTRAL"],
                "Sell": recommendation["SELL"],
            }))
        except Exception as error_message:
            await response.edit(embed=create_embed({
                "title": f"Could not load recommendation for {ticker}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    @commands.command()
    async def buyshares(self, context, ticker: str, shares_to_purchase: float):
        ticker = ticker.upper()
        shares_to_purchase = round(shares_to_purchase, 4)

        response = await context.send(embed = create_embed({
            "title": f"Buying {shares_to_purchase} shares of {ticker}...",
            "color": discord.Color.gold()
        }))

        try:
            # checks
            if shares_to_purchase <= 0:
                await response.edit(embed = create_embed({
                    "title": f"You must buy more than 0 shares",
                    "color": discord.Color.red()
                }))
                return

            share_price = get_price(ticker)
            if not share_price:
                await response.edit(embed = create_embed({
                    "title": f"Could not get share price of {ticker}",
                    "color": discord.Color.red()
                }))
                return

            # handle money transaction
            total_price = round(share_price * shares_to_purchase, 2)
            user_data = get_user_data(context.author.id)
            user_balance = round(user_data["money"], 2)
            if user_balance < total_price:
                await response.edit(embed = create_embed({
                    "title": f"You do not have enough money to purchase {shares_to_purchase} of {ticker}",
                    "color": discord.Color.red()
                }, {
                    "Total Price": f"${total_price}",
                    "Balance": "${}".format(user_balance)
                }))
                return
                
            user_data["money"] -= total_price                

            # handle share transaction
            if not user_data["stocks"].get(ticker):
                user_data["stocks"][ticker] = {
                    "shares": shares_to_purchase,
                    "average_price": share_price
                }
            else:
                average_price = user_data["stocks"][ticker]["average_price"]
                shares_owned = user_data["stocks"][ticker]["shares"]
                total_shares = user_data["stocks"][ticker]["shares"] + shares_to_purchase
                average_price = round(((average_price * shares_owned) + (share_price * shares_to_purchase)) / total_shares, 2)
                user_data["stocks"][ticker] = {
                    "average_price": average_price,
                    "shares": user_data["stocks"][ticker]["shares"] + shares_to_purchase
                }

            # response
            save_user_data(user_data)
            shares_owned = round(user_data["stocks"][ticker]["shares"], 4)
            average_price = round(user_data["stocks"][ticker]["average_price"], 2)
            await response.edit(embed = create_embed({
                "title": f"Bought {shares_to_purchase} shares of {ticker} at ${share_price} (-${total_price})",
                "color": discord.Color.green()
            }, {
                "Shares Owned": f"{shares_owned} Shares",
                "Average Price": f"${average_price}"
            }))
        except Exception as error_message:
            await response.edit(embed = create_embed({
                "title": f"Could not buy {shares_to_purchase} shares of {ticker}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    @commands.command()
    async def sellshares(self, context, ticker: str, shares_to_sell: float):
        ticker = ticker.upper()
        shares_to_sell = round(shares_to_sell, 4)

        response = await context.send(embed = create_embed({
            "title": f"Selling {shares_to_sell} shares of {ticker}...",
            "color": discord.Color.gold()
        }))
        
        try:
            # checks
            if shares_to_sell <= 0:
                await response.edit(embed = create_embed({
                    "title": f"You must sell more than 0 shares",
                    "color": discord.Color.red()
                }))
                return

            share_price = get_price(ticker)
            if not share_price:
                await response.edit(embed = create_embed({
                    "title": f"Could not get share price of {ticker}",
                    "color": discord.Color.red()
                }))
                return

            # handle money transaction
            total_price = round(share_price * shares_to_sell, 2)

            user_data = get_user_data(context.author.id)
            if not user_data["stocks"].get(ticker) or user_data["stocks"][ticker]["shares"] < shares_to_sell:
                await response.edit(embed = create_embed({
                    "title": f"You don't have enough shares of {ticker} to sell",
                    "color": discord.Color.red()
                }))
                return
            else:
                user_data["money"] += total_price
                user_data["stocks"][ticker]["shares"] -= shares_to_sell
                if user_data["stocks"][ticker]["shares"] == 0:
                    user_data["stocks"].pop(ticker)

            # response
            save_user_data(user_data)

            shares_remaining = 0
            if user_data["stocks"].get(ticker):
                shares_remaining = round(user_data["stocks"][ticker]["shares"], 4)

            await response.edit(embed = create_embed({
                "title": f"Sold {shares_to_sell} shares of {ticker} at ${share_price} (+${total_price})",
                "color": discord.Color.green()
            }, {
                "Shares Remaining": f"{shares_remaining} Shares",
            }))
        except Exception as error_message:
            await response.edit(embed = create_embed({
                "title": f"Could not sell {shares_to_sell} shares of {ticker}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    @commands.command()
    async def portfolio(self, context, member: discord.Member = None):
        if not member:
            member = context.author

        response = await context.send(embed = create_embed({
            "title": f"Loading {member}'s portfolio...",
            "color": discord.Color.gold()
        }))

        try:
            user_data = get_user_data(member.id)
            total_equity = 0
            total_profit = 0
            fields = {}
            for ticker, stock_data in user_data["stocks"].items():
                share_price = get_price(ticker)
                if not share_price:
                    continue

                total_shares = round(stock_data["shares"], 4)
                average_price = round(stock_data["average_price"], 2)
                equity = round(total_shares * average_price, 2)
                profit = round((share_price - average_price) * total_shares, 2)

                total_equity += equity
                total_profit += profit
                fields[ticker.upper()] = f"{total_shares} Shares @ ${average_price} | Equity: ${equity} | Profit: ${profit}"

            total_equity = round(total_equity, 2)
            total_profit = round(total_profit, 2)
            fields["SUMMARY"] = f"Equity: ${total_equity} | Profit: ${total_profit}"
            await response.edit(embed = create_embed({
                "title": f"{member}'s Portfolio"
            }, fields))
        except Exception as error_message:
            await response.edit(embed = create_embed({
                "title": f"Could not load {member}'s portfolio",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    # custom stocks

    @commands.command()
    async def stockinfo(self, context, ticker: str):
        ticker = ticker.upper()
        response = await context.send(embed=create_embed({
            "title": f"Retrieving stock info for {ticker}",
            "color": discord.Color.gold()
        }))

        try:
            stock = get_stock(ticker)
            if not stock:
                await response.edit(embed=create_embed({
                    "title": f"Could not find stock {ticker}",
                    "color": discord.Color.red()
                }))
                return

            current_price = round(stock["current_price"], 2)

            bid_price, bids = None, None
            if len(stock["bids"]) > 0:
                for bid_section in stock["bids"]:
                    if not bid_price or bid_section["current_price"] < bid_price:
                        bid_price = bid_section["current_price"]
                        bids = bid_section["shares"]
            
            ask_price, asks = None, None
            circulating_supply = 0
            if len(stock["asks"]) > 0:
                for ask_section in stock["asks"]:
                    if not ask_price or ask_section["current_price"] > ask_price:
                        ask_price = ask_section["current_price"]
                        asks = ask_section["shares"]
                        circulating_supply += ask_section["shares"]

            outstanding_shares = 0
            for user_data in get_all_user_data():
                if user_data["stocks"].get(ticker):
                    outstanding_shares += user_data["stocks"][ticker]["shares"]

            history_one_day = {}
            history_all = {}
            for timestamp, price in stock["history"].items():
                date = datetime.fromtimestamp(float(timestamp))
                formatted_date = date.strftime("%m/%d/%y")
                history_all[formatted_date] = price

                if date.date() == datetime.today().date():
                    formatted_date = date.strftime("%I:%M:%S %p")
                    history_one_day[formatted_date] = price

            figure, axis = plt.subplots(2)

            axis[0].plot(history_one_day.keys(), history_one_day.values())
            axis[0].set_title("One Day")
            axis[0].set_xlabel("Time")
            axis[0].set_ylabel("Price")
            
            axis[1].plot(history_all.keys(), history_all.values())
            axis[1].set_title("All")
            axis[1].set_xlabel("Time")
            axis[1].set_ylabel("Price")

            if not os.path.isdir(TEMP_PATH):
                os.mkdir(TEMP_PATH)
            plt.savefig(STOCK_CHART_PATH)

            await response.edit(embed=create_embed({
                "title": f"{ticker} - ${current_price}",
            }, {
                "Name": stock["name"],
                "Description": stock["description"],
                "Market Cap": current_price * outstanding_shares, # price * outstanding_shares
                "Outstanding Shares": outstanding_shares, # amount of shares owned hy investors
                "Circulating Supply": circulating_supply, # amount of shares owned by exchange
                "Bid Price": bid_price and f"${bid_price} x {bids}" or "None",
                "Ask Price": ask_price and f"${ask_price} x {asks}" or "None"
            }))

            await context.send(file=discord.File(STOCK_CHART_PATH))
        except Exception as error_message:
            await response.edit(embed=create_embed({
                "title": f"Could not load stock info for {ticker}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    @commands.command()
    async def bid(self, context, ticker: str, shares: int, price: int): # buy
        ticker = ticker.upper()
        price = round(price, 2)
        shares = round(shares)
        shares_text = str(shares)

        response = await context.send(embed=create_embed({
            "title": f"Bidding for {shares} share(s) of {ticker} at ${price}...",
            "color": discord.Color.gold()
        }))

        try:
            if not is_market_open():
                await response.edit(embed = create_embed({
                    "title": f"The trading day has not begun (9:00 AM - 6:00 PM)",
                    "color": discord.Color.red()
                }))
                return

            if shares <= 0:
                await response.edit(embed = create_embed({
                    "title": f"You must bid for more than 0 shares",
                    "color": discord.Color.red()
                }))
                return

            if price <= 0:
                await response.edit(embed = create_embed({
                    "title": f"Your bid price must be greater than $0",
                    "color": discord.Color.red()
                }))
                return


            # check if stock exists
            stock = get_stock(ticker)
            if not stock:
                await response.edit(embed=create_embed({
                    "title": f"Could not find stock {ticker}",
                    "color": discord.Color.red()
                }))
                return

            # check if user has enough money to buy the shares
            user_data = get_user_data(context.author.id)
            total_price = price * shares
            balance = user_data["money"]
            if balance < total_price:
                await response.edit(embed=create_embed({
                    "title": f"You do not have enough money to bid for {shares} share(s) of {ticker} at ${price}",
                    "color": discord.Color.red()
                }, {
                    "Balance": f"${balance}",
                    "Total Price": f"${total_price}"
                }))
                return

            # fill ask orders
            for index, ask_order in enumerate(stock["asks"]):
                if ask_order["current_price"] == price:
                    if shares >= ask_order["shares"]:
                        shares_bought = stock["asks"][index]["shares"]
                        shares -= shares_bought
                        stock["current_price"] = price
                        stock["history"][str(time.time())] = price

                        # give user shares
                        if not user_data["stocks"].get(ticker):
                            user_data["stocks"][ticker] = {
                                "shares": shares_bought,
                                "average_price": price
                            }
                        else:
                            average_price = user_data["stocks"][ticker]["average_price"]
                            shares_owned = user_data["stocks"][ticker]["shares"]
                            total_shares = user_data["stocks"][ticker]["shares"] + shares_bought
                            average_price = round(((average_price * shares_owned) + (price * shares_bought)) / total_shares, 2)
                            user_data["stocks"][ticker] = {
                                "average_price": average_price,
                                "shares": user_data["stocks"][ticker]["shares"] + shares_bought
                            }

                        # update seller's data
                        seller_data = get_user_data(ask_order["user_id"])
                        if user_data["user_id"] != seller_data["user_id"]:
                            seller_data["money"] += shares_bought * price
                            save_user_data(seller_data)

                        # finish trade
                        stock["asks"][index]["shares"] = 0
                    else:
                        
                        stock["asks"][index]["shares"] -= shares
                        stock["current_price"] = price
                        stock["history"][str(time.time())] = price

                        # give user shares
                        if not user_data["stocks"].get(ticker):
                            user_data["stocks"][ticker] = {
                                "shares": shares,
                                "average_price": price
                            }
                        else:
                            average_price = user_data["stocks"][ticker]["average_price"]
                            shares_owned = user_data["stocks"][ticker]["shares"]
                            total_shares = user_data["stocks"][ticker]["shares"] + shares
                            average_price = round(((average_price * shares_owned) + (price * shares)) / total_shares, 2)
                            user_data["stocks"][ticker] = {
                                "average_price": average_price,
                                "shares": user_data["stocks"][ticker]["shares"] + shares
                            }

                        # update seller's data
                        seller_data = get_user_data(ask_order["user_id"])
                        if user_data["user_id"] != seller_data["user_id"]:
                            seller_data["money"] += shares * price
                            save_user_data(seller_data)

                        # finish trade
                        shares = 0

                    if ask_order["shares"] == 0:
                        stock["asks"].pop(index)
                        
                    break

            # send bid order if bid could not be filled
            if shares > 0:
                for index, bid_section in enumerate(stock["bids"]):
                    if bid_section["current_price"] == price:
                        stock["bids"][index]["shares"] += shares
                        break
                else:
                    stock["bids"].append({
                        "current_price": price,
                        "shares": shares,
                        "user_id": context.author.id,
                    })

            user_data["money"] -= shares * price
            save_user_data(user_data)
            save_stock(stock)

            await response.edit(embed=create_embed({
                "title": f"Bought {int(shares_text) - shares}/{shares_text} shares of {ticker} at ${price}",
                "color": discord.Color.green()
            }))
        except Exception as error_message:
            await response.edit(embed=create_embed({
                "title": f"Could not bid for {shares}/{shares_text} shares of {ticker} at ${price}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    @commands.command()
    async def ask(self, context, ticker: str, shares: int, price: int): # sell
        ticker = ticker.upper()
        price = round(price, 2)
        shares = round(shares)
        shares_text = str(shares)

        response = await context.send(embed=create_embed({
            "title": f"Asking for {shares} share(s) of {ticker} at ${price}...",
            "color": discord.Color.gold()
        }))

        try:
            if not is_market_open():
                await response.edit(embed = create_embed({
                    "title": f"The trading day has not begun (9:00 AM - 6:00 PM)",
                    "color": discord.Color.red()
                }))
                return

            if shares <= 0:
                await response.edit(embed = create_embed({
                    "title": f"You must ask more than 0 shares",
                    "color": discord.Color.red()
                }))
                return

            if price <= 0:
                await response.edit(embed = create_embed({
                    "title": f"Your ask price must be greater than $0",
                    "color": discord.Color.red()
                }))
                return

            # check if stock exists
            stock = get_stock(ticker)
            if not stock:
                await response.edit(embed=create_embed({
                    "title": f"Could not find stock {ticker}",
                    "color": discord.Color.red()
                }))
                return

            user_data = get_user_data(context.author.id)
            if not user_data["stocks"].get(ticker) or user_data["stocks"][ticker]["shares"] < shares:
                await response.edit(embed = create_embed({
                    "title": f"You don't have enough shares of {ticker} to sell",
                    "color": discord.Color.red()
                }))
                return

            # fill bid orders
            for index, bid_order in enumerate(stock["bids"]):
                if bid_order["current_price"] == price:
                    if shares >= bid_order["shares"]:
                        shares_sold = stock["bids"][index]["shares"]
                        shares -= shares_sold
                        user_data["money"] += shares_sold * price
                        stock["current_price"] = price
                        stock["history"][str(time.time())] = price

                        # give buyer shares
                        buyer_data = get_user_data(bid_order["user_id"])
                        if not buyer_data["stocks"].get(ticker):
                            buyer_data["stocks"][ticker] = {
                                "shares": shares_sold,
                                "average_price": price
                            }
                        else:
                            average_price = buyer_data["stocks"][ticker]["average_price"]
                            shares_owned = buyer_data["stocks"][ticker]["shares"]
                            total_shares = buyer_data["stocks"][ticker]["shares"] + shares_sold
                            average_price = round(((average_price * shares_owned) + (price * shares_sold)) / total_shares, 2)
                            buyer_data["stocks"][ticker] = {
                                "average_price": average_price,
                                "shares": buyer_data["stocks"][ticker]["shares"] + shares_sold
                            }

                        # update seller's data
                        save_user_data(buyer_data)

                        # finish trade
                        stock["bids"][index]["shares"] = 0
                    else:
                        user_data["money"] += shares * price
                        stock["bids"][index]["shares"] -= shares
                        stock["current_price"] = price
                        stock["history"][str(time.time())] = price

                        # give buyer shares
                        buyer_data = get_user_data(bid_order["user_id"])
                        if not buyer_data["stocks"].get(ticker):
                            buyer_data["stocks"][ticker] = {
                                "shares": shares,
                                "average_price": price
                            }
                        else:
                            average_price = buyer_data["stocks"][ticker]["average_price"]
                            shares_owned = buyer_data["stocks"][ticker]["shares"]
                            total_shares = buyer_data["stocks"][ticker]["shares"] + shares
                            average_price = round(((average_price * shares_owned) + (price * shares)) / total_shares, 2)
                            buyer_data["stocks"][ticker] = {
                                "average_price": average_price,
                                "shares": buyer_data["stocks"][ticker]["shares"] + shares
                            }

                        save_user_data(buyer_data)

                        # finish trade
                        shares = 0

                    if bid_order["shares"] == 0:
                        stock["bids"].pop(index)
                        
                    break

            # send ask order if ask could not be filled
            if shares > 0:
                for index, ask_section in enumerate(stock["asks"]):
                    if ask_section["current_price"] == price:
                        stock["asks"][index]["shares"] += shares
                        break
                else:
                    stock["asks"].append({
                        "current_price": price,
                        "shares": shares,
                        "user_id": context.author.id,
                    })

            user_data["stocks"][ticker]["shares"] -= int(shares_text)
            if user_data["stocks"][ticker]["shares"] == 0:
                user_data["stocks"].pop(ticker)

            save_user_data(user_data)
            save_stock(stock)

            await response.edit(embed=create_embed({
                "title": f"Sold {int(shares_text) - shares}/{shares_text} shares of {ticker} at ${price}",
                "color": discord.Color.green()
            }))
        except Exception as error_message:
            await response.edit(embed=create_embed({
                "title": f"Could not ask for {shares}/{shares_text} shares of {ticker} at ${price}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    @commands.command()
    async def cancelorder(self, context, ticker: str, order_type: str, shares: int, price: int):
        order_type = order_type.lower()
        ticker = ticker.upper()
        price = round(price, 2)
        shares = round(shares)

        response = await context.send(embed=create_embed({
            "title": f"Canceling an existing order to {order_type} for {shares} shares of {ticker} at ${price}",
            "color": discord.Color.gold()
        }))

        try:
            if order_type != "ask" and order_type != "bid":
                await response.edit(embed=create_embed({
                    "title": f"The order type must be \"ask\" or \"bid\"",
                    "color": discord.Color.red()
                }))
                return

            if shares <= 0:
                await response.edit(embed = create_embed({
                    "title": f"You must cancel an order of more than 0 shares",
                    "color": discord.Color.red()
                }))
                return

            if price <= 0:
                await response.edit(embed = create_embed({
                    "title": f"You must cancel an order of a price greater than $0",
                    "color": discord.Color.red()
                }))
                return

            stock = get_stock(ticker)
            if not stock:
                await response.edit(embed=create_embed({
                    "title": f"Could not find stock {ticker}",
                    "color": discord.Color.red()
                }))
                return

            user_data = get_user_data(context.author.id)

            if order_type == "ask":
                for index, ask_order in enumerate(stock["asks"]):
                    ask_order_shares = ask_order["shares"]
                    ask_order_price = ask_order["current_price"]
                    if ask_order["user_id"] == context.author.id and shares == ask_order_shares and ask_order_price == price:
                        if not user_data["stocks"].get(ticker):
                            user_data["stocks"][ticker] = {
                                "shares": ask_order_shares,
                                "average_price": ask_order_price
                            }
                        else:
                            average_price = user_data["stocks"][ticker]["average_price"]
                            shares_owned = user_data["stocks"][ticker]["shares"]
                            total_shares = user_data["stocks"][ticker]["shares"] + ask_order_shares
                            average_price = round(((average_price * shares_owned) + (ask_order_price * ask_order_shares)) / total_shares, 2)
                            user_data["stocks"][ticker] = {
                                "average_price": average_price,
                                "shares": user_data["stocks"][ticker]["shares"] + ask_order_shares
                            }

                        stock["asks"].pop(index)
                        break
                else:
                    await response.edit(embed=create_embed({
                        "title": f"Could not find an existing order to {order_type} for {shares} shares of {ticker} at ${price}",
                        "color": discord.Color.red()
                    }))
                    return
            elif order_type == "bid":
                for index, bid_order in enumerate(stock["bids"]):
                    bid_order_shares = bid_order["shares"]
                    bid_order_price = bid_order["current_price"]
                    if bid_order["user_id"] == context.author.id and shares == bid_order_shares and bid_order_price == price:
                        user_data["money"] += bid_order_shares * bid_order_price
                        stock["bids"].pop(index)
                        break
                else:
                    await response.edit(embed=create_embed({
                        "title": f"Could not find an existing order to {order_type} for {shares} shares of {ticker} at ${price}",
                        "color": discord.Color.red()
                    }))
                    return

            save_user_data(user_data)
            save_stock(stock)

            await response.edit(embed=create_embed({
                "title": f"Canceled an existing order to {order_type} for {shares} shares of {ticker} at ${price}",
                "color": discord.Color.green()
            }))

        except Exception as error_message:
            await response.edit(embed=create_embed({
                "title": f"Could not cancel an existing order to {order_type} for {shares} shares of {ticker} at ${price}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

    @commands.command()
    async def getorders(self, context, ticker: str, order_type: str):
        order_type = order_type.lower()
        response = await context.send(embed=create_embed({
            "title": f"Retrieving {order_type} orders of {ticker}",
            "color": discord.Color.gold()
        }))

        try:
            if order_type != "ask" and order_type != "bid":
                await response.edit(embed=create_embed({
                    "title": f"The order type must be \"ask\" or \"bid\"",
                    "color": discord.Color.red()
                }))
                return

            stock = get_stock(ticker)
            if not stock:
                await response.edit(embed=create_embed({
                    "title": f"Could not find stock {ticker}",
                    "color": discord.Color.red()
                }))
                return

            fields = {}
            for order in order_type == "ask" and stock["asks"] or stock["bids"]:
                current_price = order["current_price"]
                shares = order["shares"]
                member = context.guild.get_member(order["user_id"]) or order["user_id"]
                fields[f"{shares} x ${current_price}"] = member

            save_stock(stock)

            await response.edit(embed=create_embed({
                "title": order_type == "ask" and f"{ticker} - Ask Orders" or f"{ticker} - Bid Orders",
            }, fields))
        except Exception as error_message:
            await response.edit(embed=create_embed({
                "title": f"Could not retrieve {order_type} orders of {ticker}",
                "color": discord.Color.red()
            }, {
                "Error Message": error_message
            }))

def setup(client):
    client.add_cog(stocks(client))
