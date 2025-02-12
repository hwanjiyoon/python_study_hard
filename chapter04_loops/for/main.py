'''
for 반복문 개념
정해진 구간 혹은 집합 내의 요소들을 순서대로 꺼내면서 반복 작업을 수행.
예를 들어 아까 전에 문자열의 index 개념을 학습했음.

1)숫자 범위를 이용한 반복
range() : 몇 번 반복할 것인가를 지정하는 함수
'''

#1부터 10까지 출력하는 while 반복문
#for 반복문

#1부터 10가지 반복되는 for 반복문
# for i in range(11): #현재 상황에서의 반복 횟수는 11회
#     print(i)

# for i in range(10):
#     print(i+1)

'''
range()함수의 응용:
    range((시작값), 종료값, (증감값))
    
    시작값 : 생략 가능, 생략할 경우 0부터 시작
    종료값 : 명시하지 않으면 끝까지 진행
    증감값 : 생략 가능, 생략할 경우에 1씩 진행
    
for 반복문
형식:
for i(아무거나 사용가능) in range(시작값, 종료값, 증감값):
'''

# for i in range(1, 10, 1):
#     print(i)

'''
문자열을 이용한 반복
문자열의 경우[]를 통해 내부에 인덱스 넘버를 명시할 수 있다는 것을 확인
그래서 in range()를 사용하는 방법 및 향상된 for문을 사용하는 방법을 통해
문자를 하나씩 추출 가능
'''
#len()(length) : ()안에 들어가는 요소의 길이를 변환하는 함수
#enhanced for loop를 통한 방식
# name = jihwan
# for letter in name: #name이라는 string에서 각 문자 하나씩을 뽑아 letter에 대입
#     print(letter)
# #
# # #첫 번재 반복의 경우
# letter = name[0]
# print(letter)

'''
대부분의 경우 반복문을 사용하게 되면 반복 대상이 되는 객체는 복수형의 변수명을 지닙니다.
ex) numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
    
향상된 for loop의 형식:
for 변수 in 반복대상객체:
    반복실행문
    
반복대상객체(iterable) : 내부에 요소가 다수 들어가 있어 반복적으로 요소의 데이터를 다룰 수 있는 객체
ex) str, list, tuple, set, dict > 현재 저희는 str만 기준으로 수업중

주의사항:
if 조건문과 마찬가지로 들여쓰기가 중요함

문자열에서 특정 문자의 개수 세기
'''
#
# count_a = 0
# count_letters = 0
# for letter in "banana"
#     if letter == "a":
#         count_a += 1
#     print(letter)
#     count_letters += 1
# print(f"a의 개수 : {count_a}")
# print(f"전체 문자 개수 : {count_letters}")
# print(f"전체 문자 개수 : {len("banana")})

'''
reeborg's world hurdle
#1-1
for _ in range(6):
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
#1-2    
n=0
while n < 6:
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    n += 1
#1-3
def turn_right():
    for _ in range(3):
        turn_left()

for _ in range(6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
#1-4
    def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for _ in range(6):    
    jump()
    
    
    
    
    
#2    
    def turn_right():
    for _ in range(3):
        turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
    
    
    
    
    
#3     
    def turn_right():
    for _ in range(3):
        turn_left()

def jump(): #def : 정의
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
        
        
        
        
        
#4        
        def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not right_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
        
        
        
        
        
#미로찾기
def turn_right():
    for _ in range(3):
        turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and wall_in_front():]
        turn_left()
    elif front_is_clear():
        turn_right()
        move()

 
'''











