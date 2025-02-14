'''
컬렉션(collection) : 여러 값을 하나의 이름으로 묶어서 관리하는 자료형
string의 경우 문자 하나를 줄로 묶어서 문자열로 출력
예를 들어 '다수의 다른 string을 관리하는 방법은 무엇일까?' 에 대한 대답

여러 명의 프로필을 관리한다고 가정


'''



# ahngeunsu = "이름 : 안근수\n 나이 : 38\n직업 : 파이썬 강사"
# print(ahngeunsu)


'''
한 명을 저장하는 데에는 문제가 없음 매번 변수 하나에 이름, 나이, 직업 등을 추가할 때마다 비효율적임 

그리고 주소를 추가한다고해도 변수들을 전부 다 참조해서 수정해줘야 할 필요성이 있음

이상의 문제들을 한꺼번에 관리하기 위한 방식으로 모음을 사용

종류 : 1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능 a = [1, 2, 3] 대괄호 사용
      2. tuple 튜플 : 추가 / 수정/ 삭제가 불가능 a = (1, 2, 3) 소괄호 사용
      3. set 세트 : 중복된 값의 저장이 불가능 / a = {1, 2, 3} 중괄호 사용
      4. dict 딕트(딕셔너리) : 키 + 값으로 관리 / a = {"name":"안근수", "age":38} 중괄호 사용
      
1. list
여러 값을 저장할 때 가장 많이 사용
자료형이 달라도 하나의 리스트에 저장가능
하나의 배열에 동일한 자료형만을 저장할 수 있는 python만의 장점
'''

# ii = [1, 2, 3, "윤지환"]
# print(list)

'''
1-1. list와 index와 slice
     list는 str과 동일한 방식의 index와 slicing을 지원함
     1) 인덱스와 마이너스 인덱스
'''

# print(li[0])
# print(li[1])
# print(li[2])
# print(li[3])
# print(li[-1])
# print(li[-2])
# print(li[-3])
# print(li[-4])

'''
2) slice
str의 슬라이싱과 같이 '시작인덱스:종료인덱스:증감값'으로 이루어져 있음

'''

# list_num1 = [100, 3.14, "hello"]
# list_num2 = list([4, 5, 6, 7, 8, 9])
# print(list_num1)
# print(list_num2[0:4:2])

'''
3) list 요쇼의 추가와 삭제
list에 새로운 요소를 추가할 때는 .append()와 .insert() '메서드'를 사용할 수 있음
기존 요소를 삭제할 때는 .pop() 메서드를 사용

.append() : 항상 마지막 인덱스에 요소를 충가
.insert(위치, 값) : 정해진 위치에 해당 값을 추가하는 메서드
'''

# scores = [30, 40, 50] #scores라는 list 내에 있는 int 데이터인 각각의 30, 40 ,50
# print(scores)         #요소라고 합니다. (element)
# scores.append(100)    #함수와 달리 list명.메서드명(데이터)와 새로운 형태로 사용
# print(scores)
# scores.insert(0, 90)
# print(scores)

'''
pop()의 경우 빈 괄호로 사용하게 되면 맨 마지막 요소가 삭제됨
pop(인덱스넘버)로 작성하면 해당 인덱스의 요소를 삭제함
'''
# scores.pop()
# print(scores)
# scores.pop(0) #오버로딩의 기초 개념이 포함되어 있어서 동일한 메서드명인데도 argument가 있을 수도 있음
# print(scores)

'''
.remove(값)을 사용하면 list내에 해당 값을 찾아 삭제함
'''

# scores.remove(40)
# print(scores)
#이상의 코드까지 실행시켰을 때, 인덱스가 두개 밖에 없어서 10개 정도의 element를 추가하는 반복문 작성
# for i in range(10):
#     scores.append(i*10)
# print(scores)
# for i in range(len(scores)):
#     print(scores[i])

#위 코드를 참조해서 전체 element를 뽑아내는 반복문을 작성 .len()함수 이용할 것
#list 내에 요소들을 하나씩 뽑아 내는 반복문 - for문

#향상된 for문
# for score in scores: #collections의 경우 복수로 이름 짓고 향상된 for문에서는 각 변수는 단수로 이름 짓는 경우가 많음
#     print(score)
#
# for score in scores:
#     scores.append(10)



'''
tuple() : 지정된 값을 변경할 수 없는 list라고 생각하면 됨 index와 slice를 사용하지만 저장된 값 이외에는
추가, 삭제, 수정이 불가

'''

