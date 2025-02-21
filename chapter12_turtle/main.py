import random
'''
chapter12_turtle
main
'''
# turtle이라는 모듈을 사용할건데, Turtle, Screen 클래스를 import 할겁니다
from turtle import Turtle, Screen

t = Turtle()        # Turtle 클래스의 객체 생성, 이름은 t
screen = Screen()   # Screen 클래스의 객체 생성
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
# t.penup()
# t.forward(100)
# t.pendown()
# t.forward(200)


# for _ in range(10):   # 그냥 반복을 10번 하는 거고 변수를 사용하지 않았기 때문에 _를 썼습니다(i나 n이 아니라)
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     t.forward(10)

# t.left(90)
# t.forward(100)

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# for _ in range(4):
#     t.forward(100)
#     t.left(90)
#
# for _ in range(3):
#     t.forward(100)
#     t.left(120)

# n=3
# for _ in range(n):
#     t.forward(100)
#     t.left(180-((n-2)*180)/n)
def dotted_line():
    for _ in range(10):
        t.penup()
        t.forward(5)
        t.pendown()
        t.forward(5)

def draw_dotted_figures(num):
    for _ in range(num):
        dotted_line()
        t.left(360/num)

random = random.Random()

colors = ["royal blue",
          "forest green",
          "firebrick",
          "green yellow",
          "plum",
          "dark magenta",
          "salmon",
          "light sea green",
          "moccasin",
          "coral",
          "tan",
          "deep sky blue",
          "light yellow",
          "dark slate gray",
          "slate gray"
          ]

t.speed(10)

def draw_figures(num):
    t.color(random.choice(colors))
    if num < 3:
        print("도형을 그릴 수 없습니다.")
        return
    for i in range(3, 11, 1):
        t.forward(100)
        t.left(180-((num-2)*180)/num)


# draw_figures(3)
# draw_figures(4)
# draw_figures(1)




'''
heading() 메서드:
거북이가 바라보는 방향을 나타내는 속성으로 각도 단위로 나타남

해당 메서드는 콘솔창에 float 형태로 출력
0도 : 동
90도 : 북
180도 : 서
270도 : 남

setheading()메서드 :
특정 각도로 거북이를 회전시키는 메서드

circle() 메서드:
거북이가 원을 그리는 메서드
'''

# t.forward(100)
# print(t.heading())
# t.right(90)
# print(t.heading())

# for _ in range(10):
#     t.circle(100)


# num = 30
# for _ in range(360 // num):
#     t.circle(100)
#     t.color(random.choice(colors))
#     t.setheading(t.heading()+num)

#draw_spidergraph(size_of_gap)로 함수화 하시오.

def draw_spidergraph(size_of_gap):
    for _ in range(360 // size_of_gap):
        t.circle(100)
        t.color(random.choice(colors))
        t.setheading(t.heading()+size_of_gap)

t.speed(0)
draw_spidergraph(2)

screen.exitonclick()