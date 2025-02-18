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
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is born.")
#     def __del__(self):
#         print(f"{self.name} is dead.")
#
# man = Person("James")
# woman = Person("emily")
#
# del man
# print("프로그램이 종료되었습니다.")


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

# class Student:
#     #생성자
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade
#     #객체의 인스턴스 변수 값을 출력해주는 메서드
#     def print_profile(self):
#         print(f"학생 이름 : {self.name} \n 학번 : {self.student_id} \n성적 : {self.grade}")
#
#     #이상의 코드는 콘솔에 찍히기만 할 뿐 연산이 불가능 call3()유형
#     def get_grade(self):
#         return self.grade
#     #grade만 바꾸게 될 메서드 > set_info() : Book 클래스의 set_info()메서드 참조
#
#     def set_grade(self, grade):
#         if grade not in ["A+", "A", "B+", "B", "C+", "C", "D+", "F"]:
#             print("불가능한 점수 입력입니다.")
#         self.grade = grade #Book클래스에서 set_info(self, title, author):
# #객체 생성
# student1 = Student("김철수", 20250001, "A")
# student2 = Student("이영희", 20250002, "B")
# student3 = Student("박민지", 20250003, "C")
#
# student1.print_profile()
# student2.print_profile()
# student3.print_profile()
#
# student1.set_grade("A+")
# student2.set_grade("A")
# student3.set_grade("B+")
#
# student1.print_profile()
# student2.print_profile()
# student3.print_profile()

#
# student1.print_profile()
# #방법1) 속성값을 직접 참조하여 변경
# student1.grade = "A+"
# student1.print_profile()
# #방법2)
# student1.set_grade("A+")
# student1.print_profile()
#
# student1.set_grade("불가능한 점수")
# student1.print_profile()
#인스턴스 변수에 값을 대입할 때 제약을 걸기 위해 method를 경유하여 값을 대입하도록 권장

#setter(call2()유형), getter(call3()유형) > 클래스로 돌아가서 해당 메서드 추가


'''
1. Setter / Getter
1) Setter : 객체의 속성 값을 변경하는 메서드
2) Getter : 객체의 속성 값을 조회하는 메서드

3) 왜 사용하는가
(1) 데이터 보호 및 무결성 유지 : 속성 값을 직접 변경하는 경우, 잘못됨 값이 입력될 가능성이 높음
                             Setter를 사용하면 특정 조건을 만족하는 값만 속성에 대입 가능
                             
(2) 객체의 캡슐화 실현 : 객체 내부의 데이터를 외부에서 직접 수정하는 것을 방지
                       대신 메서드를 통해서만 접근하도록 제한하여 보안성을 높임
                       
(3) 추후 유지 보수 및 확장성 용이 : Setter / Getter를 사용하면 특정 속성에 대한 로직을 쉽게 변경 가능
                                예를 들어, 특정 속성을 설정할 때 추가적인 검증이 필요하면 Setter에서 처리 가능
                                

2. 클래스를 정의할 때 기본적으로 Setter / Getter를 타이핑하면서 형태를 배울 것
1) Setter : call2() 유형
2) Getter : call3() 유형
'''

# Setter > Getter 적용 예시

class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        if self.age > 0 or self.age < 200:
            return self.age
        else:
            print("입력이 불가능합니다.")

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def print_person_info(self):
        print(f"제 이름은 {self.name}입니다.\n나이는 {self.age}입니다.\n주소는 {self.address}입니다.")

person1 = Person("윤지환", 202, "부산광역시 동래구")
person1.print_person_info()




