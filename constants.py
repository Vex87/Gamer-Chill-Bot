EXTENSIONS = [
    "events",
    "bot",
    "default",
    "fun",
    "vc",
    "acas",
    "leveling",
    "economy",
    "stocks",
    "bank",
    "terminal"
]

DEFAULT_GUILD_DATA = {
    "guild_id": None,
    "prefix": "?",
    "vc_language": "en",
    "vc_accent": "com",
    "vc_slow_mode": False,
    "message_cooldown": 10,
    "exp_per_message": 5,
    "exp_channels": [],
    "join_channel": None,
    "default_role": None,
    "acas_channel": None,
    "acas_role": None,
    "acas_enabled": False,
    "voice_exp": 1,
    "money_per_level": 10,
    "bank_manager": None,
    "bank_balance": 0,
    "daily_exp": 100,
}

DEFAULT_USER_DATA = {
    "user_id": None,
    "money": 1000,
    "experience": 0,
    "stocks": {},
    "acas_subscribed": False,
    "daily_streak": 0,
    "claimed_daily_timestamp": 0,
}

SETTINGS = {
    "prefix <prefix: str>": "Changes the bot's prefix for activating commands.",
    "vc_language <lan: str>": "Changes the bot's TTS language.",
    "vc_accent <acc: str>": "Changes the bot's TTS accent.",
    "vc_slow_mode <is_slow: bool": "Changes whether the bot will speak slowly.",
    "message_cooldown <sec: int>": "Changes the cooldown for earning EXP for messaging.",
    "exp_per_message <exp: int>": "Changes the amount of EXP a user will receive for messaging.",
    "exp_channels <chann: chann>": "Adds/removes a channel where users can receive EXP for messaging.",
    "join_channel <chann: chann>": "Changes the channel where member join and leave messages will be sent.",
    "default_role <role: role>": "Changes the role that will be given to members who join the server.",
    "acas_channel <chann: chann>": "Changes the channel where ACAS announcements will be sent.",
    "acas_role <role: role>": "Changes the role that will be pinged for every ACAS announcement.",
    "acas_enabled <is_enabled: bool>": "Changes whether ACAS announcements will be sent.",
    "voice_exp <exp: int>": "Changes the amount of EXP rewarded to members for being connected to a VC every minute."
}

GET_FLAGS = {
    "vc_language": "Supported TTS languages.",
    "vc_accent": "Supported TTS accents.",
}

