'''
주어진 해가 윤년인지 아닌지 계산하는 프로그램을 작성
일반적으로 1년은 365일이고, 윤년은 366일로 2월에 하루가 더 있음
다음은 특정 연도가 윤년인지 확인하는 방법입니다.
1. 4로 나누어 떨어지는 해는 윤년
2. 그러나, 100으로 나누어 떨어지는 해는 윤년이 아닙니다.
3. 그런데, 400으로 나누어 떨어지는 해는 윤년입니다.

ex)
2000 / 4 = 500 이라서 윤년
2000 / 100 = 이라서 윤년 아님
2000 / 400 = 5 라서

최종적으로 2000년은 윤년에 해당

2100 / 4 = 525 이라서 윤년
2100 / 100 = 21 이라서 윤년 아님
2100 / 400 = 5.25 이라서 윤년 아님

실행

윤년인지 확인하고 싶은 연도를 입력하세요 >>> 2200년
2200년은 윤년이 아닙니다.

윤년인지 확인하고 싶은 연도를 입력하세요 >>> 2000년
2000년은 윤년입니다.
'''

# year = int(input("윤년인지 확인하고 싶은 연도를 입력하세요 >>> "))
# if year%400 == 0:
#     print(f"{year}은 윤년입니다.")
# elif year%100 == 0:
#     print(f"{year}은 윤년이 아닙니다.")
# elif year%4 == 0:
#     print(f"{year}은 윤년입니다.")
# else:
#     print(f"{year}은 윤년이 아닙니다.")
#
# if year % 4 == 0:
#     if year%400 == 0:
#         print(f"{year}은 윤년입니다.")
#     elif year%100 == 0:
#         print(f"{year}은 윤년이 아닙니다.")
#     else:
#         print(f"{year}은 윤년입니다.")
# else:
#     print(f"{year}은 윤년이 아닙니다.")

# if year%400 == 0 or (year%100 != 0 and year%4 == 0):
#     print(f"{year}은 윤년입니다.")
# else:
#     print(f"{year}은 윤년이 아닙니다.")

'''
1. 크롬에서 사이트 확인하고 bmi가 특정 구간일 때마다
당신의 bmi 지수는 xx.xx이고, 저체중, 정상, 과체중, 비만입니다. 가 출력될 수 있도록 조건문을 작성
'''



