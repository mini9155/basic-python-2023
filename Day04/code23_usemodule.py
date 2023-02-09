#모듈 사용
import math as m # math 를 m으로 바꿔준다
import code22_person_ as p
from code23_car import car  

print(m.pi)

print(m.tan(0))
print(m.ceil(3.8)) # 반올림
print(m.floor(3.5)) # 내림
print(2 **10) #거듭제곱
print(m.pow(2,10)) #거듭제곱

me = p.Person('홍길순',160, '여성') #생성하면 어디다 담아야지 > me
print(me)

#
mycar = car
print(mycar)