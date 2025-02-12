'''
체질량지수는 몸무게를 키의 제곱으로 나눈 값
18.5 / 23 / 25
bmi_calc를 만들기 위한 사전 준비
'''

#age=input("당신의 나이는 몇 살입니까?")
#print(type(age))
#print(f"당신은 내년에 {age+1}살이 됩니다.")
#문자열과 숫자열이 연산이 되지 않음

'''
input() 함수의 겨로가값은 언제나 str > 즉, 수학 연산을 하기 위해서는 별도의 과정이 필요함
이때 필요한 함수가 '형변환 함수'임 (conversion)
'''
#age1=input("당신의 나이는 몇 살입니까?")
#print(type(age1)) #결과값 : str
#age1_int = int(age1) #str인 age1을 int로 자료형을 변환시켜서 age1_int라는 새로운 변수에 대입

#print(type(age1_int))
#print(f"당신의 내년에 {age1_int+1}살이 됩니다.")

'''
자주 쓰이는 형변환 함수
1. int() > str 또는 float을 int 로 변경
2. float() > str 또는 int를 float으로 변경
'''

# temp = int(3.8)
# print(temp)
# temp2 = float(4)
# print(temp2)
#temp3 = round(3.8)
#print(temp3)
#temp4 = round(5.3491285, 2) #괄호 첫번째 수를 소수점 2째자리까지 표기
#print(temp4)

'''
bmi 계산기를 작성
1. 키를 입력 받아 > input 함수 변수 height 저장
2. 몸무게를 입력 받아 변수 wieght에 저장
3. 몸무게 / 키의 제곱 을 계산하면 bmi 지수가 나옵니다.
4. bmi 지수를 int로 출력 > int함수 사용
5. bmi 지수를 소수점 셋째자리에서 반올림하여 둘째자리까지 출력 > round 함수 사용

로고 출력 (text to ascii art 검색)
당신의 키는 몇 cm입니까? >>> 173.2
당신의 몸무게는 몇 kg입니까? >>> 70
당신의 bmi 지수는 23 and 23.xx
'''

logo='''
 _______  __   __  ___     _______  _______  ___      _______ 
|  _    ||  |_|  ||   |   |       ||   _   ||   |    |       |
| |_|   ||       ||   |   |       ||  |_|  ||   |    |       |
|       ||       ||   |   |       ||       ||   |    |       |
|  _   | |       ||   |   |      _||       ||   |___ |      _|
| |_|   || ||_|| ||   |   |     |_ |   _   ||       ||     |_ 
|_______||_|   |_||___|   |_______||__| |__||_______||_______|
'''
#print(logo)
#height = input("당신의 키는 몇 cm입니까? >>>")
#weight = input("당신의 몸무게는 몇 kg입니까? >>>")
#height = float(height)
#weight = float(weight)
#height_m = height/100
#bmi = weight/height_m**2
#bmi_round = round(bmi, 2)
#print(f"당신의 bmi 지수는 {bmi}입니다.")
#print(f"당신의 bmi 지수는 {bmi_round}입니다.")













