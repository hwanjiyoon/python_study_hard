'''
1. 클래스 변수
    인스턴스 변수 : 인스턴스마다 서로 다른 값을 지니는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 :
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근 방식 - 인스턴스 접근(o)
                 - 클래스 접근(x)
    클래스 변수 :
        목적 - 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                 - 클래스 접근(o)

'''
# class Korean:
#     country = "한국"
#
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
# man = Korean(name="윤지환", age=23, address="부산광역시 동래구")
# print(man.name)
# print(man.age)
# print(man.address)
# print(man.country)
# print(Korean.country)

#객체명.클래스변수를 통해서 클래스 변수에 접근이 가능하긴 하지만 클래스 내부의 코드를 들여다보기 전까지는 country라는 변수가
#클래스 변수인지 인스턴스 변수인지 확인이 불가능하다는 문제가 있습니다.

#이상의 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명으로 참조하기 보다는
#클래스명.클래스변수명을 통해서 참조하는 것이 바람직합니다.

'''
클래서 메서드: 클래스 변수를 사용하는 메서드
'''
class Korean2:
    country = "대한민국"

    @classmethod
    def trip(cls, travelling_site):
        if cls.country == travelling_site:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")

#클래스 메서드의 호출
Korean2.trip("대한민국")
Korean2.trip("미국")
#객체 생성
man2 = Korean2
man2.trip("일본")
#클래스 변수 때와 마찬가지로 개개체명.클래스 메서드명()으로 호출 가능
#>하지만 마찬가지로 얘가 인스턴스 메서드인지 클래스 메서드인지 구분할 수 없기 때문에
#권장되는 코드 작성 요령이 아닙니다.