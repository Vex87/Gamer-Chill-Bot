PREFIX = "?"
DEFAULT_GUILD_SETTINGS = {"guild_id": None}
DEFAULT_USER_DATA = {"user_id": None}
EXTENSIONS = [
    "events",
    "bot",
    "default",
    "fun",
    "moderation",
    "server",
    "vc",
    "subscriptions",
    "leveling",
    "economy",
    "stocks"
]

ACAS_BLACKLISTED_DAYS = [4, 5, 6]
ACAS_REMINDER_BLOCK_TIMES = ["09:20:00", "10:50:00", "12:35:00", "14:35:00"]
ACAS_BLOCK_TIMES = ["09:25:00", "10:55:00", "12:40:00", "14:40:00"]
ACAS_UPDATE_DELAY = 1

ECONOMY_MAX_FIELDS_FOR_LEADERBOARD_EMBED = 10
ECONOMY_STARTING_MONEY = 1000

VC_LANGUAGE = "en"
VC_ACCENT = "com"
VC_VOICE_IS_SLOW = False

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

SUBSCRIPTIONS_STATUS_URL = "http://api.roblox.com/users/USER_ID/onlinestatus/"
SUBSCRIPTIONS_USERNAME_URL = "http://api.roblox.com/users/USER_ID"
SUBSCRIPTIONS_UPDATE_DELAY = 60

LEVELING_UPDATE_DELAY = 60
LEVELING_MESSAGE_COOLDOWN = 30
LEVELING_MESSAGE_EXP = 5
LEVELING_VOICE_EXP = 1
LEVELING_LEVEL_DIFFICULTY = 20
LEVELING_MAX_BOXES_FOR_RANK_EMBED = 10
LEVELING_MAX_FIELDS_FOR_LEADERBOARD_EMBED = 10
LEVELING_DEFAULT_EXPERIENCE = 0
LEVELING_MONEY_PER_LEVEL = 50

LEVELING_FILL_EMOJI = "🟦"
LEVELING_UNFILL_EMOJI = "⬜"

STOCKS_PERIOD = "2h"
STOCKS_INTERVAL = "1m"

VERSION_LOGS = {
    "1.0.13": "Rounded values in ?bal",
    "1.0.12": "Fixed showing incorrect accents.",
    "1.0.11": "Fixed notifying users of subscriptions upon bot startup",
    "1.0.10": "Added ?get to view valid vc_accent and vc_language settings.",
    "1.0.9": "Made ?forbes list net-worth instead of bank balance.",
    "1.0.8": "Created specific permissions for changing certain settings.",
    "1.0.7": "Merged ACAS with subscriptions. Do `?subscribe acas` to subscribe/unsubscribe from acas. Fixed acas not announcing block 1.",
    "1.0.6": "Added net-worth to ?bal",
    "1.0.5": "Removed minecraft subscription and status because it caused the bot to randomly disconnect and slow down.",
    "1.0.4": "Added money reward for leveling up.",
    "1.0.3": "Fixed ACAS not making announcements.",
    "1.0.2": "Added ?updatelog.",
    "1.0.1": "Added ?status and minecraft server subscriptions.",
    "1.0.0": "Added settings, more portfolio info, and increased performance.",
}