number = [1,2,1,3,1,4,1,5]
number.remove(number[1])
number[1]="sky"
number[3]="star"
print(number)

num = [1,2,3]
num.extend([4,"k",8])
num[1] = 5
print(num)
loc1 = num.index(1)
print(loc1)


number.pop()
print(number)

number.pop(1)
print(number)

dir(list)