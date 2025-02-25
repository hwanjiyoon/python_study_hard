# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_name = ["구분", "부모 클래스", "자식 클래스"]
# table.add_row(["의미", "상속해주는 클래스", "상속받는 클래스"])
# table.add_row(["용어", "슈퍼 클래스", "서브 클래스"])
# table.add_row(["", "기반 클래스", " 파생 클래스"])
# print(table)

'''
1. 상속이란?
    어떤 클래스가 가지고 있는 기능을 그대로 물려받아서 사용할 수 있는 클래스를 생성할 수 있는데,
    클래스의 기능을 물려받을 때 상속받는다는 표현을 사용함
    상속 관계에 있는 클래스를 표현할 때 부모(슈퍼) 클래스/자식(서브) 클래스라는 용어를 사용함.
+---------+-------------------+-----------------+
| Field 1 |      Field 2      |     Field 3     |
+---------+-------------------+-----------------+
|   의미  | 상속해주는 클래스 | 상속받는 클래스 |
|   용어  |    슈퍼 클래스    |   서브 클래스   |
|         |    기반 클래스    |    파생 클래스  |
+---------+-------------------+-----------------+

2. 상속 관계 구현
    두 클래스가 상속 관계에 놓이려면 IS-A 관계를 성립해야 함. IS-A 관계란 "~은 ~이다."로 해석할 수 있는
    관계를 의미
    ex) 학생은 사람이다.
    
    IS-A 원문 : is a kind of > Dog is a kind of Animal > 개는 동물의 일종이다. 
    
형식 :
class 슈퍼클래스:
    본문
class 서브클래스(슈퍼클래스):
    본문
'''

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print(f"{self.name}이(가) {food}을(를) 먹습니다.")
#
# class Student(Person):
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school
#
#     def study(self):
#         print(f"{self.name}은(는) {self.school}에서 공부합니다.")
#
# potter = Student(name="해리포터", school="호그와트")
# potter.eat("감자")
# potter.study()

'''
3. 서브 클래스의 __init__()

서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없습니다. 그러나 서브 클래스의 생성자를 구현할 때는
'반드시 슈퍼 클래스의 생성자를 먼저 호출'하는 코드를 작성해야만 합니다.

super > 슈퍼 클래스를 의미. 즉, Student의 생성자를 호출하려면 super(). __init__(name)에 의해서
슈퍼 클래스인 Person의 생성자가 먼저 호출되면서 슈퍼 클래스의 객체가 '생성'됩니다.
이후 슈퍼 클래스에서 생성된 인스턴스 변수인 name이 서브 클래스로 전달되고, 이후에 서브 클래스에서 school
인스턴스를 선언 및 초기화하여 저장하면서 서브 클래스의 객체가 생성됩니다.

4. 서브 클래스의 인스턴스 자료형

슈퍼 클래스의 객체는 서브 클래스의 인스턴스이면서 슈퍼 클래스의 인스턴스
Student 클래스의 객체는 Student의 인스턴스이면서 동시에 Person의 인스턴스라는 의미입니다.

어떤 객체가 특정한 클래스의 인스턴스인지 아닌지를 확인하기 위해서 사용하는 함수 : isinstance()

형식 :
isinstance(객체명, 클래스명)
'''

# print(isinstance(potter, Student))
# print(isinstance(potter, Person))

'''
isinstance()의 리턴값은 : bool 자료형으로 True/False를 반환함
'''

'''
다음 지시사항을 읽고 Hybrid 클래스를 구현하세요.

지시사항
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스를 구현하세요.
2. 서브 클래스 Hybrid는 다음과 같은 특징을 가지고 있습니다.
    최대 배터리 충전량은 30입니다.
    베터리를 충전하는 charge()메서드가 있습니다. 최대 충전량을 초과하도록 충전할 수 없고,
    0보다 작은 값으로 충전할 수 없습니다.
    현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다
    
3. 다음과 같은 방식으로 전체 동작 확인

car = Hybrid(oil = 0, amount=0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()


'''

class Car:
    max_oil = 50
    def __init__(self, oil):
        self.oil = oil
    def add_oil(self, oil):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f"현재 주유 상태 : {self.oil}")

class Hybrid(Car):
    max_amount = 30

    def __init__(self, oil, amount):
        super().__init__(oil)
        self.amount = amount

    def charge(self, amount):
        if amount <= 0:
            return
        self.amount += amount
        if self.amount > Hybrid.max_amount:
            self.amount = Hybrid.max_amount

    def hybrid_info(self):
        super().car_info()
        print(f"현재 충전 상태 : {self.amount} ")


car = Hybrid(oil=0, amount=0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()








