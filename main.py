'''
For next time: test the program with Henry to see how smart the AI is.

Continued working on game with Henry,we added code for enemy AI to detect when
there's only one empty space left on a row and then it will place its symbol there.
4-14-24

Posted on Github.
4-10-24
'''
import random  # for randomizing user choice (they use X or  they use O)


def displayGameBoard(game_board):
    # loop through the grid
    # x is used as a counter (x = 0, x = 1, x = 2, etc...)
    # you can use a loop to repeat statements a certain amount of times
    # in this case, the loop will go through EACH element on the game board LIST and print each one out
    # the total number of iterations that the loop will go through is 15 iterations
    for x in range(0, len(game_board)):
        # when we reach CERTAIN elements, GO TO THE NEXT LINE
        if x == 5 or x == 10 or x == 15:
            print("")
        # the notation ->  list[index number]  allows you to access an element of the LIST
        # print each element on the same line
        # first five elements are on the first row
        # next five elements are on second row
        # last five elements are on the third row
        print(game_board[x], end='')


def setUserSymbol():
    # returns a number between 0 and 1 (both included)
    random_choice = random.randint(0, 1)

    # decide on the symbol that the player will use for the game BASED ON the randomly picked number
    user_symbol = ""
    # if else statements - good for different outcome conditions
    if random_choice == 0:
        user_symbol = 'O'
    else:
        user_symbol = 'X'
    return user_symbol


"""
This function places the players game symbol on a game board position from 1 through 9 (will always be a valid position).
"""
def placeOnValidSpot(choice,game_board,player_symbol,enemy_symbol):
    # this idx var is set to -1 when initialized (will change according to users choice number provided)
    user_position_idx = -1

    # check which digit the user entered and apply the symbol to the correct position in the grid then save the index value
    if choice == 1:
        game_board[0] = player_symbol
        user_position_idx = 0
    elif choice == 2:
        game_board[2] = player_symbol
        user_position_idx = 2
    elif choice == 3:
        game_board[4] = player_symbol
        user_position_idx = 4
    elif choice == 4:
        game_board[5] = player_symbol
        user_position_idx = 5
    elif choice == 5:
        game_board[7] = player_symbol
        user_position_idx = 7
    elif choice == 6:
        game_board[9] = player_symbol
        user_position_idx = 9
    elif choice == 7:
        game_board[10] = player_symbol
        user_position_idx = 10
    elif choice == 8:
        game_board[12] = player_symbol
        user_position_idx = 12
    elif choice == 9:
        game_board[14] = player_symbol
        user_position_idx = 14
    print(f"Last position that player placed their symbol was at index {user_position_idx}")
    displayGameBoard(game_board)  # display game board after the user has made valid move (showing current status of the board)

    # after player makes a valid move, end the game if three in a row is detected
    continueGamePlayer = checkIfMatchContinues2(game_board, player_symbol, enemy_symbol)
    if not continueGamePlayer:
        print("three in a row FOUND, USER WINS, GAME OVER!")
        exit(0)
    else:
        # game is not over so return the users last positions INDEX value
        return user_position_idx


"""
This function will force the users game position choice to be a valid number between 1 and 9.
"""
def getValidChoice(player_symbol):
    # use try-except block to handle ValueError
    choice = int(input(f"\nSelect where you want to place your {player_symbol} (type in 1 - 9): "))
    # this while loop will handle input validation if user doesn't enter a valid digit in the range
    while not (1 <= choice <= 9):
        choice = int(input(f"That number falls outside the range of board positions you can pick from. Please "
                           f"enter a digit that is between 1 and 9 : "))
    return choice



