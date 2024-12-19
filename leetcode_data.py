import requests
import re
import json

cookies = {
    'csrftoken': '898UDqmnGmITtIQyu4DFayTdkUorMgP1IcoJtOm7VdT5wNCxB1aR6CDay9bVosYY',
    'INGRESSCOOKIE': '2770f9de78e7b289c8ecdd6c312de8e2|8e0876c7c1464cc0ac96bc2edceabd27',
    '__cf_bm': 's_PUtZoMP.V27WrzI.s4HV3gBxsfMMlt7mGz6lcIt5c-1734414341-1.0.1.1-wYKIh33_de4bYNNmmcrU9bLzQagCVq10k1RDw262oKQPEIDjH7hhcIEZj7C1KiIzdRuUFR8KC8NgK2zgRvZG8A',
    'ip_check': '(false, "2409:40e0:100c:eb97:de:473a:aebc:b5b2")',
    'cf_clearance': 'V_iKmzGEK7Om.UgykifBVHlhbB9Q3sL7fT3IIsisNZs-1734414377-1.2.1.1-dd_d9SuAO07rPt6Tij754HvAfKNKPToMtDrotwx1cGEiB3GwFSp930uu7ZU3Nuc3mqd9wSP.wVXGQeR23zBlBv_omAa_CZc.PRc6_jk_bSWy6wN9eoDS7cIfm6yE9IoFKdnu88c8gkBV6_mXQ5wPpSSBQOBJgy1.KFgVu9AGfvNDm8ELZH3abStSU3Qhq2Mue2lni2kpl3tzNTzpOCV4YjE9.JVbQnjFix2iU4CC8vwT5KrmNz33HeX4skYGCqDBCtC8IoXNrFvfRPRcFDXjva69ctrLb1UTGr.s30EuBYaoFEprXBAZP9bzeWRoliqFfk2axWus0qpFAj98_UmJC2D0f_gbsc.0RkkJpvBVTCZV3mCaB6hSrJYx9njfwXQuzl713LdSjVCcjPzrF27bq4ZB7MS6bKcqbOOw.imUyJTiZ5vMwOuXCm7u7LW83ibL',
    '_dd_s': 'rum=0&expire=1734415271891',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'authorization': '',
    'baggage': 'sentry-environment=production,sentry-release=30e3c08f,sentry-transaction=%2Fu%2F%5Busername%5D,sentry-public_key=2a051f9838e2450fbdd5a77eb62cc83c,sentry-trace_id=10aa13fa02d0433c85afc57f1aa2bc42,sentry-sample_rate=0.03',
    'content-type': 'application/json',
    'origin': 'https://leetcode.com',
    'priority': 'u=1, i',
    'random-uuid': '4f67e01a-78bd-623e-5643-7a8edf9d5e58',
    'referer': 'https://leetcode.com/u/niladridhar1/',
    'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Brave";v="131.0.0.0", "Chromium";v="131.0.0.0", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '10aa13fa02d0433c85afc57f1aa2bc42-80034f567e37b032-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-csrftoken': '898UDqmnGmITtIQyu4DFayTdkUorMgP1IcoJtOm7VdT5wNCxB1aR6CDay9bVosYY',
}

json_data = {
    'query': '\n    query userProfileUserQuestionProgressV2($userSlug: String!) {\n  userProfileUserQuestionProgressV2(userSlug: $userSlug) {\n    numAcceptedQuestions {\n      count\n      difficulty\n    }\n    numFailedQuestions {\n      count\n      difficulty\n    }\n    numUntouchedQuestions {\n      count\n      difficulty\n    }\n    userSessionBeatsPercentage {\n      difficulty\n      percentage\n    }\n    totalQuestionBeatsPercentage\n  }\n}\n    ',
    'variables': {
        'userSlug': 'niladridhar1',
    },
    'operationName': 'userProfileUserQuestionProgressV2',
}

response = requests.post('https://leetcode.com/graphql/', cookies=cookies, headers=headers, json=json_data)

easy_questions = re.findall(r'"count":(\d+),"difficulty":"EASY"',response.text)
medium_questions = re.findall(r'"count":(\d+),"difficulty":"MEDIUM"',response.text)
hard_questions = re.findall(r'"count":(\d+),"difficulty":"HARD"',response.text)

data = {
    "EASY_SOLVED" : int(easy_questions[0]),
    "MEDIUM_SOLVED" : int(medium_questions[0]),
    "HARD_SOLVED" : int(hard_questions[0]),
    "TOTAL_EASY" : int(easy_questions[0]) + int(easy_questions[-1]),
    "TOTAL_MEDIUM": int(medium_questions[0]) + int(medium_questions[-1]),
    "TOTAL_HARD" : int(hard_questions[0]) + int(hard_questions[-1])
}

with open("data.json","w") as f:
    json.dump(data,f)
f.close()
