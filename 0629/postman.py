# -*- coding: utf-8 -*-
# @Time : 2020/7/1 10:43 上午
# @Author : zhl
# @File : postman.py
# @Software: PyCharm


import requests

url = "http://api.lemonban.com/futureloan/member/recharge"

payload = "{\"member_id\":\"200941\",\t\"amount\":\"500001\"}"
headers = {
    'X-Lemonban-Media-Type': "lemonban.v2",
    'Authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwMDk0MSwiZXhwIjoxNTkzNDI3OTI1fQ.Xgqhi2V7XD-TsLy-8i1uqyTJAsBiQ8ZJREsMEydQpDlNmmtOdtiYonyyFv26SWFoV2oPz8bGw5iKTSFjMgi8Ow",
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "fbbfbb87-1b86-456d-ba23-6daebd50d06c,68ff7dad-b178-4ff0-8c3c-c866754bdf83",
    'Host': "api.lemonban.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "41",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)