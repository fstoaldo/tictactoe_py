""" 
Project 0 - TicTacToe.py
Flavio Stoll Toaldo
Start Date: March 23, 2019
Finish Date: March 26, 2019
"""

import itertools


def main():

    print("W E L C O M E   T O   T I C T A C T O E\n\n")

    def game_over(game_board, player=0):
        def all_same(check_list):
            if check_list.count(check_list[0]) == len(check_list) and check_list[0] != None:
                return True
            else:
                return False

        if player == 0:
            return False
        else:           
            # horizontal
            for row in game_board:
                if all_same(row):
                    print("Player {} wins!".format(player))
                    return True

            # vertical
            for col in range(len(game_board[0])):
                col_check = []
                for row in game_board:
                    col_check.append(row[col])
                if all_same(col_check):
                    print("Player {} wins!".format(player))
                    return True

            # diagonals
            # \ diagonal
            diag_check = []
            for i in range(len(game_board)):
                diag_check.append(game_board[i][i])
            if all_same(diag_check):
                print("Player {} wins!".format(player))
                return True
            # / diagonal
            diag_check = []
            for i, j in enumerate(reversed(range(len(game_board)))):
                diag_check.append(game_board[i][j])
            if all_same(diag_check):
                print("Player {} wins!".format(player))
                return True

            return False


    def print_board(game_board, row=0, col=0, player=0, update=False):
        if update == False:
            for row in game_board:
                print(row)
        else:
            try:
                if game_board[row][col] != None:
                    print("Position already taken, try again")
                    return False
                else:
                    # update board
                    if player == 1:
                        game_board[row][col] = "X"
                    else: 
                        game_board[row][col] = "O"

                    for row in game_board:
                        print(row)
                    return True
            except IndexError:
                print("Did you try to play out of bounds?")
                return False


    def play_game(players, game_size, game_board, end_game):
        print_board(game_board)
    
        while not end_game: 
            curr_player = next(players)

            def moves(curr_player):
                try:
                    row_play = int(input("Player {} select row to play: ".format(curr_player)))
                    col_play = int(input("Player {} select column to play: ".format(curr_player)))
                except:
                    print("Row and Column must be integers")
                    moves(curr_player)

                evaluation = print_board(game_board, row_play - 1, col_play - 1, curr_player, update=True)
                
                if evaluation == False:
                    moves(curr_player)

            moves(curr_player)
            end_game = game_over(game_board, curr_player)    

        if end_game == True:
            again = input("Play again? [Y/N]")
            if again.lower() == ('y' or "yes"):
                set_up()
            else:
                print("Good bye, fellas")
                quit()


    def set_up():
        try:
            game_size = int(input("Please enter the size of the board between 3 and 10: "))
        except:
            print("Game size must be an integer!")
            set_up()

        if game_size < 3 or game_size > 10:
            print("Please, choose a game size between 3 and 10")
            set_up()

        players = itertools.cycle([1, 2])
        game_board = [[None for col in range(game_size)] for row in range(game_size)]
        end_game = False
        play_game(players, game_size, game_board, end_game)

    set_up()

if __name__ == "__main__":
    main()


        

   

















