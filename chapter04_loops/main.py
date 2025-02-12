'''
while 반복문
    while 다음에 나오는 조건문이 참이라면 이하의 실행문이 반복 실행됨. (조건문이 False가 될 때까지)

형식:
while 조건문:
    실행문
'''
#무한 루프의 개념
# num1 = 1
# while num1 > 0:
#     print(num1)

'''
그래서 while 반복문을 작성할 때 고려할 점:
    특정한 상황에서 조건식이 False가 될 수 있도록 사전에 미리 지정해줘야함.
        아닐 경우 무한 루프에 빠짐
'''
# 특정 조건에서 반복문이 종료될 수 있도록 하는 예시
# num2 = 1
# while num2 < 11:
#     print(num2)
#     num2 += 1 # 특정 조건하에서 조건문이 False가 될 수 있도록 하는 부분
#
# print(f"최종 num2는 = {num2}") #

'''
if문과 비교할 때
    if문의 경우 조건식이 참일 때 실행문이 한 번 실행되지만
    while의 경우 조건식이 참일 때 실행문이 반복 실행
    특정 조건이 맞을 경우와 아닐 경우에 대한 고민이 필요한 편

기본 예제
10부터 1까지의 모든 정수를 역순을 실행
'''

# num3 = 10
# while num3 > 0:
#     print(num3)
#     num3 -= 1
#
# num3 = 11
# while num3 > 1:
#     num3 -= 1
#     print(num3)

'''
중첩 while문(Nasted while-loops)
 : while문 내부에 while문이 나타나는 것
 
ex) 총 5일 간 매일 3시간씩 수업 진행. 매일 '1일차 1교시입니다.'와 같은 메시지를 출력
1일차부터 5일까지 반복되는 일수와 1교시부터 3교시까지 반복되는 시간이라는 2개의 반복 처리 대상을 기준으로 중첩 while문 작성
'''

# day = 1
# while day < 6: #5일차까지만 출력되고 탈출해야함
#     hour = 1
#     while hour < 4: #3교시까지만 출력되고 탈출해야함
#         print(f"{day}일차 {hour}교시입니다.")
#         hour += 1
#     day += 1 #이 부분 들여쓰기 실수 많음

'''
구구단 2단부터 9단까지 출력하는 프로그램 작성 (while문 사용)
변수명은 dan / number
'''

# dan = 2
# while dan < 10: #값이 있으면 True로 취급
#     number = 1
#     while number < 10:
#         print(f"{dan}x{number} = {dan*number}")
#         number += 1
#     dan += 1

# n = 1
# while n < 101:
#     print(f"{n} {n+1} {n+2} {n+3} {n+4} {n+5} {n+6} {n+7} {n+8} {n+9}")
#     n += 10


#이상의 코드의 경우에는 반복을 10번 돌리는 경우였습니다.
#모든 편견을 가지고 코드를 억지로 작성하게 되면 100번을 반복하면
# n2 = 1
# while n2 < 101:
#     print(n2, end=" ")
#     if n2 % 10 == 0:
#     n2 += 1