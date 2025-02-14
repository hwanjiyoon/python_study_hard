'''
1. 생성자(constructor)
'''

# 클래스 정의
# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색은 {self.color}입니다.")
#
# satang = Candy()
# satang.set_info("구형", "갈색")
# satang.display_info()

'''
satang이라는 인스턴스는 생성된 이후에 set_info() 메서드를 호출하여 구형 모양의 갈색이라는 속성을 갖게됨
satang 인스턴스의 생성과정
1. 값이 없는 인스턴스 생성
2. 값을 저장할 수 있는 메서드 호출

그러면 처음부터 값이 있는 인스턴스를 생성하면 코드라인이 줄어들지 않을까
이에 대한 해답이 생성자라는 개념
__init__() 라는 메서드


__init__()메서드는 인스턴스가 생성될 때 자동으로 호출되기 때문에 인스턴스 변수 초기화 용도로 사용 즉, 값이 있는 인스턴스를 생성할 수
있다는 의미. 객체 생성과 동시에 생성자가 호출됨. 초기값을 작성할 때 사용한다는 의미

'''

# class Candy2():
#
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색은 {self.color}입니다.")
#
# satang2 = Candy2("정육면체", "흰색")
# satang2.display_info()


'''
이상에서 주목해야 할 점은 satang 인스턴스와 satang2의 생성 방식의 차이

2. 소멸자(Destructor)
    인스턴스가 생성될 때 자동으로 생성되는 생성자와 마찬가지로 인스턴스가 소멸될 때 호출되는 메서드
    이를 소멸자라고 하며, 소멸자를 정의하는 메서드는 __del__()
'''

# class Sample():
#
#     def __init__(self):
#         print(f"인스턴스가 생성되었습니다.")
#
#     def __del__(self):
#         print(f"인스턴스가 소멸되었습니다.")
#
# sample = Sample()
# del sample
# print("프로그램이 종료되었습니다.")

'''
기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오

지시 사항 
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수 capacity를 받을 것
3. get_info() 메서드를 정의할 것

usb = USB(64)
usb.get_info()

실행 예
64GB USB
'''

# class USB:
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def get_info(self):
#         print(f"{self.capacity}GB USB")
#
# usb = USB(64)
# usb.get_info()

'''
생성자와 소멸자를 이용하여 서비스 안내 메시지를 출력하는 프로그램

class Service를 정의하고, 생성자를 통해 매개변수 service로 받고, print()메서드를 생성자와 소멸자 내에 작성하시오.

main
s = Service("길 안내")
del s

실행 예
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.
'''

# class Service:
#     def __init__(self, service):
#         self.service = service
#         print(f"{self.service} Service가 시작되었습니다.")
#
#     def __del__(self):
#         print(f"{self.service} Service가 종료되었습니다.")
#
# s = Service("길 안내")
# # del s #없어도 뜨는데 코드가 다 돌아가면 종료가 되니까 그런거임
#
# print("프로그램이 종료되는 시점")
# del s


'''
응용 예제

1. 다음 지시사항을 읽고 이름을 저장하는 Person 클래스를 생성

1, man과 woman 인스턴스 생성
man = Person("James")
woman = Person("emily")

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지 출력

james is born
emily is born

3. 다음과 같은 방법으로 man 인스턴스 삭제
del man

인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성
james is dead
'''
class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is born.")
    def __del__(self):
        print(f"{self.name} is dead.")

man = Person("James")
woman = Person("emily")

del man
print("프로그램이 종료되었습니다.")


'''
예제1 

학생들의 성적을 관리하는 Student 클래스를 작성
이 클래스는 학생의 이름, 학번, 성적을 인스턴스 변수로 갖습니다.

지시사항
1) Student 클래스를 정의하고 생성자를 통해 name, student_id, grade을 초기화 하시오
2) 학생의 프로필을 출력하는 인스턴스 메서드 print_profile()를 작성하시오.
3) 학생의 성적을 변경할 수 있는 인스턴스 메서드 set_grade()를 작성하시오.
>이 부분이 고민 요소
4) 세명의 학생 인스턴스를 생성하고 각 항생의 정보를 출력한 다음 성적을 변경하고 다시 출력

student1 = Student("김철수", 20250001, "A")
student2 = Student("이영희", 20250002, "B")
student3 = Student("박민지", 20250003, "C")

실행 예

학생 이름 : 김철수
학번 : 20250001
성적 : A
...

이후 student1 성적을 A+, 2는 A, 3는 B+로 성적 변경
'''

class Student:

    def student_info(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def print_profile(self):
        print(f"학생 이름 : {self.name} \n 학번 : {self.student_id} \n성적 : {self.grade}")

    def set_grade(self, grade):
student1 = Student("김철수", 20250001, "A")
student2 = Student("이영희", 20250002, "B")
        student3 = Student("박민지", 20250003, "C")
