# 외부패키지
import requests

res = requests.get('https://www.naver.com')
print(res.status_code)
print('=============')
print(res.content)