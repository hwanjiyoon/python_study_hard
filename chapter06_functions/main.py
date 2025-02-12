'''
function : 특정 작업을 수행하는 코드 블록을 정의하는 방법
1. 함수 : 특정 작업을 수행하는 코드 블록을 정의하는 방법

예를 '사진을 찍는다.'라는 행위에 대해 생각해보면,
1) 주머니에서 폰을 꺼내고,
2) 잠금 화면을 켜고
3) 카메라를 켜고
4) 사진을 찍고자 하는 대상에 폰을 조준하고
5) 셔터를 누른다.

그런데 컴퓨터는 시키는대로만 하기 때문에 사진을 찍기 위해서 1~5까지의 명령어를 입력해줘야한다.

하지만 '사진을 찍는다.'라는 함수 내에 1~5까지의 명령어들을 미리 입력하고 나서 '사진을 찍는다'라고 하면 자연스럽게 명령을 순서대로
수행한다.

주요 수업 예시로는 reeborg's world에서 정의법을 배움

함수를 정의했다는 것은 사용한다는 것이 아니기 때문에 따로 호출해야함

2.  1) 파이썬 내장 함수
    2) 매서드(method)
    3) 사용자 정의 함수

3. 함수 용어 정리
1) 함수 정의 : 사용자 함수로 새로 만드는 것을 의미
2) 인수 : 함수에 전달할 입력값(input)
3) 매개변수 : 인수를 받아서 저장하는 변수를 의미
4) 반환값 / 결과값 / 리턴값 : 함수의 출력값
5) 함수 호출 : 함수를 실제로 사용하는 것ㅇ르 의미

4. (사용자) 함수의 형식:
def 함수_이름(매개변수)
    실행문

변수 = 함수_이름(argument)

'''

#함수 정의
# def write_name(name): #정의할 때 소괄호 내에 있는 것을 parameter
#     print(f"당신의 이름은 {name}입니다.")
# #함수 호출
# write_name("윤지환") #호출할 때 소괄호 내에 있는 것을 argument라고 합니다.
#
# def write_name_age(name, age): #parameter가 복수
#     print(f"당신의 이름은 {name}이고, 나이는 {age}입니다.")
#
# write_name_age("윤지환", 23)
# write_name_age(age=23, name="윤지환")

'''
예를 들어 input("이름을 입력하세요. >>>")을 이용해서 이것을 name이라는 변수에 담았다고 가정하면,
name=input("이름을 입력하세요. >>>")이라고 작성해왔음
즉, 여태까지 함수의 결과값을 변수에 담아오고 있었음

파이썬 내장 함수는 이미 함수가 정의되어있고, 개발자들은 함수 호출만 잘 하면됨
사용자 함수는 개발자 자신이 함수를 정의하고, 그 후에 호출하는 것까지의 과정이라고 생각하면 됨

내장 함수 예시
print, type, int, float, input

2. method : 특정 객체가 가지고 있는 함수를 의미, 특정 자료형에 포함되어있는 함수.
사실 함수와 메서드는 동일한 개념, 호출 방식에 있어서 차이가 있음

함수는 독립적으로 사용가능, 메서드는 특정 객체를 통해서만 호출


'''

# eng_name = input("당신의 이름을 소문자로 입력하세요. >>>").upper()
#
# print(eng_name)
# eng_name2 = input("당신의 이름을 소문자로 입력하세요. >>>").title()
# print(eng_name2)

'''
함수의 유형
'''
# def call1():
#     print("[x ㅣ x]")
#
# def call2():
#     print("[ㅇ ㅣ x]")
#
# def call3():
#     print("[xㅣo]")
#     return "안녕하세요."
#
# def call4(str_type):
#     print("[x ㅣ o]")
#     return f"제 이름은 {str_type}입니다."
#
# print(call3())
# print(call3()+1)
#
# new_element = (call3()+3)*10
# print(new_element)
#
# call4("윤지환")
# print(call4("윤지환"))

'''
call3, call4 유형에서 함수 내에 print()를 집어 넣어두면 main 단계에서(들여쓰기가 되어있지 않은 단계)
print() 함수를 입력할 필요가 없어 훨씬 편할 것 같은데
왜 굳이 return 형태로 입력해서 main에서 일일이 print() 함수를 적용해야 하는가?

함수형 프로그래밍 : 특정한 함수 1의 결과값이
또 다른 함수2의 argument로 사용되는 것을 의미
그리고 함수2의 결과값이 함수3의 argument로 사용되는 것이 반복된다면

'''
#사용자 함수 정의
# def introduce(name, addrees):
#     return f"제 이름은 {name}이고, {address}에 삽니다:
# #함수1 사용 : input() > 파이썬 내장 함수
# name = input("이름을 입력하세요. >>>")
# address = input("주소를 입력하세요. >>>")
# #함수1의 결과값을 함수2인 사용자 함수의 argument로 사용 > 그 결과값을 함수3인 print() 함수의 argument로 사용
# print(introduce(name, address))

'''
700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지
그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록

반환값 : call1~4중 어떤 유형인지 고려하세요
함수이름 vending_machine()
매개변수 정수 money

음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''

# def vending_machine(my_money):
#     for i in range(my_money//700 + 1): #i=int
#         print(f"음료수 = {i}개, 잔돈 = {my_money - (700 * i)}원")
#
# vending_machine(5000)

# my_money = 3000
# drink_price = 700
# charge = 3000-(700*)

# for i in range(my_money//drink_price) + 1):
#     print(f"음료수 = {i}개, 잔돈 = {my_money-(drink_price*i)}원")

'''
예제 : 구구단 출력
함수 정의 :
함수 이름 : multiply
매개변수 : 정수 n
리턴값 : 없음

함수 호출 :
multiply(dan)

몇 단을 출력하시겠습니까? >>> 3

# dan = 2
# while dan < 10: #값이 있으면 True로 취급
#     number = 1
#     while number < 10:
#         print(f"{dan}x{number} = {dan*number}")
#         number += 1
#     dan += 1
'''


# def munltiply(n):
#     n = int(input("몇 단을 출력하시겠습니까? >>>"))
#     for i in range(1, 10, 1): #range 시작, 종료, 증감
#         print(f"{n}*{i}={n*i}")







