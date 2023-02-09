#좀 더 복잡한 계산기

def calc(option, *args):    #*args 가변인자 - *뒤에 함수는 바뀌어도 상관없다. 
                            #함수의 갯수가 몇개인지 모를 때 사용
    result = 0
    if option == 'add':
        for i in args:
            result += i
    elif option == 'mul':
        result = 1
        for i in args:
            result *= i
    elif option == 'sub':
        result = args[0]
        for i in args[1:]:
            result -= i
    elif option == 'div':
        result = args[0]
        for i in args[1:]:
            result /= i

    return result

print(calc('add', 5, 7, 17))
print(calc('mul',512,2,2,2,2,2,2,2,2))
print(calc('sub',10,248,396))
print(calc('div',100,5))

 # 여러값을 리턴할 때는 튜플을 사용
def mul_and_div_and_add_and_sub(x,y):
    return (x*y, x/y, x + y, x - y)

# 받을 때는 튜플(소괄호) 생략 가능
#(res1, res2, res3,res4) = mul_and_div_and_add_and_sub(5,7)
res1, res2, res3,res4 = mul_and_div_and_add_and_sub(5,7)
print(res1, res2, res3, res4)