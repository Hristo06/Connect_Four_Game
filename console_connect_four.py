def print_of_field(field):
    for i in field:
        print(i)

def mechanics(field, column):
    for row in range(len(field)):
        if row + 1 == len(field):
            field[row][column-1] += curr_player
            return row
        elif field[row + 1][column - 1] != 0:
            field[row][column - 1] += curr_player
            return row
def check_for_win(field, row, column):
    list_of_numbers = []

    #check for horizontal
    if field[row].count(curr_player) >= 4:
        #check for right
        if column - 1 + 3 <= 6:
                for col in range(column - 1, column + 3):
                    list_of_numbers.append(field[row][col])
                if list_of_numbers.count(list_of_numbers[0]) == 4:
                    print_of_field(field)
                    print(f"The winner is player {curr_player}")
                    quit()
                else:
                    list_of_numbers.clear()

        #check for left
        if column - 1 - 3 >= 0:
                #left horizontal
                for col in range(column - 1, column - 5, -1):
                    list_of_numbers.append(field[row][col])
                if list_of_numbers.count(list_of_numbers[0]) == 4:
                    print_of_field(field)
                    print(f"The winner is player {curr_player}")
                    quit()
                else:
                    list_of_numbers.clear()


    #check for vertical
    if row + 3 < 6:
        for vertical_numbers in range(row, row + 4):
            list_of_numbers.append(field[vertical_numbers][column - 1])
        if list_of_numbers.count(list_of_numbers[0]) == 4:
            print_of_field(field)
            print(f"The winner is player {curr_player}")
            quit()
        else:
            list_of_numbers.clear()

    #check for diagonal
    #left side
    if column - 1 - 3 >= 0:
        #down left
        if row + 3 < 6:
            down_left = 0
            for down_l_row in range(row, row + 4):
                list_of_numbers.append(field[down_l_row][column - 1 - down_left])
                down_left += 1
            if list_of_numbers.count(list_of_numbers[0]) == 4:
                print_of_field(field)
                print(f"The winner is player {curr_player}")
                quit()
            else:
                list_of_numbers.clear()

        #up left
        if row - 3 > - 1:
            up_left = 0
            for up_l_row in range(row, row - 4, -1):
                list_of_numbers.append(field[up_l_row][column - 1 - up_left])
                up_left += 1
            if list_of_numbers.count(list_of_numbers[0]) == 4:
                print_of_field(field)
                print(f"The winner is player {curr_player}")
                quit()
            else:
                list_of_numbers.clear()

    #right side
    if column - 1 + 3 <= 6:
        #down right
        if row + 3 < 6:
            down_right = 0
            for down_r_row in range(row, row + 4):
                list_of_numbers.append(field[down_r_row][column - 1 + down_right])
                down_right += 1
            if list_of_numbers.count(list_of_numbers[0]) == 4:
                print_of_field(field)
                print(f"The winner is player {curr_player}")
                quit()
            else:
                list_of_numbers.clear()
        #up right
        if row - 3 > - 1:
            up_right = 0
            for up_r_row in range(row, row - 4, - 1):
                list_of_numbers.append(field[up_r_row][column - 1 + up_right])
                up_right += 1
            if list_of_numbers.count(list_of_numbers[0]) == 4:
                print_of_field(field)
                print(f"The winner is player {curr_player}")
                quit()
            else:
                list_of_numbers.clear()



player_count = int(input(f"Your goal is to connect four numbers diagonally, horizontally and vertically.\nSelect number of players(2 players recommended)\n"))
field = [[0 for el in range(7)] for b in range(6)]
print_of_field(field)
curr_player = 1
moves_of_players = {}
for players in range(1, player_count + 1):
    moves_of_players[players] = 0
while True:
    selected_column = int(input(f"Player {curr_player}, please choose a column:\n"))
    if not 0 < selected_column <= 7:
        print(f"Please choose a valid column (from 1 to 7)")
        continue
    if field[0][selected_column - 1] != 0:
        print(f"No free places in current column! Try again")
        continue
    row = mechanics(field, selected_column)
    moves_of_players[curr_player] += 1
    if moves_of_players[curr_player] >= 4:
        check_for_win(field, row, selected_column)
    print_of_field(field)
    if curr_player < player_count:
        curr_player += 1
    elif curr_player == player_count:
        curr_player = 1