# tuple_num1 = (1, 2, 3)
# tuple_num2 = tuple((4, 5, 6))
# tuple_num3 = 7, 8, 9
# print(tuple_num1)
# print(tuple_num2)
# print(tuple_num3)
# #복수의 변수 선언 및 초기화 방법

'''
튜플 생성 방법 3을 이용한다고 가정했을 때, 값이 하나 밖에 없는 튜플을 생성한다면
tuple_num4 = 0이라고 입력할 경우 생기는 문제는 무엇일까?
'''

# tuple_num4 = 0
# print(tuple_num4)
# print(type(tuple_num4))
# tuple_num5 = 0,
# print(tuple_num5)
# print(type(tuple_num5))

'''
1) 튜플에서의 인덱스 / 마이너스인덱스

'''

# tuple_num6 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(type(tuple_num6[2])) #collections의 element에 type() 함수를 적용하면
#                            #element의 자료형이 반환됨
#                            #즉, tuple_num6[2]는 3이라는 element를 가리키기 때문에
#                            #type함수 적용시 int의 자료형이 뜸
#

# tuple_num7 = "hello. ", "nice to meet you. ", "my name is ", "yun jihwan. ", "I am ", "23 ", "years old."
#
# for words in tuple_num7:
#     print(words.title(), end="")
#
# for words in tuple_num7:
#     print(words, end="") #words.title()을 적용시켰다고 해서 tuple내의 element들이 전부 값이 바뀐 상태가 유지되는 것이 아니라
#                          #words.title() 이렇게 작성했을 때만 메서드가 적용된 상태이기 때문에
# #튜플의 정의를 생각하면
# str_example = "yunjihwan"
# print(str_example.upper())

'''
3. set
수학의 집합 개념을 구현한 자료형. list와의 차이점은 순서가 없기 때문에(비스퀀스) 인덱스 및 슬라이싱 사용이 불가능.
중복된 값의 저장이 불가능

이를 활용하여 중복 제거용으로 사용하는 경우와, 교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우 사용

set를 사용하기 위해서는 중괄호({})를 사용함
'''
# set_num1 = {1, 2, 3}
# set_num2 = set({4, 5, 6})
# print(set_num1)
# print(set_num2)
#
# li = []
# tu = ()
# se = {}

# print(type(li)) #<class 'list'>
# print(type(tu)) #<class 'tuple'>
# print(type(se)) #<class 'dict'>


'''
se = {} 형태로 비어있는 set 생성시 se는 사실 <class 'dict'> 때문에 비어있는 set를 만들기 위해서는 세트
생성 방법 2를 사용해야만 함
'''
#
# se = set({})
# print(type(se2))

'''
특징:
1. 저장되는 순서가 없다. > 인덱싱 / 슬라이싱 불가능
2. 중복되는 값을 지정할 수 없다.
3. 2.의 특징으로 인해 set 단독으로 쓰이기 보다는 list와 연계해서 많이 쓰임
'''

# list_num5 = [1, 1, 2, 2, 3, 3, 3]
# print(list_num5)
# set_num5 = set(list_num5)
#
# print(set_num5)
# list_num6 = list(set_num5)
# print(list_num6)

'''
set에는 인덱싱 / 마이너스인덱싱 / 슬라이싱을 지원하지 않기 때문에 특정 요소만 추출하기 위해서는
형변환 과정이 필요함

요소 관련 메서드
.add() - set에 새로운 요소 추가
.remove() - 기존 요소 삭제
.discard() -  기존 요소 삭제
'''

# set_num6 = {10, 20, 30}
# set_num6.add(50)
# print(set_num6)
# set_num6.remove(50)
# print(set_num6)
#
# set_num6.remove(70) #정확하게 입력해야함
# set_num6.discard(70) #요소에 정확한 값이 있지 않더라도 오류가 발생하지 않음

'''
4. dictionary - 말 그대로 사전의 의미를 생각
flower : 꽃
dictionary : 사전
등으로 기재되어있음. 즉 ":"울 기준으로 좌측과 우측이 나누어진 형태를 가지고 있는데 딕셔너리는 리스트, 튜플, 세트와 달리
key : value의 구성으로 이루어져있음
'''

# dict_num1 = {
#     "이름" : "윤지환",
#     "나이" : 23,
#     "주소" : "부산광역시 동래구",
# }

#맨 마지막에 있는 ,의 의미는 혹시 후에 key_value를 추가할 때 이전 라인에서 콤마를 입력하고 엔터치고
#또 key : value의 형태롤 작성하기 귀찮으니까 미리 쉼표를 찍어놔서 쉽게 추가할 수 있도록 하는게 매너

