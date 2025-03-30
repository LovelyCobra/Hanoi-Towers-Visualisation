import os, time

tlc = "┌"  #Top Left Corner
trc = "┐"  #Top Right Corner
blc = "└"  #Bottom Left Corner
brc = "┘"  # Bottom Right Corner
hl = "─"    #Horizontal Line
vl = "│"    #Vertical Line
st = "┬"   # Straight T-shape
rt = "┴"    #Reverse T-shape

#Helper function for generating strings representing lines that make up each tower with or without discs
def disc_print(disc, above, posit, num):
    section_width = num * 2 + 4
    
    #the first empty line
    if posit == 1:
        if disc == 0:
            first_line = section_width * " "
        else:
            side_len = int((section_width / 2 - disc - 1))
            first_line = side_len * " " + tlc + disc * 2 * hl + trc + side_len * " "
        return first_line
    
    #the second empty line
    elif posit == 2:
        if disc == 0 and above == 0:
            second_line = section_width * " "
        elif disc != 0 and above == 0:
            side_len = int((section_width / 2 - disc - 1))
            second_line = side_len * " " + tlc + disc * 2 * hl + trc + side_len * " "
        else:
            side_len = int((section_width / 2 - above - 1))
            second_line = side_len * " " + blc + above * 2 * hl + brc + side_len * " "
        return second_line
    
    #the top of a rod
    elif posit == 3:
        if disc == 0 and above == 0:
            side_len = int((section_width - 2) / 2)
            rod_top = side_len * " " + tlc + trc + side_len * " "
        elif disc != 0:
            side_len = int((section_width / 2 - disc - 1))
            rod_top = side_len * " " + tlc + disc * 2 * hl + trc + side_len * " "
        else:
            side_len = int((section_width / 2 - above - 1))
            diff = above - disc - 1
            rod_top = side_len * " " + blc + diff * hl + st + 2 * disc * hl + st + diff * hl + brc + side_len * " "
        return rod_top
    
    #a rod section
    elif above == 0 and disc == 0:
        side_len = int((section_width - 2) / 2)
        rod_section = side_len * " " + 2 * vl + side_len * " "
        return rod_section
    
    # any disc lying on the top of a larger disc
    elif disc > 0:
        side_len = int((section_width / 2 - disc - 1))
        diff = disc - above - 1
        d = side_len * " " + tlc + diff * hl + rt + 2 * above * hl + rt + diff * hl + trc + side_len * " "
        return d
    
    # a rod section below an ascending or descending disc
    elif disc == 0 and  above != 0:
        side_len = int((section_width / 2 - above - 1))
        diff = above - disc - 1
        d = side_len * " " + blc + diff * hl + st + 2 * disc * hl + st + diff * hl + brc + side_len * " "
        return d
    
    #the last line, the ground     
    else:
        side_len = int((section_width / 2 - above - 1))
        ground = side_len * hl + rt + 2 * above * hl + rt + side_len * hl
        return ground
    
    
#The main printing function
def three_towers_print(s, t, a, wh):
    n = len(s) - 1
    if wh is False:
        for row in range(3, n):
            line = disc_print(s[row], s[row - 1], row, n) + disc_print(a[row], a[row - 1], row, n) + disc_print(t[row], t[row - 1], row, n)
            print(line)        
        ground = disc_print(-1, s[n-1], 0, n) + disc_print(-1, a[n-1], 0, n) + disc_print(-1, t[n-1], 0, n)
        print(ground)
        
    else:
        for row in range(1, n ):
            line = disc_print(s[row], s[row - 1], row, n) + disc_print(a[row], a[row - 1], row, n) + disc_print(t[row], t[row - 1], row, n)
            print(line)
        ground = disc_print(-1, s[n-1], 0, n) + disc_print(-1, a[n-1], 0, n) + disc_print(-1, t[n-1], 0, n)
        print(ground)
        

#The horizontal movement between towers
def horizon_move(move, A, C, B, num, mc, pause):
    
    first_line = "    " + disc_print(A[1], A[0], 1, num) + "        " + disc_print(B[1], B[0], 1, num) + "        " + disc_print(C[1], C[0], 1, num) + "    "
    second_line = "    " + disc_print(A[2], A[1], 2, num) + "        " + disc_print(B[2], B[1], 2, num) + "        " + disc_print(C[2], C[1], 2, num) + "    "
    
    #Line length
    ll = len(first_line)
    
    #Last index
    li = len(move[0]) - 1
    
    #Section Width
    #5 discs sw = 7; 6 == 8; 4 = 6
    sw = num + 2
    
    if [move[0][li], move[1][li]] == ["A", "B"] or [move[0][li], move[1][li]] == ["B", "C"]:
        for pos in range(sw):
            first_line = "   " + first_line[:ll - 3]
            second_line = "   " + second_line[:ll - 3]
            os.system('cls' if os.name == 'nt' else 'clear')
            print(first_line)
            print(second_line)
            three_towers_print(A, C, B, False)
            print(f"\nMOVE COUNT: {mc}")
            time.sleep(pause / 5)

    elif [move[0][li], move[1][li]] == ["A", "C"]:
        for pos in range(2 * sw):
            first_line = "   " + first_line[:ll - 3]
            second_line = "   " + second_line[:ll - 3]
            os.system('cls' if os.name == 'nt' else 'clear')
            print(first_line)
            print(second_line)
            three_towers_print(A, C, B, False)
            print(f"\nMOVE COUNT: {mc}")
            time.sleep(pause / 5)
    
    elif [move[0][li], move[1][li]] == ["C", "B"] or [move[0][li], move[1][li]] == ["B", "A"]:
        for pos in range(sw):
            first_line = first_line[3:ll] + "   "
            second_line = second_line[3:ll] + "   "
            os.system('cls' if os.name == 'nt' else 'clear')
            print(first_line)
            print(second_line)
            three_towers_print(A, C, B, False)
            print(f"\nMOVE COUNT: {mc}")
            time.sleep(pause / 5)
			
    elif [move[0][li], move[1][li]] == ["C", "A"]:
        for pos in range(2 * sw):
            first_line = first_line[3:ll] + "   "
            second_line = second_line[3:ll] + "   "
            os.system('cls' if os.name == 'nt' else 'clear')
            print(first_line)
            print(second_line)
            three_towers_print(A, C, B, False)
            print(f"\nMOVE COUNT: {mc}")
            time.sleep(pause / 5)
    

if __name__ == '__main__':
    pass
    