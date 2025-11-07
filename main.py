class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play(self, board):
        print(f"{self.name}'s turn.")
        while True:
            row, col = self.get_coordinates()
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Please enter valid numbers. [1, 3]")
            elif board.board[row - 1][col - 1] != ' ':
                print("This cell is already taken! Try again.")
            else:
                board.board[row - 1][col - 1] = self.symbol
                break


    def get_coordinates(self):
        while True:
            try:
                row = int(input("Row: "))
                column = int(input("Column: "))
                return (row, column)
            except ValueError:
                print("Please enter valid numbers. [1, 3]")
        

class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def display_board(self):
        print("--------------------------")
        print("    1   2   3 ")
        print("  -------------")
        for i in range(3):
            print(f"{i + 1} |", end="")
            for j in range(3):
                print(f" {self.board[i][j]}", end="")
                print(" |", end="")
            print()
            if i < 2:
                print("  -------------")
    
        print("  -------------")
        print()

    def check_winning(self):
        # Rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != ' ':
                return True 

        # Columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != ' ':
                return True
        
        # Diagonals
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != ' ':
            return True 
        if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] != ' ':
            return True 

def get_symbol():
    symbol = input("Enter a one-character symbol: ")
    while len(symbol) != 1 or symbol.isspace():
        if symbol.isspace():
            print("Symbol can't be whitespace!")
        else:
            print("Symbol must be of length one.")
        symbol = input("Please try again: ")

    return symbol


def start_game():
    print("First Player Info.")
    name1 = input("Enter your name: ")
    symbol1 = get_symbol()
    player1 = Player(name1, symbol1)

    print("Second Player Info.")
    name2 = input("Enter your name: ")
    symbol2 = get_symbol()
    while symbol1 == symbol2:
        print("Symbols must be different!")
        symbol2 = get_symbol()


    player2 = Player(name2, symbol2)

    board = Board()

    turns = 0
    while True:
        board.display_board()
        player1.play(board)

        if board.check_winning():
            board.display_board()
            print(f"Congrats {player1.name}, you won!")
            break
        
        turns += 1
        if turns == 9:
            board.display_board()
            print("Draw!")
            break

        board.display_board()
        player2.play(board)
        if board.check_winning():
            board.display_board()
            print(f"Congrats {player2.name}, you won!")
            break

        turns += 1
            
    choice = input("Play again? (Y/N) ")
    if choice.upper() == 'Y':
        start_game()
    else:
        print("See You.")


if __name__ == "__main__":
    start_game()
