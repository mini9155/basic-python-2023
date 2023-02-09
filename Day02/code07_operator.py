# 연산자
#할당연산 assigment
# 2 = 1 (x)
val = 1

# 1= val 변수는 무조건 왼쪽

# equal 연산자
print(1 == 1)

#사칙연산
print(1 + 1) # 2
print(1 - 1) # 0
print(10 + 10) # 20
print(1024 / 2) # 512.0
print(1024 // 2) # 512
print(1 / 3) # 실수 나누기 - 0.33
print(1 // 3) # 정수나누기 - 0
print(1 % 3) # 나머지 - 1
print(6 // 3) # 2
print(9 % 3) # 나머지 3>=0 6>=0 9>=0

# print( 6 / 0 ) ZeroDivisionError
# print( 6 // 0 ) ZeroDivisionError
# 0으로 나눌 수 없다, 무한대 계산 불가

print(2 ** 10) # 2의 10승

#문자열 연산

first = 'Hello'
second = 'world'
print(first + second )
print(first + ' ' + second)
print(first,second)
print(first * 3) # first 문자열은 3번 출력
print(len(first)) # 문자열의 길이 = 5
print(first[0]) # 문자열의 1번째 출력
print(first[1]) # 문자열의 2번쨰 출력
print(first[2]) # 문자열의 3번째 출력
print(first[3]) # 문자열의 4번쨰 출력
print(first[4]) # 문자열의 5번째 출력
# print(first[5]) 문자열의 6번째가 없어서 출력 x

print(first[-1]) #마이너스를 붙이면 거꾸로 인덱스를 찾아감
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 자르기(스플릿)
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4]) # 0번 부터 4번 배열까지 보여줌
print(current[5:7])
print(current[8:10])
print(current[14:16])
print(current[17:]) # 17번 부터 끝까지

print(current[0:4] + '년' + current[5:7] + '월' + current[8:10] + '시' + current[14:16] + '분' + current[17:] + '초' )

print(current[-19:-15]) #문자열 끝이 -1

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7 # que[0]에 7을 넣는다
print(que)

# que[5] = 10 열을 넘으면 변경이 안된다
que.append(10) # append 열이 너머도 추가가 된다
print(que)

que.insert(3,99) # 값을 원하는 위치에 추가
print(que)
tup = (1, 2, 3, 4, 5)

que.remove(10) # 해당값 삭제
print(que)

# tup[1] = 9 tup은 변경 불가 

#문자열 == 문자 리스트
title = 'python'
print('P' + title[1:]) # P를 출력 + 1번부터 출력 

# title[0]  = 'P' 문자열에서는 값 변경 x
print(title[0])

#일반적인 문자형 리스트
text = ['p','y','t','h','o','n']
print(text)
text[0] = 'P'
print(text)

#문자열 포맷팅
print("I'm so happy {0} you {1} !!".format( 2, 'hey')) #코드 블록 , 숫자 순서대로 - format()안에 순서대로

#최신식 문자열 포맷팅
preword = 2
sayHello = 'hey'
print(f"Im so happy {preword} you, {sayHello}!!") # 필요할 떄 값을 입력받아서 대입, 예시로 사이트에 회원가입 후 이름 띄울 때

pi = 3.141592
print(f'파이는 {pi}입니다')
print(f'파이는 {pi:0.2f}입니다') # 0.02f 소수점 2번째 자리까지 출력
print(f'파이는 {pi:10.3f}입니다') # 10.3f 10번 띄우고 소수점 3번쨰 자리까지 출력

#문자열을 특정문자로 자르기
full_name = 'seung_ min'
vals = full_name.split( )
print(type(vals))
print(vals)

vals  = full_name.split('_') # 언더바가 있는 곳을 잘라라
print(vals)
#age =  25
#print(f"Hello I'm {full_name}, and I'm {age:2.0f} ages.")

print(full_name.replace('seung','min')) # replace() 안에 1,2번째를 바꾼다.

#문자열 공백 없애기
hi = '          Hello~ Bye~          '
print(hi.lstrip() + '|') # 오른쪽 공백 없애라
print(hi.rstrip() + '|') # 왼쪽 공백 없애라
print(hi.strip() + '|') # 양쪽 공백 없애라

print(full_name.index('m'))
#print(full_name.index('G')) 찾는 게 없으면 오류 뜸
 
print(full_name.find('m')) # 
print(full_name.find('G')) # 찾는 게 없으면 -1

#찾는 단어의 갯수
print(full_name.count('n'))

#모든 단어를 대문자/소문자로 변경
print(full_name.upper()) # upper 대문자
print(full_name.lower()) # lower 소문자


# 연산자 우선순위
print(3 + 4 * 2)
print( (3 + 4) * 2 ) # ()를 쓰면 연산자 우선순위를 가진다