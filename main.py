def game():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    a1 = ''
    a2 = ''

    def display():
        print("\n   0   1   2")
        for i in range(3):
            print(i, ' | '.join(board[i]))
            if i < 2:
                print("  ------------")
        print()

    def selectXorO():
        nonlocal_a1 = ''
        nonlocal_a2 = ''
        a = 'wrong'
        while a not in ['X', 'O']:
            a = input("Player 1, choose X or O: ").upper()
            if a not in ['X', 'O']:
                print("Invalid choice. Please choose X or O.")
        if a == 'X':
            nonlocal_a1, nonlocal_a2 = 'X', 'O'
        else:
            nonlocal_a1, nonlocal_a2 = 'O', 'X'
        print(f"Player 1 is '{nonlocal_a1}', Player 2 is '{nonlocal_a2}'")
        return nonlocal_a1, nonlocal_a2

    def get_move_player1():
        while True:
            try:
                print(f"Player 1's turn ({a1})")
                r = int(input("Enter row (0-2): "))
                c = int(input("Enter column (0-2): "))
                if r not in [0,1,2] or c not in [0,1,2]:
                    print("Invalid position.")
                    continue
                if board[r][c] != ' ':
                    print("Spot already taken.")
                    continue
                board[r][c] = a1
                break
            except:
                print("Enter valid numbers.")

    def get_move_player2():
        while True:
            try:
                print(f"Player 2's turn ({a2})")
                r = int(input("Enter row (0-2): "))
                c = int(input("Enter column (0-2): "))
                if r not in [0,1,2] or c not in [0,1,2]:
                    print("Invalid position.")
                    continue
                if board[r][c] != ' ':
                    print("Spot already taken.")
                    continue
                board[r][c] = a2
                break
            except:
                print("Enter valid numbers.")

    def check_winner():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]
        for row in board:
            if ' ' in row:
                return None
        return 'Draw'

    a1, a2 = selectXorO()
    display()

    while True:
        get_move_player1()
        display()
        result = check_winner()
        if result:
            if result == 'Draw':
                print("It's a draw!")
            elif result == a1:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            break

        get_move_player2()
        display()
        result = check_winner()
        if result:
            if result == 'Draw':
                print("It's a draw!")
            elif result == a1:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            break
game()