VC_ACCENTS = {
    "com": "Worldwide (Original for the United States)",
    "ac": "Ascension Island",
    "ad": "Andorra",
    "ae": "United Arab Emirates",
    "com.af": "Afghanistan",
    "com.ag": "Antigua and Barbuda",
    "com.ai": "Anguilla",
    "al": "Albania",
    "am": "Armenia",
    "co.ao": "Angola",
    "com.ar": "Argentina",
    "as": "American Samoa",
    "at": "Austria",
    "com.au": "Australia",
    "az": "Azerbaijan",
    "ba": "Bosnia and Herzegovina",
    "com.bd": "Bangladesh",
    "be": "Belgium",
    "bf": "Burkina Faso",
    "bg": "Bulgaria",
    "com.bh": "Bahrain",
    "bi": "Burundi",
    "bj": "Benin",
    "com.bn": "Brunei",
    "com.bo": "Bolivia",
    "com.br": "Brazil",
    "bs": "Bahamas",
    "bt": "Bhutan",
    "co.bw": "Botswana",
    "by": "Belarus",
    "com.bz": "Belize",
    "ca": "Canada",
    "com.kh": "Cambodia",
    "cc": "Cocos (Keeling) Islands",
    "cd": "Democratic Republic of the Congo",
    "cf": "Central African Republic",
    "cat": "Catalan Countries",
    "cg": "Republic of the Congo",
    "ch": " Switzerland",
    "ci": "Ivory Coast",
    "co.ck": "Cook Islands",
    "cl": "Chile",
    "cm": "Cameroon",
    "cn": "China",
    "g.cn": "China",
    "com.co": "Colombia",
    "co.cr": "Costa Rica",
    "com.cu": "Cuba",
    "cv": "Cape Verde",
    "com.cy": "Cyprus",
    "cz": "Czech Republic",
    "de": "Germany",
    "dj": "Djibouti",
    "dk": "Denmark",
    "dm": "Dominica",
    "com.do": "Dominican Republic",
    "dz": "Algeria",
    "com.ec": "Ecuador",
    "ee": "Estonia",
    "com.eg": "Egypt",
    "es": "Spain",
    "com.et": "Ethiopia",
    "fi": "Finland",
    "com.fj": "Fiji",
    "fm": "Federated States of Micronesia",
    "fr": "France",
    "ga": "Gabon",
    "ge": "Georgia",
    "gf": "French Guiana",
    "gg": "Guernsey",
    "com.gh": "Ghana",
    "com.gi": "Gibraltar",
    "gl": "Greenland",
    "gm": "Gambia",
    "gp": "Guadeloupe",
    "gr": "Greece",
    "com.gt": "Guatemala",
    "gy": "Guyana",
    "com.hk": "Hong Kong",
    "hn": "Honduras",
    "hr": "Croatia",
    "ht": "Haiti",
    "hu": "Hungary",
    "co.id": "Indonesia",
    "iq": "Iraq",
    "ie": "Ireland",
    "co.il": "Israel",
    "im": "Isle of Man",
    "co.in": "India",
    "io": "British Indian Ocean Territory",
    "is": "Iceland",
    "it": "Italy",
    "je": "Jersey",
    "com.jm": "Jamaica",
    "jo": "Jordan",
    "co.jp": "Japan",
    "co.ke": "Kenya",
    "ki": "Kiribati",
    "kg": "Kyrgyzstan",
    "co.kr": "South Korea",
    "com.kw": "Kuwait",
    "kz": "Kazakhstan",
    "la": "Laos",
    "com.lb": "Lebanon",
    "com.lc": "Saint Lucia",
    "li": "Liechtenstein",
    "lk": "Sri Lanka",
    "co.ls": "Lesotho",
    "lt": "Lithuania",
    "lu": "Luxembourg",
    "lv": "Latvia",
    "com.ly": "Libya",
    "co.ma": "Morocco",
    "md": "Moldova",
    "me": "Montenegro",
    "mg": "Madagascar",
    "mk": "Macedonia",
    "ml": "Mali",
    "com.mm": "Myanmar",
    "mn": "Mongolia",
    "ms": "Montserrat",
    "com.mt": "Malta",
    "mu": "Mauritius",
    "mv": "Maldives",
    "mw": "Malawi",
    "com.mx": "Mexico",
    "com.my": "Malaysia",
    "co.mz": "Mozambique",
    "com.na": "Namibia",
    "ne": "Niger",
    "com.nf": "Norfolk Island",
    "com.ng": "Nigeria",
    "com.ni": "Nicaragua",
    "nl": "Netherlands",
    "no": "Norway",
    "com.np": " Nepal",
    "nr": "Nauru",
    "nu": "Niue",
    "co.nz": "New Zealand",
    "com.om": "Oman",
    "com.pk": "Pakistan",
    "com.pa": "Panama",
    "com.pe": "Peru",
    "com.ph": "Philippines",
    "pl": "Poland",
    "com.pg": "Papua New Guinea",
    "pn": "Pitcairn Islands",
    "com.pr": "Puerto Rico",
    "ps": "Palestine[4]",
    "pt": "Portugal",
    "com.py": "Paraguay",
    "com.qa": "Qatar",
    "ro": "Romania",
    "rs": "Serbia",
    "ru": "Russia",
    "rw": "Rwanda",
    "com.sa": "Saudi Arabia",
    "com.sb": "Solomon Islands",
    "sc": "Seychelles",
    "se": "Sweden",
    "com.sg": "Singapore",
    "sh": "Saint Helena, Ascension and Tristan da Cunha",
    "si": "Slovenia",
    "sk": "Slovakia",
    "com.sl": "Sierra Leone",
    "sn": "Senegal",
    "sm": "San Marino",
    "so": "Somalia",
    "st": "São Tomé and Príncipe",
    "sr": "Suriname",
    "com.sv": "El Salvador",
    "td": "Chad",
    "tg": "Togo",
    "co.th": "Thailand",
    "com.tj": "Tajikistan",
    "tk": "Tokelau",
    "tl": "Timor-Leste",
    "tm": "Turkmenistan",
    "to": "Tonga",
    "tn": "Tunisia",
    "com.tr": "Turkey",
    "tt": "Trinidad and Tobago",
    "com.tw": "Taiwan",
    "co.tz": "Tanzania",
    "com.ua": "Ukraine",
    "co.ug": "Uganda",
    "co.uk": "United Kingdom",
    "com": "United States",
    "com.uy": "Uruguay",
    "co.uz": "Uzbekistan",
    "com.vc": "Saint Vincent and the Grenadines",
    "co.ve": "Venezuela",
    "vg": "British Virgin Islands",
    "co.vi": "United States Virgin Islands",
    "com.vn": "Vietnam",
    "vu": "Vanuatu",
    "ws": "Samoa",
    "co.za": "South Africa",
    "co.zm": "Zambia",
    "co.zw": "Zimbabwe"
}

