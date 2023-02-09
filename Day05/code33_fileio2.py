#파일 읽어오기

file = open('./Day05/sample01.txt','r',encoding='utf-8')

#text = file.read() #readline 한줄씩
#print(text)

while True:
    text = file.read()

    if not text:break

    print(text)
file.close() #파일을 열면 무조건 닫아줘야한다