"""
This function allows the player to select where they want to put their game symbol, it will check that its valid
before allowing the symbol to be placed down or it will prompt the user to enter a valid number repeatedly.
"""
def playersMove(player_symbol, game_board,enemy_symbol):
    # a dictionary to keep track of numbers already placed down by the user in previous turns
    spaces_taken_already = {1:game_board[0], 2:game_board[2], 3:game_board[4],
                            4:game_board[5], 5:game_board[7], 6:game_board[9],
                            7:game_board[10], 8:game_board[12], 9:game_board[14]}

    # use try-except block to handle ValueError
    try:
        choice = getValidChoice(player_symbol)
        # this while loop will handle if the space has been taken already that the user selected, keep asking for new choice
        while spaces_taken_already[choice] != "_":
            print("that space has been taken already man!")
            choice = getValidChoice(player_symbol)

        # capture the users last position (this is assuming three in a row hasn't happened so an index value was
        # returned from placeonValidSpot function) and return it
        last_position_index = placeOnValidSpot(choice, game_board, player_symbol,enemy_symbol)
        return last_position_index
    except KeyboardInterrupt:
        print("\nUser closed the game session early.")
        exit(0)

'''
In this function, the AI will make its move by keeping
track of all the horizontal, vertical, and diagonal game spaces and any user symbols placed on them. If
it detects the last user position was on a specific space using a subfunction then it will place near that space.
'''
def AImove(enemy_symbol, game_board, player_symbol,last_position_index):
    print("\ninside AI move function")

    '''
    game board VALID POSITION INDEXES
    0  2  4
    5  7  9
    10 12 14
    '''

    # vertical game board positions
    v_array1 = [game_board[0], game_board[5], game_board[10]]
    v_array2 = [game_board[2], game_board[7], game_board[12]]
    v_array3 = [game_board[4], game_board[9], game_board[14]]

    # diagonal game board positions
    d_array1 = [game_board[0], game_board[7], game_board[14]]
    d_array2 = [game_board[4], game_board[7], game_board[10]]

    # horizontal game board positions
    h_dict1 = {1: [game_board[0], game_board[2], game_board[4]]}
    h_dict2 = {2: [game_board[5], game_board[7], game_board[9]]}
    h_dict3 = {3: [game_board[10], game_board[12], game_board[14]]}


    # call the function to activate the AI's strategy via a custom algorithm
    '''
    if the users last position index falls on 0,2, or 4 then detect symbols on HORIZONTAL ROW 1.
    User placed symbol in the top row.
    '''
    if last_position_index == 0 or last_position_index == 2 or last_position_index == 4:
        filled_row = detectUserSymbolsOnRows(enemy_symbol, game_board, player_symbol, h_dict1)
        # if row is full then check next row
        if filled_row:
            print("The previous row was completely filled so calling the function again for the NEXT ROW")
            detectUserSymbolsOnRows(enemy_symbol, game_board, player_symbol, h_dict2)

        # when user symbol falls on index 0, also check vertical row 1 and diagonal row 1
        # when user symbol falls on index 2, also check vertical row 2
        # when user symbol falls on index 4, also check vertical row 3 and diagonal row 2
    elif last_position_index == 5 or last_position_index == 7 or last_position_index == 9:
        # user placed symbol in the middle row
        detectUserSymbolsOnRows(enemy_symbol, game_board, player_symbol, h_dict2)

        # when user symbol falls on index 5, also check vertical row 1
        # when user symbol falls on index 7, also check vertical row 2, diagonal row 1, diagonal row 2
        # when user symbol falls on index 9, also check vertical row 3
    else:
        # user placed symbol in the bottom row
        detectUserSymbolsOnRows(enemy_symbol, game_board, player_symbol, h_dict3)

        # when user symbol falls on index 10, also check vertical row 1, diagonal row 2
        # when user symbol falls on index 12, also check vertical row 2
        # when user symbol falls on index 14, also check vertical row 3, diagonal row 1

    displayGameBoard(game_board)
    continueGameEnemy = checkIfMatchContinues2(game_board, player_symbol, enemy_symbol)
    if not continueGameEnemy:
        print("three in a row FOUND, ENEMY AI WINS, GAME OVER!")
        exit(0)