VC_LANGUAGES = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en-au": "English (Australia)",
    "en-ca": "English (Canada)",
    "en-gb": "English (UK)",
    "en-gh": "English (Ghana)",
    "en-ie": "English (Ireland)",
    "en-in": "English (India)",
    "en-ng": "English (Nigeria)",
    "en-nz": "English (New Zealand)",
    "en-ph": "English (Philippines)",
    "en-tz": "English (Tanzania)",
    "en-uk": "English (UK)",
    "en-us": "English (US)",
    "en-za": "English (South Africa)",
    "en": "English",
    "eo": "Esperanto",
    "es-es": "Spanish (Spain)",
    "es-us": "Spanish (United States)",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fr-ca": "French (Canada)",
    "fr-fr": "French (France)",
    "fr": "French",
    "gu": "Gujarati",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jw": "Javanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "la": "Latin",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt-br": "Portuguese (Brazil)",
    "pt-pt": "Portuguese (Portugal)",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Filipino",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-CN": "Chinese",
    "zh-cn": "Chinese (Mandarin/China)",
    "zh-tw": "Chinese (Mandarin/Taiwan)"
}

EIGHTBALL_RESPONSES = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "No.",
    "Your question isn't important, but btc to the moon is.",
    "Ask better questions next time.",
]

COMMANDS = {
    "Default": {
        "acas": "Subscribes/unsubscribes to ACAS. Server command only.",
        "help": "Retrieves bot commands.",
        "userinfo <user>": "Retrieves info of the user.",
        "serverinfo": "Retrieves server info. Server command only.",
        "settings": "Retrieves/changes settings. Server command only.",
        "messageleaderboard": "Retrieves the users with the most messages in the server.",
        # "clear <amount>": "Clears the amount of messages in the channel.",
    },
    "Economy": {
        "bal": "Retrieves your balanace.",
        "forbes": "Retrieves the users in the server with the most money.",
        "give <member> <amount>": "Gives the user money.",
    },
    "Leveling": {
        "rank <user>": "Retrieves the user's rank.",
        "leaderboard": "Retrieves the users in the server with the highest level.",
    },
    "Bank": {
        "bank": "Retrieves the bank's balance. Server command only.",
        "print <amount>": "Adds money to the bank's balance. Server command only.",
        "loan <member> <amount>": "Transfers money from the bank to the user. Server command only.",
        "fine <member> <amount>": "Transfers money from the user to the bank. Server command only.",
    },
    "Stocks": {
        "getprice <ticker>": "Gets the price of the stock.",
        "buyshares <ticker> <shares>": "Buys shares of the stock.",
        "sellshares <ticker> <shares>": "Sells owned shares of the stock.",
        "portfolio <user>": "Retrieves the user's points.",
        "stockinfo <ticker>": "Get stock info for custom stocks.",
        "bid <ticker> <shares> <price>": "Buys shares of a custom stock at a specific price. A seller must sell their shares in order for the buyer to receive them.",
        "ask <ticker> <shares> <price>": "Sells shares of a custom stock at a specific price. A buyer must buy the seller's shares in order for the seller to earn money."
    },
    "Fun": {
        "8ball": "Retrieves a random response to a question.",
        "roll <number>": "Retrieves a die of number.",
        "impersonate": "Impersonates sending a message as a user.",
        "randomperson": "Retrieves a random user in the server.",
        "m": "Retrieves a random meme from r/meme. DM command only.",
        "join": "Makes the bot join your VC.",
        "leave": "Makes the bot leave your VC.",
        "say <message>": "Makes the bot say the message. Server command only.",
    },
    "Bot": {
        "load <extension>": "Loads an extension.",
        "unload <extension>": "Unloads an extension.",
        "reload <extension>": "Reloads an extension.",
        "update": "Reloads all extensions.",
        "run <code>": "Runs code through the bot.",
        "cls": "Clears the terminal.",
        "restart": "Restarts the bot.",
        "info": "Retrieves the bot's ping, invite link, uptime, connected servers, members watching, and users watching."
        # "changeactivity <activity>": "Changes the bot's activity.",
        # "changestatus <status>": "Changes the bot's status.",
    },
}

ACAS_BLACKLISTED_DAYS = [4, 5, 6]
ACAS_REMINDER_BLOCK_TIMES = ["09:20:00", "10:50:00", "12:35:00", "14:35:00"]
ACAS_BLOCK_TIMES = ["09:25:00", "10:55:00", "12:40:00", "14:40:00"]
ACAS_UPDATE_DELAY = 1

LEVELING_UPDATE_DELAY = 60
LEVELING_LEVEL_DIFFICULTY = 500

UPDATE_TICKERS = 5
TICKER_PERIOD = "w"
TICKER_INTERVAL = "1d"

MAX_LEADERBOARD_FIELDS = 10
MAX_FILL = 10

FILL_EMOJI = "🟦"
UNFILL_EMOJI = "⬜"
CHECK_EMOJI = "✅"
NEXT_EMOJI = "▶️"
BACK_EMOJI = "◀️"
CHANGE_EMOJI = "\N{gear}"

IS_TESTING = False
CURRENT_VERSION = "9.0.1"
LIVE_DATASTORE = "datastore5"
TESTING_DATASTORE = "datastore2"

MAX_MEMES = 10
MEME_SUBREDDIT = "memes"

DELETE_RESPONSE_DELAY = 3
WAIT_DELAY = 3

TEMP_PATH = "__temp__"
TTS_PATH = "__temp__/tts.mp3"
