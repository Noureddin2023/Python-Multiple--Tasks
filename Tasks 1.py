# 1 : Create a math game using Python:
    # a- Start Game: Welcome Massage ---> all games
    # b- Enter Game Number
    # c- Start Game [User]
    # d- Play again
    # Y : Play again
    # N : Exit



class Game:
    def __init__(self):
        while True:

            print('''
       Welcome To our Game:
       1 : Multiplication Table Game
       2 : Remove Duplicates Game
       3 : Divided Numbers Game
       4 : To Exit
       ''')

            user_choice = int(input('Enter Game Number:'))
            if user_choice > 4:
               
