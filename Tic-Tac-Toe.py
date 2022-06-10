import random


class TicTacToe:

    # represent instance of the class, in this case the board
    def __init__(self):
        self.board = []

    # method to create a 2-dimensional array
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    # method to random the first player to play
    def get_random_first_player(self):
        return random.randint(0, 1)

    # method to fill in the selected spot, to which player
    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    # method to check if player won the game
    def is_player_win(self, player):
        win = None

        # stores the number of items in an object
        n = len(self.board)

        # checking rows, win/lose horizontally
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns, win/lose vertically
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals, win/lose diagonally
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    # method to check if that slot in the board is empty or not
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    # method to swap turns
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    # return empty slots after board is refreshed with user inputs X or O
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    # main method to start the game
    def start(self):
        # calling method to create the board
        self.create_board()

        # calling method to random first player and set X and O
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            # calling method to show board
            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
