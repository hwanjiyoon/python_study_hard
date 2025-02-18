'''
은행 계좌를 관리하는 BankAccount 클래스 생성 이 클래스는 계좌 소유자 이름, 계좌 번호, 잔액을 인스턴스 변수로 가짐

지시 사항 1. BankAccount 클래스를 정의하고 '생성자를 통해' owner, account_num, balance를 초기화 하시오.
        2. 각 인스턴스 변수에 대한 setter / getter 정의.
        3. 입금 기능을 하는 메서드(deposit())를 구현하시오. 입금 금액을 입력 받아 잔액을 증가시킴.
        > 입금 금액이 0이라면 입금이 불가능 하도록 구현.
        4. 출금 기능을 하는 인스턴스 메서드(withdraw())를 구현하시오.
        >잔액-출금금액이 0 미만이라면 출금이 불가능 하도록 로직 설정.
        5. 계좌 정보를 출력하는 인스턴스 메서드 print account_info를 구현하시오.
        6. 두 개의 계좌를 생성하고, 입금과 출금을 수행한 후 계좌 정보를 출력하시오.

'''

class BankAccount:

    def __init__(self, owner, account_num, balance):
        self.owner = owner
        self.account_num = account_num
        self.balance = balance

    def set_owner(self, owner):
        self.owner = owner

    def set_account_num(self, account_num):
        self.account_num = account_num

    def set_balance(self, balance):
        self.balance = balance

    def get_owner(self):
        return

    def get_account_num(self):
        return

    def get_balance(self):
        return self.balance

    def print_account_info(self):
        print(f"계좌 소유자 : {self.owner}")
        print(f"계좌 번호 : {self.account_num}")
        print(f"현재 잔액 : {self.balance}")

    def deposit(self, money):
        if money <= 0:
            print(f"{money}는 입금할 수 없는 금액입니다.")
            return
        self.balance += money
        print(f"{money} 입금되었습니다. 현재 잔액 {self.balance}입니다.")

    def withdraw(self, money):
        if money <= 0:
            print(f"{money}는 출금할 수 없는 금액입니다.")
            return
        if self.balance - money <0:
            print("잔액이 부족하여 출금할 수 없습니다.")
            return

        self.balance -= money
        print(f"{money} 출금되었습니다. 현재 잔액 {self.balance}입니다.")

account1 = BankAccount("홍길동", "123-456-789", 100000)
account2 = BankAccount("신사임당", "987-645-432", 500000)

account1.print_account_info()
account2.print_account_info()

account1.deposit(50000)