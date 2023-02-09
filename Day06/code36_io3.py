# 콘솔출력 보충
# 이스케이프 캐릭터(탈출 문자)
print('1.Hello.\r\n world')
print('2.Hello.\n world') # 3,4번 줄 차이가 없다. \n을 쓰는 게 나음

print('3.Hello.\n\tworld') # t는 tab
print('4.Hello.\n\t\bworld') # \b 백스페이스

print('5.Hello.\n\'world\'') # \' 문자열 내 홑따옴
print('6.Hello. "world"')
print('7.Hello. \"world\"')

print('7.Hello. \\ world') # 파이썬만 가능 \를 문자열에 표현
print('8.Hello\00') # \00 은 문자가 끝났다고 알려주는데 다른 언어에는 필요함

# 문자열 포맷팅 - 구닥다리
# %로 포맷코드를 시작

me = '저'
name = '한승민'
age = 20
print('%s는 %s입니다. %d대 입니다.'% (me,name,age))

print(f'{254.112233:.2f}') # .2f 소수점 2번쨰 자리에서 자름
print('%4.4f'%(254.112233)) # 구식버전 소수점  4번째 자리에서 자름