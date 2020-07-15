# -*- coding: utf-8 -*-
# @Time : 2020/7/1 10:48 上午
# @Author : zhl
# @File : lesson_requests.py
# @Software: PyCharm

import requests
url = "http://api.lemonban.com/futureloan/member/recharge"
data={"member_id":"200941",	"amount":"500001"}
headers={"X-Lemonban-Media-Type":"lemonban.v2"}

resp = requests.post(url,json=data,headers=headers)
print(resp.status_code)

print(resp.headers)

print(resp.text)