# 공공데이터포탈 csv파일 읽기
#부산광역시 시내버스,마을버스 현황

import csv

fileName ='busanbus.csv'
dirName = 'C:/source/study-python2023/' #마지막에 구분자 적어주는 게 좋다
fullpath = dirName + fileName

file = open(fullpath,'r',encoding= 'utf-8')
reader = csv.reader(file,delimiter=',')
next(reader)

for Line in reader:
    print(Line)

file.close()