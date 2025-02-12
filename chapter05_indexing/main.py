'''
indexing
문자열 indexing
index? '문자열'을 구성하는 모든 요소에 부여한 고유한 번호
시작 번호는 0
1234
'''

'''
[]를 사용하여 index number 부여
마이너스 index : 문자열의 뒤에서부터 부여하는 번호, 마지막 문자의 imdex -1
'''

'''
문자열 슬라이싱(slicing) : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용하는 방법
추출하고자 한 단어나 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이 문자들을 추출하는 방법

형식 : a[시작인덱스 : 종료인덱스 : 증감값]

시작인덱스 : 생략하면 처음부터 추출
종료인덱스 : 생략하면 끝가지 추출
증감값 : 생략하면 1씩 변화(인덱스 넘버가 1씩 증가, 0, 1, 2, 3...)
'''

name = jihwan
print(name[:2:]) #종료인덱스의 앞까지만 추출

'''
기본 예제
네 자리 숫자를 입력 받아 그 숫자의 맨 마지막 자리를 출력하시오.

네 자리 숫자를 입력하세요>>> 2025
맨 마지막 숫자는 5입니다.
마지막 숫자는 5이며, 홀수입니다.
'''

# num = input("네 자리 숫자를 입력하세요 >>> ")

#형 변환을 조건문에 삽입해서 그대로 사용
# if int(num[3])%2 == 0:
#     print (f"마지막 숫자는 {num[3]}이며, 짝수입니다.")
# else:
#     print (f"마지막 숫자는 {num[3]}이며, 홀수입니다.")

#변수를 선언하여 활용한 사례
# last_num = int(num[3])

# if last_num%2 == 0:
#     even _ood = "짝수"
# else:
#     even_ood = "홀수"
# print(f"맨 마지막 숫자는 {last_num}이며, {even_ood}입니다.")

'''
응용 예제

미세먼지 저감 활동의 일환으로 차량 2부제를 실시하고자 합니다. 사용자로부터 차량 번호를 입력받아
짝수로 끝나면 운행가능 아니면 운행불가가 출력되는 프로그램을 작성하시오
단 차량 번호는 237가 1234와 같은 형식으로 입력받는다고 가정합니다.

차량번호를 입력하세요 >>> 237가1234
차량번호 237가1234는 오늘 운행 가능입니다.
'''

# num = input("차량 번호를 입력하세요 >>>")
# last_num = int(num[-1])
# if last_num%2 == 0:
#     print(f"차량번호 {num}은(는) 오늘 운행 가능입니다.")
# else:
#     print(f"차량번호 {num}은(는) 오늘 운행 불가입니다.")








