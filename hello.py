# 만약 배민에서 음식을 고를려고 하는데
# 선택하기 힘들어 메뉴를 추친 기능을 이용
# 치킨, 피자, 분식, 중식
# 무작위(랜덤)
import random
print(random.random())

menu = '치킨', '피자', '분식', '중식'
random.choice(menu)

import requests

r = requests.get('https://www.melon.com/')
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
r = requests.get("https://www.melon.com/",headers=header)
print(r) # 접속이 잘됐는지 확인

# html 정보 가지고오기
soup = BeautifulSoup(r.text, 'html.parser')
print(soup) #가져온 html 데이터 출력