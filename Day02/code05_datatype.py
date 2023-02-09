# 자료형
# python, java, c++ 객채지향언어
# None 값이 없는 값
None # 컴퓨터 왈 "난 몰랑"

print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3
print(type(val)) # 정수형

val = 3.14
print(type(val)) # 실수형

val = 'hello'
print(type(val)) # 문자형

val = 0b1010
print(type(val)) 
#계산기에서 bin 2진수

val = 12.45354635435353464324235362423423523654
print(type(val))

val = 4_520_000 # 언더바 읽기 쉽도록 해줌 - 천단위마다
print(val)

# 문자열
val = 'Life is short, you need python'
print(val)
print(type(val))

val = 'Hell\nworld' # \n 탈출문자
print(val)
val = 'Hell\tworld' # \t 네 칸 띄워준다
print(val)
val = 'Hell\t\bworld' # \b 한 칸 줄여준다
print(val)

#문자열을 띄어서 쓰고 싶을떄 '''개를 쓴다
val = '''life is short,
you need python'''
print(val)

val = "Hi, I'm 'hugo'" #문자안에 ' 들어갈 경수 ""를 쓰면 된다
print(val)

val = 'Hi, I\'m \'hugo\''
print(val)

# 불린형 or 불형
참 =  True
거짓 = False
print(type(거짓))

print( 1 + 1 == 2)
# 거짓이라는 False 값 변수가 참이냐?
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(3)) # 1 이외의 값은 True라고 하지마세요