'''
Scope : 범위

지역 변수 : 함수 내부에 정의된 변수
전역 변수 : 함수 외부에 정의된 변수 (main)


'''

# enemies = 1
#
# def increase_enemies():
#     enemies = 2 #같은 이름이지만 지역 변수
#     print(f"함수 내부의 적의 숫자는 {enemies}입니다.")
#
# increase_enemies()
# print(f"함수 외부의 적의 숫자는 {enemies}입니다.")

#지역 변수는 전역 변수와 다름 > 그렇기 때문에 변수명을 서로 다르게 짓는게 혼란을 피하는 방식

#함수 정의
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)
#지역 변수 선언 후 호출한다고해서 메인에서 해당 변수를 참조하는 것은 불가능



'''
Global_Scope

'''

player_health = 10

# def game():
#     def drink_potion():
#         # player_health += 2 #전역에서 선언되고 초기화된 변수를 함수 내에서 조작하는 것은 불가능
#
#         global player_health
#         player_health += 2
#
#         #이상의 코드에서 생겨날 수 있는 잠재적 문제점은
#         #함수의 호출 횟수에 따라 전역 변수의 값이 바뀌기 때문에
#         #함수의 호출 횟수를 알아야함
#         #이상을 이유로 함수가 전역 변수의 값을 바꾸는 이러한 코딩 방식은 선호되지 않음
#     drink_potion()
#
# game()
# print(f"체력은 {player_health}입니다.")

game_level = 3
def create_enemy():
    enemies = ["좀비", "스켈레톤", "에일리언"]
    if game_level < 5:
        new_enemy = enemies[0]


    print(new_enemy)

create_enemy()
'''
이상의 코드에서 생기는 문제점
1. game_level 이라는 전역 변수를 creat_enemy 라는 함수의 정의 부분에서 사용하고 있음에도 오류 발생하지 않음
2. 함수 정의 내부의 if절에서 new_enemy라는 변수는 선언 및 초기화 했음에도,
if 절 바깥에서 new_enemy를 참조했음에도 오류가 발생하지 않음.

1.의 이유 : game_level이라는 전역변수의 값을 바꾸는게 아니라, 참조만 해서 True/False만 변환하기 때문에 오류 발생하지 않음
2.의 이유 : if, while, for문 등 콜론을 기준으로 들여쓰기가 있는 모든 코드 블록들은 지역 변수를 만드는 것으로 간주되지 않음
지역 변수의 용어 정의에 주목할 필요가 있음
'''