'''
In this function, the enemy AI can detect when user has 1 or 2 symbols placed down and attempts to
place a symbol near it.
'''
def detectUserSymbolsOnRows(enemy_symbol, game_board, player_symbol, h_dict):
    print("\ninside detectUserSymbolsOnRows function")

    # boolean flag var that will indicate whether the row was full or not
    row_full = False

    # figure out which row the function will analyze
    row_number = list(h_dict.keys())[0]

    # initialize list of indexes (the indexes of the elements on the game board)
    # if the row number has an ID value of 1, 2,or 3 then it correponds to that specific row so store the appropriate index numbers in the list
    if row_number == 1:
        #print("row number is 1")
        row_idx_list = [0, 2, 4]
    elif row_number == 2:
        #print("row number is 2")
        #x = 0 1 2
        #y = 5 7 9
        row_idx_list = [5, 7, 9]
    else:
        #print("row number is 3")
        row_idx_list = [10, 12, 14]

    # check if the row is full already (no underscores remaining), if true then do nothing and go to the next row
    if h_dict[row_number].count("_") == 0:
        #print("this row has no empty spaces left, place symbol on next row.")
        row_full = True
    elif h_dict[row_number].count("_") == 1:
        print("ONLY ONE EMPTY SPACE LEFT")

        # find the INDEX of the empty space _ and then place the enemy symbol there
        x = h_dict[row_number].index("_")
        h_dict[row_number][x] = enemy_symbol

        # IGNORE THIS OLD CODE: now use X var to identify the correct index value in row_idx_list
        #y = row_idx_list[x]

        # finally update the GAME BOARD at the correct index with the correct value
        game_board[row_idx_list[x]] = h_dict[row_number][x]
    else:
        # detect if user has placed ONE symbol in the specific dictionary row (indicated by row number)
        if h_dict[row_number].count(player_symbol) == 1:
            print(f"AI has detected player has placed one symbol down on row {row_number}.")
            # right-most position has player symbol OR left-most position has player symbol
            if h_dict[row_number][0] == player_symbol or h_dict[row_number][2] == player_symbol:
                #print("AI has detected player has placed one symbol on the LEFT MOST space or RIGHT MOST space.")
                # CHANGE THE SECOND ELEMENT OF THE LIST TO THE ENEMY SYMBOL
                h_dict[row_number][1] = enemy_symbol
                #print(f"The value of h_dict[row_number][1] is {h_dict[row_number][1]}")
                # CHANGE THE GAME BOARD MIDDLE VALUE (ON THE CORRECT ROW) TO THE ENEMY SYMBOL
                game_board[row_idx_list[1]] = h_dict[row_number][1]
                #print(f"The value of game_board[row_idx_list[1]] is {game_board[row_idx_list[1]]}")
            # middle position has player symbol (so place enemy symbol to the left or right RANDOMLY)
            if h_dict[row_number][1] == player_symbol:
                #print("AI has detected player has placed one symbol on the MIDDLE SPACE.")
                # use the random library
                enemy_random_choice = random.randint(0, 1)
                # CHANGE THE FIRST ELEMENT TO THE ENEMY SYMBOL
                if enemy_random_choice == 0:
                    h_dict[row_number][0] = enemy_symbol
                else:
                    # CHANGE THE THIRD ELEMENT TO THE ENEMY SYMBOL
                    h_dict[row_number][2] = enemy_symbol
                # FIRST ELEMENT WAS SET TO THE ENEMY SYMBOL SO CHANGE THE GAME BOARD LEFT MOST VALUE (ON THE CORRECT ROW) TO ENEMY SYMBOL
                if h_dict[row_number][0] == enemy_symbol:
                    # old game_board[0] = h_dict[0]
                    game_board[row_idx_list[0]] = h_dict[row_number][0]
                else:
                    # THIRD ELEMENT WAS SET TO THE ENEMY SYMBOL SO CHANGE THE GAME BOARD RIGHT MOST VALUE (ON THE CORRECT ROW) TO ENEMY SYMBOL
                    # old game_board[4] = h_dict[2]
                    game_board[row_idx_list[2]] = h_dict[row_number][2]
                #print(f"The value of h_dict[row_number][0] is {h_dict[row_number][0]}")
                #print(f"The value of h_dict[row_number][2] is {h_dict[row_number][2]}")
                #print(f"The value of game_board[row_idx_list[0]] is {game_board[row_idx_list[0]]} and value of game_board[row_idx_list[2]] is {game_board[row_idx_list[2]]}")
        elif h_dict[row_number].count(player_symbol) == 0:
            print(f"AI has detected 0 player symbols on row {row_number}.")

            # place enemy symbol on a random space in the row
            # use the random library
            enemy_random_choice = random.randint(0, 2)
            # CHANGE THE FIRST ELEMENT TO THE ENEMY SYMBOL
            if enemy_random_choice == 0:
                h_dict[row_number][0] = enemy_symbol
            elif enemy_random_choice == 1:
                # CHANGE THE SECOND ELEMENT TO THE ENEMY SYMBOL
                h_dict[row_number][1] = enemy_symbol
            else:
                # CHANGE THE THIRD ELEMENT TO THE ENEMY SYMBOL
                h_dict[row_number][2] = enemy_symbol


            # FIRST ELEMENT WAS SET TO THE ENEMY SYMBOL SO CHANGE THE GAME BOARD LEFT MOST VALUE (ON THE CORRECT ROW) TO ENEMY SYMBOL
            if h_dict[row_number][0] == enemy_symbol:
                game_board[row_idx_list[0]] = h_dict[row_number][0]
            elif  h_dict[row_number][1] == enemy_symbol:
                # SECOND ELEMENT WAS SET TO THE ENEMY SYMBOL SO CHANGE THE GAME BOARD MIDDLE MOST VALUE (ON THE CORRECT ROW) TO ENEMY SYMBOL
                game_board[row_idx_list[1]] = h_dict[row_number][1]
            else:
                # THIRD ELEMENT WAS SET TO THE ENEMY SYMBOL SO CHANGE THE GAME BOARD RIGHT MOST VALUE (ON THE CORRECT ROW) TO ENEMY SYMBOL
                game_board[row_idx_list[2]] = h_dict[row_number][2]
            #print(f"The value of h_dict[row_number][0] is {h_dict[row_number][0]}")
            #print(f"The value of h_dict[row_number][1] is {h_dict[row_number][1]}")
            #print(f"The value of h_dict[row_number][2] is {h_dict[row_number][2]}")
            #print(f"The value of game_board[row_idx_list[0]] is {game_board[row_idx_list[0]]}"
            #      f"and value of game_board[row_idx_list[1]] is {game_board[row_idx_list[1]]} "
            #      f"and value of game_board[row_idx_list[2]] is {game_board[row_idx_list[2]]}")

        elif h_dict[row_number].count(player_symbol) == 2:
            print(f"AI has detected 2 player symbols on row {row_number}.")

            '''
            AI has to place a symbol on a row that has TWO player symbols already
            possible scenarios include :  
            
            scenario 1)   _ | X | X 
            
            scenario 2)   X | X | _
            
            scenario 3)   X | _ | X
             '''
            if h_dict[row_number][1] == player_symbol and h_dict[row_number][2] == player_symbol:
                #print("player symbol detected on MIDDLE SPACE AND RIGHT-MOST SPACE")

                h_dict[row_number][0] = enemy_symbol
                #print(f"The value of h_dict[row_number][0] is {h_dict[row_number][0]}")
                # CHANGE THE GAME BOARD LEFT-MOST VALUE (ON THE CORRECT ROW) TO THE ENEMY SYMBOL
                game_board[row_idx_list[0]] = h_dict[row_number][0]

        else:
            #print("this row has been completely filled with just player symbols, moving on to next row (keep this for testing purposes).")
            row_full = True
    return row_full


