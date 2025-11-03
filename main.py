class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play(self, board):
        print(f"{self.name}'s turn.")
        row = int(input("Row: "))
        column = int(input("Column: "))
        while True:
            if row < 1 or row > 3 or column < 1 or column > 3:
                print("Please enter valid numbers. [1, 3]")
                row = int(input("Row: "))
                column = int(input("Column: "))
            elif board.board[row - 1][column - 1] != ' ':
                print("This cell is already taken! Try again.")
                row = int(input("Row: "))
                column = int(input("Column: "))
            else:
                break

        board.board[row - 1][column - 1] = self.symbol        


class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(f" {self.board[i][j]}", end="")
                if j < 2:
                    print(" |", end="")

            if i < 2:
                print("\n-----------")
            else:
                print()

    def check_winning(self):
        # Rows
        if self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2] and self.board[0][0] != ' ':
            return True 
        if self.board[1][0] == self.board[1][1] and self.board[1][0] == self.board[1][2] and self.board[1][0] != ' ':
            return True 
        if self.board[2][0] == self.board[2][1] and self.board[2][0] == self.board[2][2] and self.board[2][0] != ' ':
            return True 

        # Columns
        if self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0] and self.board[0][0] != ' ':
            return True 
        if self.board[0][1] == self.board[1][1] and self.board[0][1] == self.board[2][1] and self.board[0][1] != ' ':
            return True 
        if self.board[0][2] == self.board[1][2] and self.board[0][2] == self.board[2][2] and self.board[0][2] != ' ':
            return True 
        
        # Diagonals
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != ' ':
            return True 
        if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] != ' ':
            return True 


def start_game():
    print("First Player Info.")
    name1 = input("Enter your name: ")
    symbol1 = input("Enter your symbol: ")
    player1 = Player(name1, symbol1)

    print("Second Player Info.")
    name2 = input("Enter your name: ")
    symbol2 = input("Enter your symbol: ")
    player2 = Player(name2, symbol2)

    board = Board()

    turns = 0
    while True:
        board.display_board()
        player1.play(board)
        print("--------------------------")
        if board.check_winning():
            board.display_board()
            print(f"Congrats {player1.name}, you won!")
            break
        
        turns += 1
        if turns == 9:
            print("--------------------------")
            board.display_board()
            print("Draw!")
            break

        board.display_board()
        player2.play(board)
        print("--------------------------")
        if board.check_winning():
            board.display_board()
            print(f"Congrats {player2.name}, you won!")
            break

        turns += 1
            
    choice = input("Play again? (Y/N) ")
    if choice == 'Y':
        start_game()
    else:
        print("See You.")


if __name__ == "__main__":
    start_game()
