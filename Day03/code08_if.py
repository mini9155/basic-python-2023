#if문을 배워요

#name = input('성함이 어떻게 되시나요?') # - 변수  = input() 
#state = input('몸이 아프신가요?')
name = '승민'
state = '아픔'

if name == '승민':
    print('진료실에서 담당의사를 만납니다')
    if state == '아픔':
        print('선생님, 배가 아파요~')
        print('배 어디가 어떻게 아프십니까?')
    else:
        print('어디가 아프십니까?')
        print('안아픈데요')
        print('그럼 왜 오셨어요?')

elif name == '다원':
    print('주사실로 갑니다.')
    print('엉덩이 내리세요.')
else:
    print('조용히 기다립니다.')