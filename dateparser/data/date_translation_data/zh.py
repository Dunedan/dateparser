# -*- coding: utf-8 -*-
info = {
    "name": "zh",
    "date_order": "YMD",
    "january": [
        "一月",
        "1月"
    ],
    "february": [
        "二月",
        "2月"
    ],
    "march": [
        "三月",
        "3月"
    ],
    "april": [
        "四月",
        "4月"
    ],
    "may": [
        "五月",
        "5月"
    ],
    "june": [
        "六月",
        "6月"
    ],
    "july": [
        "七月",
        "7月"
    ],
    "august": [
        "八月",
        "8月"
    ],
    "september": [
        "九月",
        "9月"
    ],
    "october": [
        "十月",
        "10月"
    ],
    "november": [
        "十一月",
        "11月"
    ],
    "december": [
        "十二月",
        "12月"
    ],
    "monday": [
        "星期一",
        "周一",
        "礼拜一"
    ],
    "tuesday": [
        "星期二",
        "周二",
        "礼拜二"
    ],
    "wednesday": [
        "星期三",
        "周三",
        "礼拜三"
    ],
    "thursday": [
        "星期四",
        "周四",
        "礼拜四"
    ],
    "friday": [
        "星期五",
        "周五",
        "礼拜五"
    ],
    "saturday": [
        "星期六",
        "周六",
        "礼拜六"
    ],
    "sunday": [
        "星期日",
        "周日",
        "星期天",
        "礼拜日"
    ],
    "am": [
        "上午"
    ],
    "pm": [
        "下午"
    ],
    "year": [
        "年"
    ],
    "month": [
        "月",
        "个月",
        "個月"
    ],
    "week": [
        "周",
        "星期"
    ],
    "day": [
        "日",
        "天"
    ],
    "hour": [
        "小时"
    ],
    "minute": [
        "分钟",
        "分"
    ],
    "second": [
        "秒"
    ],
    "relative-type": {
        "1 year ago": [
            "去年"
        ],
        "0 year ago": [
            "今年"
        ],
        "in 1 year": [
            "明年"
        ],
        "1 month ago": [
            "上个月"
        ],
        "0 month ago": [
            "本月"
        ],
        "in 1 month": [
            "下个月"
        ],
        "1 week ago": [
            "上周"
        ],
        "0 week ago": [
            "本周"
        ],
        "in 1 week": [
            "下周"
        ],
        "1 day ago": [
            "昨天"
        ],
        "0 day ago": [
            "今天"
        ],
        "in 1 day": [
            "明天"
        ],
        "0 hour ago": [
            "这一时间 / 此时"
        ],
        "0 minute ago": [
            "此刻"
        ],
        "0 second ago": [
            "现在"
        ],
        "2 day ago": [
            "前天"
        ]
    },
    "relative-type-regex": {
        "in \\1 year": [
            "(\\d+)年后"
        ],
        "\\1 year ago": [
            "(\\d+)年前"
        ],
        "in \\1 month": [
            "(\\d+)个月后"
        ],
        "\\1 month ago": [
            "(\\d+)个月前"
        ],
        "in \\1 week": [
            "(\\d+)周后"
        ],
        "\\1 week ago": [
            "(\\d+)周前"
        ],
        "in \\1 day": [
            "(\\d+)天后"
        ],
        "\\1 day ago": [
            "(\\d+)天前"
        ],
        "in \\1 hour": [
            "(\\d+)小时后"
        ],
        "\\1 hour ago": [
            "(\\d+)小时前"
        ],
        "in \\1 minute": [
            "(\\d+)分钟后"
        ],
        "\\1 minute ago": [
            "(\\d+)分钟前"
        ],
        "in \\1 second": [
            "(\\d+)秒钟后",
            "(\\d+)秒后"
        ],
        "\\1 second ago": [
            "(\\d+)秒钟前",
            "(\\d+)秒前"
        ]
    },
    "locale_specific": {},
    "no_word_spacing": "True",
    "skip": [
        "约",
        " ",
        ".",
        ",",
        ";",
        "-",
        "/",
        "'",
        "|",
        "@",
        "[",
        "]",
        "，"
    ],
    "ago": [
        "前"
    ],
    "in": [
        "在"
    ],
    "simplifications": [
        {
            "半小时前": "30分前"
        },
        {
            "(?:中午|下午|(?:晚上?))(?:\\s*)(\\d+)(?:\\s*):(?:\\s+|:)?(\\d+)": "\\1:\\2 pm"
        },
        {
            "(?:上午|早上|凌晨)(?:\\s*)(\\d+)(?:\\s*):(?:\\s+|:)?(\\d+)": "\\1:\\2 am"
        },
        {
            "中午": "12:00"
        },
        {
            "(\\d+)年(?:\\s+)?(\\d+)月(?:\\s+)?(\\d+)日(?:\\s+)?(\\d+)时(?:\\s+)?(\\d+)分": "\\1-\\2-\\3 \\4:\\5"
        },
        {
            "(\\d+)年(?:\\s+)?(\\d+)月(?:\\s+)?(\\d{1,2})(?:日)?(?:\\s+)?(\\d{1,2})(?:点|:)(\\d{1,2})": "\\1-\\2-\\3 \\4:\\5"
        },
        {
            "(\\d+)年(?:\\s+)?(\\d+)月(?:\\s+)?(\\d{1,2})(?:日)?": "\\1-\\2-\\3"
        },
        {
            "(\\d+)月(?=.*[前后])": "\\1 月"
        }
    ]
}