'''
딕셔너리는 인덱스는 존재하지 않지만 위와 같이 key를 인덱스와 유사하게 사용함.
즉, key 값을 알면 저장된 값을 확인할 수 있는 구조
'''

# li2 = [10, 20 ,30 ,40]
# for num in li2:
#     print(num)
#
# # #dictionary에서 같은 방식의 반복문을 활용하게 될 때,
# for i in range(len(dict_num1)):
#     print(dict_num1[i])
#
# for key in dict_num1:
#     print(key) #그냥 print()하게 되면 dict_num1의 key만 추출됨.
#     print(dict_num1[key])
#     print()
#
# #key 목록을 추출하는 메서드
# print(dict_num1.keys()) #<class 'dict_keys'>
# print(dict_num1.values()) #<class 'dict_values'>
#
# print(type(dict_num1.keys()))
# print(type(dict_num1.values()))
#
# keys = list(dict_num1.keys())
# values = list(dict_num1.values())
#
# print(keys[1])
# print(values[2])
#
#
# '''
# 1) 딕셔너리 요소의 추가와 삭제
# '''
# dict_num1["직업"] = "코리아it아카데미 파이썬 강사"
# print(dict_num1)
# dict_num1["직업"] = "코리아it아카데미 웹개발 강사"
# print(dict_num1)
# #key 하나당 value 하나
# dict_num1.pop("직업") #key를 정확하게 입력해야 삭제 가능
# print(dict_num1) #key를  삭제하면 value도 함께 날아감

'''
응용 예제

list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소부터 7번째 요소만 추출한 결과, 그리고 
그 list에서 2번째 요소를 출력하는 프로그램 작성

실행 예
3번째 요소로부터 7번째 요소 = [30, 40, 50, 60, 70]
3번째 요소로부터 7번째 요소 중 2번째 요소 = 40
'''


# list_origin = [10, 20, 30, 40, 50, 60, 70, 80,90, 100]
# print(f"3번째 요소로부터 7번째 요소 = {list_origin[2:7:1]}")
# print(f"3번째 요소로부터 7번째 요소 중 2번째 요소 = {list_origin[2:7:1][1]}")
#
# list_sliced = list_origin[2:7:1]
# print(f"3번째 요소로부터 7번째 요소 = {list_sliced}")
# print(f"3번째 요소로부터 7번째 요소 중 2번째 요소 = {list_sliced[1]}")

'''
사용자로부터 1에서 12사이의 월을 입력 받아, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하시오
윤년은 고려하지 않음
1~12 사이의 월을 입력하세요 >>> 2
2월은 28일까지입니다.
'''

# month = input("1~12 사이의 월을 입력하세요. >>>")
# month_int = int(month)
# last_dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# print(f"{month_int}월은(는) {last_dates[month_int-1]}일까지 있습니다.")



# last_date_dict = {
#     "1" : 31,
#     "2" : 28,
#     "3" : 31,
#     "4" : 30,
#     "5" : 31,
#     "6" : 30,
#     "7" : 31,
#     "8" : 31,
#     "9" : 30,
#     "10" : 31,
#     "11" : 30,
#     "12" : 31,
# }
# print(f"{month}월은 {last_date_dict[month]}일까지 있습니다.")

# month = input("1~12 사이의 월을 입력하세요. >>>")
# month_int = int(month)
#
# last_dates_short = [28, 30, 31]
# if month_int == 2:
#     last_date = last_dates_short[0]
#     print(f"{month_int}월은 {last_dates_short[0]}일까지 있습니다.")
# elif month_int == 4 or month_int ==6 or month_int == 9 or month_int == 11:
#     last_date = last_dates_short[1]
# elif month_int in (1, 3, 5, 7, 8, 10, 12):
#     last_date = last_dates_short[2]
# else:
#     print("잘못입력하셨습니다.")
#     last_date = "x"
# print(f"{month_int}월은 {last_date}일까지 있습니다.")

# list_num5 = [1, 1, 2, 2, 3, 3, 3]
# print(list_num5)
# set_num5 = set(list_num5)
#
# print(set_num5)
# list_num6 = list(set_num5)
# print(list_num6)

