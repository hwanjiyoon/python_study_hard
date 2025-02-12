logo = '''

___.          .__          __
\_ |__ _____  |  |   ____ |  | __
 | __ \\__  \ |  | _/ ___\|  |/ /
 | \_\ \/ __ \|  |_\  \___|    <
 |___  (____  /____/\___  >__|_ \
     \/     \/          \/     \/
'''
print(logo)

color = input("지금 입은 하의 색깔은 무엇입니까? >>> ")
last_food = input("마지막으로 먹은 음식은 무엇입니까? >>> ")
band_name = color + " " + last_food
#print(f"당신의 밴드 이름은 {band_name} 입니다.")
print(f"당신의 밴드 이름은 {color} {last_food} 입니다.")
