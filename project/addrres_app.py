# 주소록 프로그램
# 2023 - 02 - 06
# smg
import os #운영체제용 모듈
#15. 예외처리
# 15-1 파일 없을 떄 나는 예외
# 15-2 입력시 / 개수가 다를 때 예외
# 15-3 메뉴번호 입력 숫자외 예외

# 2. 클래스 생성
class Contact: #class 내 함수 self를 쓴다
    # 생성자 - 이름, 전번, 이메일, 주소
    def __init__(self, name, ph_num, email, addr) -> None:
        self.__name = name
        self.__ph_num = ph_num
        self.__email = email
        self.__addr = addr

    #4 __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름 : {self.__name}\n'
                   f'핸드폰 : {self.__ph_num}\n'
                   f'이메일 : {self.__email}\n'
                   f'주 소  : {self.__addr}\n')
        return str_res

    #10. 객체 존재여부 확인
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False
    # 12. 각 멤버변수 접근하는 함수
    #getName,,getPhnum
    def getName(self):
        return self.__name
    
    def getph_num(self):
        return self.__ph_num
    
    def getemail(self):
        return self.__email
    
    def getaddr(self):
        return self.__addr        


# 5. 사용자입력
def set_contact():
    name,  ph_num, email, addr = input('정보입력''(이름/폰번호/이메일/주소)').split('/')
    #    print(name, ph_num, email, addr)
    
    # 7. contact 객체 만들기
    contact = Contact(name, ph_num, email, addr)
    return contact
    
#9.주소록 출력

def get_contacts(list):
    for item in list:
        print(item) # str이 출력됨
        print('=====================')

#10. 주소록 삭제
def del_contact(list, name):
    count = 0
    for i, item in enumerate(list): # 앞에 i를 붙이면 순서를 정해서 출력 가능
        if item.isNameExist(name):
            count += 1
            del list[i] #리스트 삭제
    if count > 0:
        print('삭제했습니다!')
    else:
        print('삭제할 주소록이 없습니다.')


# 13. 주소록 파일 저장
def save_contacts(list):  #파일을 저장해주는 함수 save
    file = open('C:/source/study-python2023/project/contacts.txt','w', encoding='utf-8') # 파일경로,쓰기,인코딩
    
    for item in list:
        text = f'{item.getName()}/{item.getph_num()}/{item.getemail()}/{item.getaddr()}'
        file.write(f'{text}\n')

    file.close() #파일 닫아줘야 함!

#14. 주소록 읽어오기
def load_contacts(list):
    try:
        file = open('C:/source/study-python2023/project/contacts.txt','r', encoding='utf-8')
    except Exception as e: #15-1 예외처리
        f = open('C:/source/study-python2023/project/contacts.txt','w', encoding='utf-8')
        f.close() #파일이 없어서 생기는 예외는 파일 생성하고 함수 아웃
        return

    while True:
        line = file.readline().replace('\n','') #15. 문장끝 \n 제거
        if not line:
            break

        lines = line.split('/') #라인을 자르면 그 문자열은 리스트
        contact = Contact(lines[0],lines[1],lines[2],lines[3]) #
        list.append(contact)
#추가. 화면클리어
def clear_console():
    command = 'clear' #리눅스, 유닉스 클리어
    if os.name in('nt','dos'): # 윈도우 운영체제라면 
        command = 'cls'

    os.system(command)

#6.메뉴 표시
def get_menu():
    str_menu = ('주소록앱 v0.5\n'''
                '1.연락처 추가\n'
                '2.연락처 출력\n'
                '3.연락처 삭제\n'
                '4.앱종류')
    print(str_menu)
    try:
        menu = int(input('메뉴입력 : '))
    except Exception as e: # 15- 3 숫자외 입력예외 처리
        menu = 0 #영문자, 특수문자 넣으면 전부
    return menu

#전체 실행
def run():
    contacts = list() # 주소를 담기위한 빈리스트 생성
    load_contacts(contacts) #14. 주소록 읽어오기
#    temp = Contact('한승민', '010-6436-9628', 'hanbv@naver.com', '부산시 수영구')
#    print(temp)
#    set_contact()

    clear_console()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1: #연락처 추가
            try:
                contact = set_contact()
                contacts.append(contact)
            except Exception as e:
                print('이름/전번/이메일/주소순으로 정확하게 입력해주세요!!')
                input()
            clear_console()
            Contact = set_contact()
            contacts.append(Contact)
            input('주소록 입력 성공!') # 아무것도 안받는 입력
            clear_console()
            
        elif sel_menu == 2: # 9.연락처 출력
            get_contacts(contacts)
            input('주소록 출력 완료!')
            clear_console()

        elif sel_menu == 3:
            name = input('삭제할 이름을 선택 : ')
            del_contact(contacts, name)
            input()
            clear_console

        elif sel_menu == 4: #13.종료시 주소록 파일 저장
            save_contacts(contacts) # contacts 파일을 종료시 저장해줌
            break
        else:
            clear_console()

#1. 메인 실행 영역
if __name__ == '__main__':
    run()