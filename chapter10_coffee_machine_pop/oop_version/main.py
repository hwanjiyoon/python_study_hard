from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"어떤 음료를 드시겠습니까? {menu.get_items()}>>>").lower()
    # todo - 1 : choice가 off/report 오타났을 때 작성하는 부분을 완성하시오.
    if choice == "off":
        is_on = False
        print("자판기가 종료되었습니다.")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) #음료 객체를 변수명 drink에 저장
        if drink == None:
            continue        #continue가 실행되면 이 밑의 코드라인은 실행되지 않고 while 반복문의 맨 앞으로 돌아감
        # 여기서부터 오타없이 메뉴 이름을 정확하게 작성했을 때 의 로직
        # 재료가 충분한지 확인 > 돈 받는다 > 반은 돈이 음료 가격보다 높으면 커피 만든다
        # import 받은 애들은 하나도 수정 안하고 여기 부분만 작성해서 동일한 자판기 프로그램을 완성하시오.
        if coffee_maker.is_resource_sufficient(drink):
            # coffee_maker.is_resource_sufficient()메서드 확인해보면
            # drink.ingredients를 반복문 돌린다는 것을 확인 가능
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)