# study-python2023
부경대 IoT 파이썬 학습 리포지토리

# 중요
 - 오류 시 터미널 잘 확인하기
 - 주석 잘 달자

## 1일차
1. 기본구성
    - 개발환경 구성
    - Git/Github 설치 및 연동
    - Visual stdio code 설치 및 연동
    - python 설치
2. Python 기본
    - 콘솔출력
    - 변수

```python
# date : 2023-01-30
# author : mini9155
# 콘솔출력 / 여기는 주석입니다!

print('Hello, Python!!') #콘솔출력 함수
```

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자
    - 흐름제어

```python
#변수
val = 1

#자료형
print(type(val)) #<class 'int'>

#문자열 포맷팅
pi = 3.141592
print(f'파이는 {pi}입니다') # 파이는 3.141592입니다
print(f'파이는 {pi:0.2f}입니다') # 파이는 3.14입니다
print(f'파이는 {pi:10.3f}입니다') # 파이는           3.141입니다
```

# 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 구구단 프로그램
    - 함수

# 4일차
1. 파이썬 기본
    - 가상환경
    - 객체지향 OOP
        - 객체는 동사와 명사의 집합(ex.심즈 - 현실의 모든 것들을 안으로 집어넣음)
        - 객체를 넣을려고 준비한 툴이 클래스
        - 절차지향 <-> 객체지향
    - 패키지(라이브러리),모듈
        - 모듈은 레고( 부품 하나하나가 모듈로 이해하면 쉬움)
        - 모듈은 import를 이용해서 부를 수 있다

# 5일차
1. 파이썬 기본
-패키지 계속
-입출력 다시
-예외처리
-객체지향 다시

# 6일차
1. 파이썬 기본
    - 콘솔 출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중 상속

2. 파이썬 응용
    - 주소록 프로그램 [소스](https://github.com/mini9155/study-python2023/blob/main/project/addrres_app.py)
![실행화면](https://raw.githubusercontent.com/mini9155/study-python2023/main/Images/address_app.png)
실행화면

# 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법(파일메뉴에서 열어야함)
    - 노트북 생생 : 파일메뉴>새파일
    - 리스트 연산 추가
    - 라이브러리 사용법
        - folium(지도 라이브러리)
# 8일차
1. 파이썬 응용
    - 라이브러리 사용법
    - 웹크롤링 사용법
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAPI 크롤링
        - beautifulsoup 크롤링

![실행화면](https://raw.githubusercontent.com/mini9155/study-python2023/main/jupyter_folium.png)

 # 9일차

 1. 파이썬 개발
    - GUI개발(PyQt)
        - Tkinter 소개
        - PyQt 소개 및 사용
        - PyQt 기본 사용법
        - 위젯

# 10일차
1. 파이썬 응용
    -  GUI 개발
        - PyQt 위젯 계속
