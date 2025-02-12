import random

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
# print(chosen_word)

#todo - 1 : 비어있는 list인 display를 만드시오.
# chosen_word의 각 문자 개수마다 "_"를 추가하시오.

display = []
# for i in range(len(chosen_word)):   #변수가 사용되지 않으므로 i가 아니라 _로 명시함.
#     display.append("_")

for letter in chosen_word:
    display.append("_")

# print(display)

#todo - 2 : chosen_word의 각 문자들을 반복시키세요.
# 만약 그 위치의 문자가 guess와 일치하면, 해당 위치의 display에서 해당 문자를
# 공개하세요. ex) "p"를 입력했고, chosen_word가 "apple"이라면 display = ['_', 'p', 'p', '_', '_']로 바뀌어야함


guess = input("알파벳 입력하세요. >>>").lower()
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess
    #else는 안써도 됨 > 틀리면 지시 사항이 없음
print(display)


display[1] = guess
display[2] = guess

