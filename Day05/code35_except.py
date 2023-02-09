# 예외처리
def add(x,y):
    return x + y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

try:
    x, y = input('두 수를 입력하세요 >').split() #입력부터 입력실패하면 종료시켜야 함
    x = int(x)
    y = int(y)
except Exception as a:
    print(a)
    exit()
finally:
    print('계속되나요?') #무조건 나옴

# if y == 0:
#     print('y에 0을넣지마세요')
#     exit()
#가장 원시적인 예외처리

print('계산 테스트')

try:
    print(div(x,y))
# except ZeroDivisionError as a: # 메세지를 알려준다 e는 다른 단어로 변경되도 상관 없음
#     print('0으로 나누면 안되요!!') #exception 제일 마지막에 들어가야한다
except Exception as a:
    print(a)
finally:
    print('계산은 계속된다')

print(add(x,y))
print(mul(x,y))