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
             print('Please Enter Number between 1:4')
         
            elif user_choice == 4:
              print('Godbay')
              return
            elif user_choice == 1:
                self.game1()
                
            elif user_choice == 2:
                self.game2()
                
            elif user_choice == 3:
                self.game3()
                
            play_again == input('Press Y to Play again, N to Exit')
            if play_again == 'n':
                print('Goodbye')
                break
            
    def game1(self):
        Start = int(input('Enter Start Number : '))
        End = int(input('Enter End Number : '))
        for x in range(Start,End+1):
             for y in range(1,13):
               print(f'{x}X{y}={x*y}')   
                  
            
    
    def game2(self):
        

    
    def game3(self):
        Start = int(input('Enter Start Number : '))
        End = int(input('Enter End Number : '))
        for x in range(Start,End+1):
             for y in range(1,13):
              print(f'{x}/{y}={x%y}')

G1 = Game() 
              
  
                
           
          
            
       
