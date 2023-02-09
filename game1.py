print('게임을 시작하지')
print('이 게임은 숫자 맞추기 게임이네')
print('숫자는 랜덤으로 정해지네')

from random import randrange

c = 0
b = randrange(1,100)


while  c < 5:
    c += 1
    a = input('정답을 맞춰보시게. 기회는 5번일세:>>')
    a = int(a)

    if a == b:
        print('당신이 이겼습니다')
        break

    elif a > b:
        print('언더')
    
    elif a < b:
        print('오버')

print(f'정답은 {b} 입니다')