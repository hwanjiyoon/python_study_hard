'''
condition 조건
1. if문
if문은 조건이 참(True)일 때만 해당 블록의 코드를 실행
'''
#age = 20
#if age >= 19:
#print("성인입니다.") #if와 함께있는 조건문이 True일 때만 라인이 실행됨.

'''
if문에서 주의할 점:
1) if와 같은 라인에 작성된 코드는 True/False으로 구분할 수 있어야함.
2) if와 같은 라인에 있는 조건문이 끝났을 때 콜론(:)으로 마무리.
3) python에서는 타 언어들과 달리 들여쓰기가 매우 중요.

if-else문 : if문 다음에 else 사용, if가 참일 때 실행된다면, else는 거짓일 때 실행됨.
'''
#if age >= 19:
    #print("성인입니다.")
#else:
    #print("미성년자입니다.")

'''
19는 if절에, 21은 else에 종속.

if-else는 서로 반대이기 때문에 else절에서는 굳이 조건식을 명시하지 않는다.

if-elif-else문
    여러 조건을 동시에 검사하기 위해서 사용하는 구조
'''

#age = 14
#if age >= 19:
    #print("성인입니다.")
#elif age >= 10:
    #print("학생입니다.")
#else:
    #print("미취학아동입니다.")


'''
1)첫번째 조건은 False
2)두번째 조건은 True
3)이후 조건은 확인하지 않고 조건문 전체 종료

if 조건식1:
    실행문1
(elif 조건식2:)
    (실행문2)
(elif 조건식3:)
    (실행문3)
(else:)
    (실행문4)
    
중첩 if문(Nested if)
    조건문 내부에 또 다른 조건문을 사용할 수 있음. 다만 가독성이 떨어지는 편이어서 추후에 배우는 논리 연산자와 함께 사용   
'''

#if age >= 19:
    #if has_ticket:
        #print("영화관 입장이 가능합니다.")
    #else:
        #print("티켓을 구매하세요")
#else:
    #print("미성년자는 출입할 수 없습니다.")

'''
조건문에서 자주 쓰이는 연산자
비교 연산자 :
1)== : 같다
2) != : 같지 않다
3) > : 초과
4) < : 미만
5) >= : 이상
6) <= : 이하

논리 연산자 :
    1)and : A and B > A와 B 모두 참일 때 실행문 실행
    2)or : A or B > A또는 B 중 하나가 참이면 실행문 실행
    3)not : if not A > A가 False일 때 실행문 실행
'''








