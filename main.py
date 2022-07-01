#
#
import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()


t.setheading(270)
t.up()
t.setposition(-200,200)
t.pendown()
lines = 9

s.delay(0)
for i in range(lines):
    t.forward(400)
    t.up()
    t.setposition(t.xcor()+50,200)
    t.pendown()
t.up()
t.setposition(-200,200)
t.down()
t.setheading(0)
t.hideturtle()
vertical_line = [xcor for xcor in range(-200,181,50)]
horizontal_line = [ycor for ycor in range(-180,181,20)]

tried = []
for j in range(10):
    for i in range(-200,181,50):
        x = random.choice(vertical_line)
        y = random.choice(horizontal_line)
        tried.append([i,y])
        # if len(tried) > 1:
        #     if tried[i][0] == tried[i-1][0]:
        #         print("test")
        t.up()
        t.setx(i)
        t.sety(y)
        t.down()
        t.forward(50)

count = 0
exist = []
for j in range(len(tried)):
    for i in range(j):
        if tried[i][1] == tried[j][1] and abs(tried[i][0] - tried[j][0]) == 50:
            # print(tried[i][0], tried[i][1], tried[j][0], tried[j][1])
            exist.append([tried[i][0], tried[i][1]])
            count += 1
# print(count)

# 중복제거
t.pensize(2)
t.color("white")
print(len(tried))
# print(exist)
for i in range(len(exist)):
    t.penup()
    t.setposition(exist[i][0]+1,exist[i][1])
    t.pendown()
    t.forward(48)
    try:
        del tried[tried.index([exist[i][0],exist[i][1]])]
    except:
        pass
    # print("test")
# print(len(tried))


player = turtle.Turtle()
player.shape("turtle")
player.shapesize(2)
player.setheading(270)
player.color("red")
player.up()
player.setposition(-200,200)
s.delay(1)

print(len(tried))

while True:
    player.forward(1)
    # print([int(player.ycor()),int(player.xcor())])
    if [int(player.ycor()),int(player.xcor())] in tried:
        print("test")
        if player.heading() == 0:
            player.setheading(270)
        else:
            player.setheading(0)


# s.mainloop()

#
# import requests
#
#
# url = "https://maker.ifttt.com/trigger/codeis/with/key/dm-dDRa9RDITIh86iS889p"
# data = {'value1': '홍길동', 'value2': '가나다', 'value3': 'ㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇ'}
# re = requests.post(url,data = data)
#


# https://infinitt.tistory.com/