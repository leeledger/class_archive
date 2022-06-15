import turtle
import time
import random

s = turtle.Screen()
write = turtle.Turtle()
write.hideturtle()

rand_numbers = [i for i in range(1,101)]

nums = int(s.textinput("입력", "생성할 숫자의 갯수 입력?"))
com_nums = []
while True:
    num = random.choice(rand_numbers)
    print("test")
    if num not in com_nums:
        com_nums.append(num)
    else:
        continue
    if nums == len(com_nums):
        break
for num in com_nums:
    write.clear()
    write.write(num,False,"center",font=("",100,"bold") )
    time.sleep(1)
write.clear()
print(com_nums)
user_nums = s.textinput("입력","숫자를 입력하세요 ' , '로 구분")
# user_nums = [int(num) for num in user_nums ]
user_nums = user_nums.split(",")
user_nums = [int(num) for num in user_nums]

if user_nums == com_nums:
    write.write("정답",False,"center",font=("",100,"bold"))
else:
    write.write("노답", False, "center", font=("", 100, "bold"))
s.mainloop()