#객체지향 클래스
#클래스 안에 변수를 속성변수
#맴버함수 ,self(오브젝트가 씀,지칭해줘야함)
class Person: # 함수 이름
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    #초기화 추가
    # def __init__(self): # __ > 매직메서드, init 초기화
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'
    
    def __init__(self, name, height, gender) -> None: #살짝 흐리면 아직 사용x, 불러줘야함
        self.name = name

        self.height = height
        self.gender = gender

    def walk(self):
        print('걷습니다')
    
    def run(self,option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이 빨리 뜁니다!!')
        else:
            print(f'{self.name}이 천천히 뜁니다!!')

    def stop(self):
        print(f'{self.name}이 멈춥니다')

#2.생성자외 매적메서드(평션) __ str__
    def __str__(self) -> str:
         return f'출력:이름은 {self.name}, 성별은 {self.gender} 입니다.'

min = Person('한승민',185,'A' ) # 객체생성, instance, 함수처럼 호출
min.name = '한승민' #파란색 박스 속성함수, 보라색박스 함수 , 언더바 있는 함수는 파이썬이 만든 함수
min.height = '185'
min.gender = 'male'
min.blood_type = 'RH+ A'

print(f'{min.name}의 혈액형은 {min.blood_type} 입니다')

min.run('Fast')
print('한승민')

hong = Person('홍길동',170,'AB')

hong.run('Slow')

print('======================================')

#2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리',165,'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)