import os, time
import han_print as hp
from cobraprint import *

moves_list = []

#The main recursive function that generates the list of moves solving the Towers of Hanoi puzzle with the number of discs equal num

def hanoi_towers(num, source, target, aux):
    
    if num == 1:
        moves_list.append([source, target])
        
    else:
        hanoi_towers(num - 1, source, aux, target)
        moves_list.append([source, target])
        hanoi_towers(num - 1, aux, target, source)



#The animation function that animates the movement of the discs using the above list of moves as a template
        
def animation(pause):
        move_count = 0
        
        # Generating representation of the 3 towers as 3 lists A, B a C where discs are represented as integers 1, 2, 3 etc (values corresponding to the discs' sizes) 
        # and number 0 represents either empty rod or 3 spaces above it.
        
        A = [0, 0, 0]
        A.extend([i for i in range(num + 1)])
        A.append("A")
        B = [0, 0, 0]
        B.extend([0 for i in range(num + 1)])
        B.append("B")
        C = [0, 0, 0]
        C.extend([0 for i in range(num + 1)])
        C.append("C")
        
        #Generating the list of moves solving the puzzle for 'num' discs
        hanoi_towers(num, A, C, B)
        
        #Showing the initial state
        os.system('cls' if os.name == 'nt' else 'clear')
        hp.three_towers_print(A, C, B, True)
        print(f"\nNumber of discs: {num}")
        time.sleep(1.5)
        
        l = len(A) - 1

        #The loop going throught all the moves
        for move in moves_list:
            move_count += 1
            
            #The movement of the top disc upwards
            for i in range(l):
                if move[0][i] != 0:
                    n = i
                    break
            while n > 1:
                    move[0][n - 1] = move[0][n]
                    move[0][n] = 0
                    os.system('cls' if os.name == 'nt' else 'clear')
                    hp.three_towers_print(A, C, B, True)
                    print(f"\nMOVE COUNT: \033[94m{move_count}\033[0m\n")
                    time.sleep(pause)
                    n -= 1
                   
                    
            
            #The movement of the disc horizontally
            hp.horizon_move(move, A, C, B, num, move_count, pause)
            
            move[1][1] = move[0][1]
            move[0][1] = 0

            #The movement of the disc downwards            
            for i in range(2, l):
                if move[1][i] != 0:
                    n = i
                    break
                else:
                    n = l
            for j in range(1, n - 1):
                move[1][j + 1] = move[1][j]
                move[1][j] = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                hp.three_towers_print(A, C, B, True)
                print(f"\nMOVE COUNT: \033[94m{move_count}\033[0m\n")
                time.sleep(pause)
                
        
        
if __name__ == '__main__':
    
    clear
    n = input("\nHow many discs would you like to move?\n")
    num = int(n)
    pause = 0.07
    
    animation(pause)
    
