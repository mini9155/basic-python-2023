#파일 만들기

file = open('../sample06.txt', 'w', encoding = 'utf-8') #파일 쓰기로 만듦 , a 수정 , r 읽기

#file = open('./Day05/../Day04/sample06.txt', 'w', encoding = 'utf-8')

file.write('안녕하세요~ \n')
file.write('첫번째 파일이다!!!!!!\n')
file.write('절대경로에 파일이 생성 될 겁니다')

file.close()
print('sample.txt가 생성되었습니다')

# ASCII -> 한단어를 표현하는 체계(영어)
# (UTF-8) -> 모든 나라언어를 다 표현가능

#파일/폴더 경로
# /,\,\\ 절대
# .. 부모 .자신 - 상대(짧게 쓰기 위한)