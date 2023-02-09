# #다중입력
# x, y = input('두 영단어를 입력하세요 > ').split(',')

# print(x)
# print(y)

#완전 다중입력(개수가 몇개던지 상관 없음)

inputs = list(map(str, input('단어를 입력하세요(개수 상관X) >>').split())) #map은 들어오는 함수를 나열해줌(멀로 나열할지 지정해줘야함)

print(inputs)

inputs = list(map(int, input('정수를 입력하세요(개수 상관X) >>').split())) #map은 들어오는 함수를 나열해줌(멀로 나열할지 지정해줘야함)

print(inputs)

#r,w,a 