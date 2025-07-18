board=[[' ',' ',' ',],[' ',' ',' ',],[' ',' ',' ',]]
def display():
    print(game_list[0][0],game_list[0][1],game_list[0][2])
    print(game_list[1][0],game_list[1][1],game_list[1][2])
    print(game_list[2][0],game_list[2][1],game_list[2][2])

display()
def selectXorO():
    a='wrong'
    while a not in ['X','O']:
        a=input("Player one X or O:")
        if a not in ['X','O']:
            print("Select either X or O only")
    if a=='X':
        a1='X'
        print(f"Player-1 has opted {a} Player-2 gets O")
    else:
        a2='O'
        print(f"Player-1 has opted {a} Player-2 gets X")
selectXorO()       
def getanswerplayer1():
    print("Player-1 your chance:")
    print("Enter the position u want to enter the row and column")
    rpos1='wrong'
    cpos1='wrong'
    while rpos1 and cpos1 not in [0,1,2]:
        rpos1=int(input())
        cpos1=int(input())
        if rpos1 and cpos1 not in [0,1,2]:
            print("Please enter valid literals")
    board[rpos1][cpos1]=a1
def getanswerplayer2():
    print("Player-1 your chance:")
    print("Enter the position u want to enter the row and column")
    rpos2='wrong'
    cpos2='wrong'
    while rpos2 and cpos2 not in [0,1,2]:
        rpos2=int(input())
        cpos2=int(input())
        if rpos2 and cpos2 not in [0,1,2]:
            print("Please enter valid literals")
    board[rpos2][cpos2]=a2

def checkwin():
    
        
    