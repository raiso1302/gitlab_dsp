#Import appropriate library for random
from random import randint
#create a pole with "đấm, lá, kéo"
decision = {
    '1':'Đấm',
    '2':'Lá',
    '3':'Kéo'
}

#create a rule dictionary, đấm = 1, lá = 2, kéo = 3; computer is added first then player: exp: 13 --> computer đấm, user kéo
rules = {'11':'hoà',
         '22':'hoà',
         '33':'hoà',
         '12':'Máy tính ra đấm, bạn ra lá, bạn thắng, lá thắng đấm',
         '13':'Máy tính ra đấm, bạn ra kéo, bạn thua, kéo thua đấm',
         '21':'Máy tính ra lá, bạn ra đấm, bạn thua, đấm thua lá',
         '23':'Máy tính ra lá, bạn ra kéo, bạn thắng, kéo thắng lá',
         '31':'Máy tính ra kéo, bạn ra đấm, bạn thắng, đấm thắng kéo',
         '32':'Máy tính ra kéo, bạn ra lá, bạn thua, lá thua kéo'}

#creat a function that decide who wins
def who_wins(comp, user):
    result = str(comp) + str(user)
    return rules[result]

#creat a function that get the right input from user:
def get_input():
    user_input = input("please give me your input, or 'q' to quit:\n")
    if user_input == 'q':
        return user_input
    try:
        print("Bạn chọn ra: ", decision[user_input])
        return user_input
    except KeyError:
        print("I need a number from 1,2,3")
        return get_input()

#start the game
stop = False
while stop == False:
    #computer get the random number
    comp = randint(1,3)
    #get the input
    user_choice = get_input()
    if user_choice == 'q':
        stop = True
        print("End game \n")
    else:
        print(who_wins(comp,user_choice))

