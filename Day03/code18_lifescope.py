# 라이프스코트
a = 1

#더블클릭 후 f2 누르면 전체 이름 변경

def vartest(x):
    global a # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다.
    a = a + x + 1
    return a

a = vartest(a)
print(a)