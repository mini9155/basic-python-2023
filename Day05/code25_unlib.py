# urllib 불러오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')
res = urlopen(req)
print(res.status) #200은 https 값을 제대로 받았다는 뜻