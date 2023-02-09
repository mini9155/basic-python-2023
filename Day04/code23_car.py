

# 자동차 클래스 만들기
class car:
    __number = '54라 9538'

    def get_number(self):
        return self.__number

    #클래스 외부에선 변경 x, 멤버함수로는 내부조작 가능
    def set_number(self, number):
        self.__number = number

    def __init__(self,number ='54라 9538') -> None:
        self.__number = number
        print('__init__')

    # def __new__(cls):  # super라는 클래스 생성
    #     print('__new__')
    #     return super().__new__(cls) 부모클래스 (상속)
        #new는 생성자
        #init은 초기화해서 새로운 변수를 할당하려고 할 때
        #부모 클래스를 생성해서 new를 실행해라
    def __str__(self) -> str:
        return f'차번호는 {self.__number}'

yourcar = car(number='88호 7645')
print(yourcar)
yourcar.__number = '54라9999' #외부에서는 멤버변수에 접근 불가
print(yourcar)
print('내부함수 사용')
yourcar.set_number('55오5555')
print(yourcar)

mycar = car()
print(mycar.get_number())
print(f'제차는 요, 아이오닉이고, 번호가 {mycar.get_number()}에요')

mycar.__number = '132거8874'
print(mycar.__number)