#복합형

#리스트 안 쓰면
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10
print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)

#리스트 == 배열
#리스트는 값을 추가,수정,변경 가능
# a = [ 1,2,3,4,5,6,7,8,9,10 ]
arr = [ 1,2,3,4,5,6,7,8,9,10 ]
print(arr)
sum = 0
for i in arr:
    sum += i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello',13,'world', True]
print(arr3)
print(type(arr3))
#print('arr1의 2번 인덱스값' + str(arr1[3]))

arr4 = [] #빈 리스트
arr5 = list() #빈 리스트 - 32,33 똑같다
print(arr4)
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]] # 리스트 안에 리스트를 넣을 수 있다 - 3차원 배열
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]] # 2차원 배열
print(arr7)

#튜플

tuple1 = (1,2,3,4)
print(tuple1)

arr5.append('4')
print(arr5)

#  tuple1.append(4) tuple은 한 번 만들면 값을 추가,변경,수정 불가능
print(tuple1)
print(type(tuple1)) # 클래스 tuple

#딕셔너리

spiderman = { 'name' : 'peter parker',
               'age' : '18',
            'weapon' : 'web shooter',
            'desert' : '탈영병' }
print(spiderman)

# 결과값 : {'name': 'peter parker', 'age': '18', 'weapon': 'web shooter','desert' : '탈영병'}

print(spiderman['weapon'])
print(spiderman['desert'])
print(type(spiderman)) # 딕셔너리 타입 - dict

#집합
set1 = set([1,2,3,4])
print(set1)

# 결과값 : {1, 2, 3, 4}

set1 = set("Hello World")
print(set1)