'''
3. set
수학의 집합 개념을 구현한 자료형. list와의 차이점은 순서가 없기 때문에(비스퀀스) 인덱스 및 슬라이싱 사용이 불가능.
중복된 값의 저장이 불가능

이를 활용하여 중복 제거용으로 사용하는 경우와, 교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우 사용

set를 사용하기 위해서는 중괄호({})를 사용함
'''
'''
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 함
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장함
학생을 3명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오.

실행 예

희망하는 수학여행지를 입력하세요. >>>
희망하는 수학여행지를 입력하세요. >>> 제주
희망하는 수학여행지를 입력하세요. >>> 제주
희망하는 수학여행지를 입력하세요. >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.

'''


# trip1 = input("희망하는 수학 여행지를 입력하세요. >>>")
# trip2 = input("희망하는 수학 여행지를 입력하세요. >>>")
# trip3 = input("희망하는 수학 여행지를 입력하세요. >>>")
# trip_list = [trip1, trip2, trip3]
# trip_set = set(trip_list)
# print(f"조사된 수학 여행지는 {trip_set}입니다.")


# field_trip_list = []
# field_trip_set = set({})
#
# for i in range(3):
#     student = input("희망하는 수학 여행지를 입력하세요. >>>")
#     field_trip_list.append(student)
#
# field_trip_set = set(field_trip_list)
#
# print(f"조사된 수학 여행지는 {field_trip_set}입니다.")

'''
짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력 받고, 그 정수만큼 숫자를 입력 받아 list에 저장
이후 저장된 숫자 중 짝수만 새로운 list에 저장하여 출력하는 프로그램을 작성

몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>>
2번째 숫자를 입력하세요 >>>
3번째 숫자를 입력하세요 >>>
4번째 숫자를 입력하세요 >>>
5번째 숫자를 입력하세요 >>>
입력받은 숫자들 중 짝수는 [10, 20, 30]입니다.

'''

# li_original = []
# list_even = []
#
#
# n = input("몇 개의 숫자를 입력할까요? >>>")
# for i in range(int(n)):
#     print(f"{"n"}번째 숫자를 입력하세요. >>>")


# li_original = []
# li_even = []
# index_num = int(input("몇 개의 숫자를 입력할까요? >>>"))
#
# for i in range(index_num):
#     num = int(input(f"{i+1}번째 숫자를 입력하세요. >>>"))
#     li_original.append(num)
#
#
# print(f"입력 받은 숫자는 {li_original}")
#
#
# for num in li_original:
#     if num % 2 == 0:
#         li_even.append(num)
#
# print(f"입력 받은 숫자들 중 짝수는 {li_even}")

# li_original2 = []
# li_even2 = []
# for i in range(int(input("몇 개의 숫자를 입력하시겠습니까? >>>"))):
#     num2 = int(input(f"{i+1}번째 숫자를 입력하세요. >>>"))
#     li_original2.append(num2)
#     if num2 % 2 == 0:
#         li_even2.append(num2)
#
# print(f"입력 받은 숫자는 {li_original2}")
# print(f"입력 받은 숫자들 중 짝수는 {li_even2}")


'''
딕셔너리 기반의 연락처 관리

사용자로부터 3명의 이름과 전화번호를 입력받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는 프로그램

실행 예
1번째 사람의 이름을 입력하세요. >>> 김일
1번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2번째 사람의 이름을 입력하세요. >>> 김이
2번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3번째 사람의 이름을 입력하세요. >>> 김삼
3번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 {'김일':'010-1234-5678', '김이':'010-2345-6789', '김삼':'010-3456-7890')
'''

# telephones = {}
# for i in range(3):
#     dict_key = input(f"{i+1}번째 사람의 이름을 입력하세요. >>>")
#     dict_value = input(f"{i+1}번째 사람의 연락처를 입력하세요. >>>")
#
#     telephones[dict_key] = dict_value
#
# print(f"입력받은 연락처는 {telephones}입니다.")

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 리스트 list01을 선언하고 그 안에 입력받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers(last_num)
print(add_numbers(last_num))

실행 예
숫자 몇까지 입력하시겠습니까? >>> 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

# list01 = []
# #함수 정의
# def add_numbers(n):
#     for i in range(n):
#         list01.append(i+1)
#     print(list01)
#
#
# #함수호출
# last_num = int(input("숫자 몇 까지 입력하시겠습니까? >>>"))
# add_numbers(last_num)

'''
짝수와 홀수 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성

함수 정의
함수 이름 : count_even_odd
매개변수 : list numbers(요소는 모두 정수)

함수 호출
count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개

count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

'''

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"짝수의 개수 : {even_count}\n 홀수의 개수 : {odd_count}")

count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])








































