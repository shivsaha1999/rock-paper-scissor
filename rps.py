import random
import math 

def is_win(player1, player2):
     if(player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r'):
         return True 
     return False

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper. 's' for scissors \n")
    user=user.lower()
    
    pc = random.choice(['r', 'p', 's'])
    
    # tie
    if (pc==user):
       return (0, user, pc)
   
   # r>s, s>p, p>rrs
    if is_win(user,pc):
        return (1, user, pc)
    
    else:
        return (-1, user, pc)
    
    
def best_of(n):
    # To win the condition should be ceil(n/2) games (ie 2/3, 3/5, 4/7)
    user_wins = 0
    pc_wins = 0
    wins_need = math.ceil(n/2)
    
    while user_wins<wins_need and pc_wins<wins_need:
        result, user, pc =play()
        
        #tie
        if result==0:
            print ("It's a TIE. You and the computer have both chosen {}.\n".format(user))
            
        # user won
        elif result==1:
            user_wins+user_wins+1
            print ("You WON!!! You chose {} and the computer chose {}.\n".format(user,pc))
          
        # pc wins    
        else:
            pc_wins=pc_wins+1
            print ("You LOSE!!! You chose {} and the computer chose {}.\n".format(user,pc))
        print("\n")
        
    if user_wins>pc_wins:
        print("You won the best of {} games!! What a Champ :D".format(n))
    else:
        print("Ohhh NOO!!! The computer has won the best of {} games. Better luck nect time <3".format(n))
    
if __name__=='__main__':
    print("Enter the number maximum plays : ")
    n=int(input())
    print(best_of(n))

