# 함수
# 함수 정의 - 이건 실행이 아님
def add(x,y): #함수를 쓸 때 무조건 def를 쓴다
    result = x + y
    return result # 불렀던 곳으로 돌아간다

def sub(x,y):
    result = x - y
    return result

def mul(x,y):
    result = x * y
    return result

def div(x,y):
    result = x // y
    return result
    
# 함수 호출
val = add(1024,5) # add라는 함수를 만들어서 x에 1024 y에 5를 넣어라.
print(val)

val = sub(1024,1000)
print(val)

val = mul(512,2)
print(val)

val = div(108,10)
print(val)