'''
In this function, the enemy AIs game symbol will be picked based on what the players symbol is.
'''
def setEnemySymbol(player_symbol):
    if player_symbol == "X":
        enemy_symbol = 'O'
    else:
        enemy_symbol = 'X'

    return enemy_symbol


''' Observes the entire game board after EACH PLAYER makes a move
and if three of the same symbol are detected vertically, horizontally, diagonally then
END THE GAME (ALTERNATIVE ALGORITHM)'''
def checkIfMatchContinues2(game_board, player_symbol, enemy_symbol):
    print("\ncheckIfMatchContinues2 function called")
    # ALTERNATE SOLUTION : CONSIDER EACH ROW, COLUMN, AND DIAGONAL AS ITS OWN ARRAY, AND JUST CHECK THOSE ARRAYS IF THEY HAVE THREE MATCHING ELEMENTS!

    # horizontal game board positions
    h_array1 = [game_board[0], game_board[2], game_board[4]]
    h_array2 = [game_board[5], game_board[7], game_board[9]]
    h_array3 = [game_board[10], game_board[12], game_board[14]]

    # vertical game board positions
    v_array1 = [game_board[0], game_board[5], game_board[10]]
    v_array2 = [game_board[2], game_board[7], game_board[12]]
    v_array3 = [game_board[4], game_board[9], game_board[14]]

    # diagonal game board positions
    d_array1 = [game_board[0], game_board[7], game_board[14]]
    d_array2 = [game_board[4], game_board[7], game_board[10]]

    # this boolean var confirms whether match will continue or not
    continueMatch = True

    if h_array1.count(player_symbol) == 3 or h_array1.count(enemy_symbol) == 3:
        print("all elements are the same on the first horizontal row")
        continueMatch = False
    elif h_array2.count(player_symbol) == 3 or h_array2.count(enemy_symbol) == 3:
        print("all elements are the same on the second horizontal row")
        continueMatch = False
    elif h_array3.count(player_symbol) == 3 or h_array3.count(enemy_symbol) == 3:
        print("all elements are the same on the third horizontal row")
        continueMatch = False
    elif v_array1.count(player_symbol) == 3 or v_array1.count(enemy_symbol) == 3:
        print("all elements are the same on the first vertical row")
        continueMatch = False
    elif v_array2.count(player_symbol) == 3 or v_array2.count(enemy_symbol) == 3:
        print("all elements are the same on the second vertical row")
        continueMatch = False
    elif v_array3.count(player_symbol) == 3 or v_array3.count(enemy_symbol) == 3:
        print("all elements are the same on the third vertical row")
        continueMatch = False
    elif d_array1.count(player_symbol) == 3 or d_array1.count(enemy_symbol) == 3:
        print("all elements are the same on the first diagonal row")
        continueMatch = False
    elif d_array2.count(player_symbol) == 3 or d_array2.count(enemy_symbol) == 3:
        print("all elements are the same on the second diagonal row")
        continueMatch = False
    else:
        print("no three in a row found on this game board!")
    #print("exiting checkIfMatchContinues2 function")
    return continueMatch


def main():
    print("TIC TAC TOE GAME")
    # create the grid game board
    # use the list type - a data type that is able to store multiple elements of the same value
    game_board = ['_', '|', '_', '|', '_',
                  '_', '|', '_', '|', '_',
                  '_', '|', '_', '|', '_']

    # users symbol is selected first
    player_symbol = setUserSymbol()
    print(f"the value of player_symbol is {player_symbol}")

    # set the AI enemy symbol to be the leftover one
    enemy_symbol = setEnemySymbol(player_symbol)
    print(f"the value of enemy_symbol is {enemy_symbol}")

    # show the game boards current state
    displayGameBoard(game_board)

    # main game loop
    while True:
        # store the INDEX of the position that the user placed their last symbol at
        # pass this var into the AI move function so the AI knows which row to focus on and which rows to ignore
        last_position_index = playersMove(player_symbol, game_board,enemy_symbol)
        print(f"\nlast_position_index value after player function call is {last_position_index}")
        AImove(enemy_symbol, game_board, player_symbol, last_position_index)
main()

