# while
hit = 0

while hit < 10: # hit이 11보다 작으면
    hit += 1 # hit에 1을 더해라

    print('나무를 {hit}번 찍었습니다')
    if hit == 10: # 만약 hit이 10이면 '나무가 넘어갔습니다'를 출력
        print('나무가 넘어갔습니다!!')  
        break # while문에서 탈출
    else: # 만약 hit이 10이 아니면 '나무가 아직 넘어가지 않았습니다. 끈질긴 놈'를 출력
        print('나무가 아직 넘어가지 않았습니다. 끈질긴 놈') 

print('나무찍기 완료') # while문 탈출 후 '나무찍기 완료' 출력