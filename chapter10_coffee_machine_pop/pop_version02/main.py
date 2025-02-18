MENU = {
    "에스프레소": {
        "재료": {
            "물": 50,
            "커피": 18,
        },
        "가격": 1.5,
    },
    "라떼": {
        "재료": {
            "물": 200,
            "우유": 150,
            "커피": 24,
        },
        "가격": 2.5,
    },
    "카푸치노": {
        "재료": {
            "물": 250,
            "우유": 100,
            "커피": 24,
        },
        "가격": 3.0
    }
}

profit = 0
resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,

}


def is_resources_enough(order_ingredients):
    """DocString : 함수/클래스/메서드가 어떤 작동을 하는지 사람들에게 설명해주는 기능
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면
    True 반환, 아니면 False 반환
    :param : order_ingredients
    :return : True/False"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이(가) 부족합니다.")
            return False
        return True

def process_coins():
    """동전들을 입력받아 전체 금액을 반환하는 함수 call3() 유형
    쿼터, 다임, 니켈, 페니 네 종류의 동전
    쿼터 : 0.25 달러
    다임 : 0.1 달러
    니켈 : 0.05 달러
    페니 : 0.01 달러
    quarters, dimes, nickels, pennies
    """
    total = 0.0
    total += int(input("쿼터 동전을 몇 개 넣으시겠습니까?")) * 0.25
    total += int(input("다임 동전을 몇 개 넣으시겠습니까?")) * 0.1
    total += int(input("니켈 동전을 몇 개 넣으시겠습니까?")) * 0.05
    total += int(input("페니 동전을 몇 개 넣으시겠습니까?")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아 동전이 가격보다 높으면 True 아니면 False 반환"""
    charge = money_received - drink_cost
    if charge >= 0:
        global profit
        profit += drink_cost
        print(f"잔돈${charge}를 반환합니다.")
        return True
    else:
        print("동전이 충분하지 않습니다. 금액을 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """
    resources에 있는 재료에서 MENU[음료이름][재료]들을 차감함
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"{drink_name}가 나왔습니다. 맛있게 드세요!")

is_on = True

while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>>")

    if choice == "off":
        is_on = False
        print("자판기가 종료되었습니다.")
    elif choice == "report":
        print(f"물 : {resources["물"]}ml")
        print(f"우유 : {resources["우유"]}ml")
        print(f"커피 : {resources["커피"]}ml")
        print(f"돈 : ${[profit]}")
    elif choice in ["에스프레소", "라떼", "카푸치노"]:
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]) and is_transaction_successful(process_coins(), drink["가격"]):
                make_coffee(choice, drink["재료"])
    else:
        print(f"잘못 입력하셨습니다. 다시 입력해주세요.")
