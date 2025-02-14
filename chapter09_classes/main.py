'''
1. 클래스 도입의 필요성


'''
# #매개 변수가 6개인 함수 정의
# def student_info(name, department, professor, phone, address, grade):
#     print(name)
#     print(department)
#     print(professor)
#     print(phone)
#     print(address)
#     print(grade)
#
# # name1 = "윤지환"
# # department1 = "에너지자원공학과"
# # professor1 = "David"
# # phone1 = "010-1234-5678"
# # address1 = "부산광역시 동래구"
# # grade1 = "A"
#
# # student_info(name1, department1, professor1, phone1, address1, grade1)
#
# '''
# 지금까지 배운 함수와 매개변수, 그리고 argument를 통해 6개의 변수를 처리했습니다. 하지만 만들어야 할 변수의 개수가 많고, 학생 한 명당
# 매개변수가 6개라면, 학생이 100명일 경우 600개의 변수를 처리할 필요가 있습니다.
#
# '''
#
# student_info(grade="B",
#              address="서울특별시 종로구",
#              phone="010-2345-6789",
#              professor="John",
#              department="computer science",
#              name="김일"
#              )
#
# #name2, ... grade2라는 변수들을 선언하고 거기에 정보를 입력한뒤
# #keyword argument를 통해서 student_info()함수를 호출
#
# name2 = "김이"
# department2 = "자동차공학과"
# professor2 = "Max"
# phone2 = "010-3456-7890"
# address2 = "부산광역시 해운대구"
# grade2 = "B"
#
# student_info(name=name2, department=department2, professor=professor2, phone=phone2, address=address2, grade=grade2)

'''
이상의 상황들(변수에 각각 데이터를 대입한 후에 함수의 argument로 사용하거나, 혹은 데이터를 직접 argument에 등록)을
벗어나기 위해 클래스와 객체 개념을 도입

class란? : 객체를 만드는 도구 - 설계도/틀/청사진

    자동차 설계도 > 클래스
    설계도를 통해 생성된 자동차들 > 객체
    
    같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있음.
    마찬가지로 같은 클래스로 만든 객체라 하더라도 서로 다른 값을 가질 수 있음.
    
    인스턴스 역시 클래스를 이용해서 생성된 객체를 가리키는 용어
    객체와 인스턴스 그 둘을 바라 보는 관점의 차이로 볼 수 있음.
    
    1. '자동차 설계도'로 만든 자동차는 객체(object)입니다.
    2. 자동차는 자동차 설계도의 인스턴스(instance)입니다.
    
1. 클래스 정의
    클래스를 작성하는 것을 클래스 정의라고 합니다. > 함수 정의를 생각하시면 됩니다.
    
    형식 :
    class 클래스명(대문자로시작)
        본문
        
    객체생성형식 :
    객체이름 = 클래스명()
'''

class WaffleMachine:
    pass  #코드를 나중에 작성하겠다는 의미 실행시켜도 오류 안남

#객체 생성 예시
waffle = WaffleMachine() #소괄호() 중요함
print(waffle)
'''
print(waffle)을 실행시켰을 때 <__main__.WaffleMachine object at 0x000002AA255713A0>에서 object라고 표기된 
점을 미루어 waffle은 WaffleMachine의 객체임을 확인할 수 있음.

클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지닙니다.
    객체를 생성하기 위해서는 클래스는 객체가 가져야 할 '값'과 '기능'을 지녀야 합니다.
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 변수는 두 가지로 구분됩니다.
        1)클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
        2)인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
        
    메서드는 특징에 따라서
        1)클래스 메서드
        2)정적 메서드
        3)인스턴스 메서드
        
    인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미
        모든 인스턴스 변수는 self라는 키워드를 앞에 붙여준다.
        
    인스턴스 메서드 : 인스턴스 변수를 사용하는 메서드
        인스턴스 변수값에 따라서 각 인스턴스마다 다르게 동작됩니다.
        인스턴스 메서드는 첫 번째 매개변수로 self를 추가해야합니다.
'''


# class Person:
#
#     def set_info(self, name, age, tel, address):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.address = address
#
#     def display_info(self):
#         print(f"이름 : {self.name}")
#         print(f"나이 : {self.age}")
#         print(f"전화 : {self.tel}")
#         print(f"주소 : {self.address}")
#
#     def display_info2(self):
#         print(f"제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}인데, {self.address}에 살고 있습니다.")
#
# person01 = Person()
# person01.set_info("윤지환", 23, "010-1234-5678", "부산광역시 동래구")
# person01.display_info()
#
# person02 = Person()
# person02.set_info("김일", 20, "010-2345-6789", "부산광역시 해운대구")
# person02.display_info2()

# person02 객체 생성 person02.set_info()를 활요해 이름 나이 연락처 주소를 입력하고
# display_info2()를 정의하여 다음 실행 예와 같이 출력되도록 작성하시오.
# 제 이름은 ___이고, __살입니다.
# 연락처는 ____인데, ____에 살고 있습니다.
# print(person02.display_info2())

'''
응용 예제

다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book 클래스 생성 > 객체 생성

1. 다음과 같은 방법을 book1과 book2 인스턴스 생성

book1 = Book()
book2 = Book()

2. set_info(self, title, author)를 통해 책 제목 입력

3.display_info()를 통해 실행 예와 같이 출력되도록 작성하세요.

실행 예
책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생텍쥐페리

'''

class Book:

    def set_info(self, title, author, stock):
        self.title = title
        self.author = author
        self.stock = stock

    def display_info(self):
        print(f"책 제목 : {self.title} \n책 저자 : {self.author}")


book1= Book()
book2= Book()
book1.set_info("파이썬", "민경태", 3)
book2.set_info("어린왕자", "생텍쥐페리", 10)
#book2.set_info(title= "어린왕자", author= "생택쥐페리") > keyword argument 사용
book1.display_info()
book2.display_info()

#특정 객체의 속성값을 확인하는 방법
#객체명.속성명
print(book1.title)
print(book1.stock + 2) #연산도 가능


