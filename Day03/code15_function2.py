# 함수
# 함수 정의 - 이건 실행이 아님
##함수 만드는 방법 4가지
 #1. 파라미터0 리턴0
 #2. 파라미터0 리턴x
 #3. 파라미터x 리턴x
 #4. 파라미터x 리턴x
def add(x,y): #함수를 쓸 때 무조건 def를 쓴다
    result = x + y
    print(result)
    return # return이 생략됨

def sub(x,y):
    result = x - y
    print(result)
    
def mul(x,y):
    result = x * y
    print(result)
    
def div(x,y):
    result = x // y
    print(result)
    
def hello():
    print('Hello~!!!')
    

def hello2():
    msg = 'Hello, Hello'
    return msg


# 함수 호출
hello()
print(hello2())
add(1024,5) # add라는 함수를 만들어서 x에 1024 y에 5를 넣어라.
sub(1024,1000)
mul(512,2)
div(108,10)
