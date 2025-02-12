import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(f"테스트 코드 : {chosen_word}")

display = []

end_of_game = False
lives = 6

for letter in chosen_word:
    display.append("_")

while not end_of_game:
    print(stages[lives])
    guess = input("알파벳을 입력하세요. >>>").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            print(display)
        # else:
        #     lives -= 1
        #     print(f"당신의 기회는 {lives}번 남았습니다.")
        #     if lives == 0:
        #         print("모든 기회를 잃었습니다.")
        #         end_of_game = True

    if guess not in chosen_word:
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            end_of_game = True
            print("모든 기회를 잃었습니다.")
    if "_" not in display:
        print("정답입니다.")
        end_of_game = True
        break



    print(" ".join(display))
    print(stages[lives])



#todo - 1 : 남은 목숨 수를 추적하기 위한 'lives'라는 변수를 선언하고, 6으로 초기화하세요.

#todo - 2 : 추측한 알파벳이 chosen_word에 없으면 lives를 1 감소시키세요.
#  lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.

#todo - 3 : display list의 모든 요소를 결합하여 문자열로 변환하세요.

#todo - 4 : 사용자가 모든 문자를 맞췄는지 확인하세요 -> 정답을 맞췄다면 "정답입니다!!:)"를 출력하세요
