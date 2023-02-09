# for문

arr = [1,2,3,4,5]
sum = 0

for item in arr: #arr 가 item 안으로 5까지 반복 후 나감
    print(item)
    sum += item # sum = sum + item

print('합계는',sum)

# 홀짝
# 리스트를 편하게 만드는 방법
vals = [i for i in range(1,11)]
print(vals)

num = 0
for item in vals:
    num += 1
    if num%2 == 0:
        continue #이후의 것을 수행하지 않고 그대로 올라가
    else:
        print(num, '번수는',item,'입니다')