board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = {1:[],2:[]}
create = []
flag = True
k = 0

#TRY: 1,7,4,9,8,3,5,6  and   1,2,3,4,5

def display(board_print) :
    for i in range(0,len(board_print),3):
        print("{} | {} | {}".format(board_print[i],board_print[i+1],board_print[i+2]))
        print("----------")

def board_logic():
    global board,k
    player_list1 = player[1]
    player_list2 = player[2]
    print(player_list1)
    print(player_list2)
    while k<2:
        print("This is k: {}".format(k))
        if flag:
            if (player_list1[k+1]+player_list1[k]+player_list1[k+2])==15 or (player_list1[k+1]+player_list1[k]+player_list1[k+2])%6==0:
                print("Player {} wins!".format(1))
                exit(1)
            else:
                print("1st else")
                k +=1
                return None            
        elif not flag:
            if (player_list2[k+1]+player_list2[k]+player_list2[k+2])==15 or (player_list2[k+1]+player_list2[k]+player_list2[k+2])%6==0:
                print("Player {} wins!".format(2))
                exit(1)
            else:
                print("2nd else")
                k +=1
                return None
    

def user_input():
    global board
    check = True
    while check:
        temp = input("Player 1 choose: x/o\n").upper()
        if temp=='X' and temp.isalpha():
            create = [temp,'O']
            check = False
        elif temp=='O' and temp.isalpha():
            create = [temp,'X']
            check = False
        else:
            print("Please enter either 'x' or 'o'")
            check = True
    print(create)
    
    game = True
    player_number = 2
    check_input = set()

    for i in range(0,9):
        global k,flag
        player_number = 3-player_number
        if player_number==1:
            flag = True
        elif player_number==2:
            flag = False
        game = True
        while game:
            temp = input("Player {} choose a number from 1 to 9:\n".format(player_number))
            if temp.isdigit():
                if  int(temp) in range(1,10) and temp not in check_input:
                    game = False
                elif temp:
                    print("Wrong input, choose correctly!")
            else:
                print("Invalid input, only numbers allowed!")
        board[int(temp)-1] = create[player_number-1]
        player[player_number].append(int(temp))
        check_input.add(temp)
        display(board)
        if i>=4:
            board_logic()

def main():
    user_input()
    board_logic()
    
if __name__ == '__main__':
    main()