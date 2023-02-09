# 구구단 프로그램
for x in range(2,10):
    print(f'{x}단 시작') # x단 시작할 때 문자열 출력함
    for y  in range(1,10):
        print(f'{x} x {y} = {x*y:>2}',end=' ') # 한줄로 만들려면 end = '', :>2 2줄로 정렬
        # print(x, 'x',y, '=', x*y)
    print()