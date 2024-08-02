import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

method_list = [rock, paper, scissors]

def get_user_chocie(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("꼭 다른거 쳐 넣는 저능아들이 있어요, 똑바로 넣으세요 ^^")
        except ValueError:
            print("꼭 다른거 쳐 넣는 저능아들이 있어요, 똑바로 넣으세요 ^^")

rule = get_user_chocie("가위,바위,보 랜덤 게임. 바위 = 0, 가위 = 1, 보 = 2 입니다. 이겨보세요 ㅎㅎ\n안내면 진거, 가위 바위 보!\n")

print("User Choice:")
print(method_list[rule])

AI_choice = random.randint(0, 2)
print("AI Choice:")
print(method_list[AI_choice])

if rule == AI_choice:
    same = int(input("오~ 이걸 비긴다고? 그럼 한판 더 해야지\n안내면 진거, 가위 바위 보!\n"))
    print("User Choice:")
    print(method_list[same])
    print("AI Choice:")
    print(method_list[AI_choice])
    if same == 0 and AI_choice == 1:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif same == 1 and AI_choice == 2:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif same == 2 and AI_choice == 0:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif same == 0 and AI_choice == 2:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    elif same == 1 and AI_choice == 0:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    elif same == 2 and AI_choice == 1:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    else:
        print("이걸 또 비긴다고? 넌 AI에게 패배했다, 실력 더 키우고 오셈 ㅅㄱ")

elif rule == 0 and AI_choice == 1:
    win = int(input("와 이기셨네요, 축하드립니다. 그럼 한판 더 해야겠죠?\n안내면 진거, 가위 바위 보!\n"))
    print("User Choice:")
    print(method_list[win])
    print("AI Choice:")
    print(method_list[AI_choice])
    if win == 0 and AI_choice == 1:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win == 1 and AI_choice == 2:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win == 2 and AI_choice == 0:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win == 0 and AI_choice == 2:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    elif win == 1 and AI_choice == 0:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    elif win == 2 and AI_choice == 1:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    else:
        print("이걸 비긴다고? 넌 AI에게 패배했다, 실력 더 키우고 오셈 ㅅㄱ")

elif rule == 1 and AI_choice == 2:
    win1 = int(input("와 이기셨네요, 축하드립니다. 그럼 한판 더 해야겠죠?\n안내면 진거, 가위 바위 보!\n"))
    print("User Choice:")
    print(method_list[win1])
    print("AI Choice:")
    print(method_list[AI_choice])
    if win1 == 0 and AI_choice == 1:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win1 == 1 and AI_choice == 2:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win1 == 2 and AI_choice == 0:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win1 == 0 and AI_choice == 2:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    elif win1 == 1 and AI_choice == 0:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    elif win1 == 2 and AI_choice == 1:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    else:
        print("이걸 비긴다고? 넌 AI에게 패배했다, 실력 더 키우고 오셈 ㅅㄱ")

elif rule == 2 and AI_choice == 0:
    win2 = int(input("와 이기셨네요, 축하드립니다. 그럼 한판 더 해야겠죠?\n안내면 진거, 가위 바위 보!\n"))
    print("User Choice:")
    print(method_list[win2])
    print("AI Choice:")
    print(method_list[AI_choice])
    if win2 == 0 and AI_choice == 1:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win2 == 1 and AI_choice == 2:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win2 == 2 and AI_choice == 0:
        print("ㅊㅊ 이걸 이기네, 휴먼 실력 괜찮누~\nGG")
    elif win2 == 0 and AI_choice == 2:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    elif win2 == 1 and AI_choice == 0:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    elif win2 == 2 and AI_choice == 1:
        print("와 개못하노 ㅋㅋㅋㅋㅋㅋㅋ, 넌 나가라~")
    else:
        print("이걸 비긴다고? 넌 AI에게 패배했다, 실력 더 키우고 오셈 ㅅㄱ")

elif rule == 0 and AI_choice == 2:
    print("와, 이걸 한번에 지네 ㅉㅉ 넌 안되겠다, 나가라~")
elif rule == 1 and AI_choice == 0:
    print("와, 이걸 한번에 지네 ㅉㅉ 넌 안되겠다, 나가라~")
elif rule == 2 and AI_choice == 1:
    print("와, 이걸 한번에 지네 ㅉㅉ 넌 안되겠다, 나가라~")