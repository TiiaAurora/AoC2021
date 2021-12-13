from os import replace
from pathlib import Path

data_whatever = Path("Day4b.txt").read_text().splitlines()
first_line = data_whatever[0]

draw_numbers_str = first_line.split(",")
draw_numbers = [int(i) for i in draw_numbers_str]

current_line = 1
bingo_boards: list[list[list[int]]] = []

while True:

    line = data_whatever[current_line]
    current_line += 1
    if not line:
        rows = []
        continue

    line_numbers = []
    for i in line.split(" "):
        if i:
            line_numbers.append(int(i))
    rows.append(line_numbers)

    if len(rows) == 5:
        bingo_boards.append(rows)

    if len(data_whatever) == current_line:
        break

print(bingo_boards)


def bingo_winner_board_thingy():
    winning_draw = None
    winning_board = None

    # for each drawn number:
    for draw in draw_numbers:
        winners = []

        # check if it is in any of the bingo boards and clear those entries
        for board in bingo_boards:
            for row in board:
                if draw in row:
                    i = row.index(draw)
                    row[i] = None

        # check if any of the boards has won

        for board in bingo_boards:
            # check if any row is only None
            for row in board:
                if row == [None, None, None, None, None]:
                    winning_board = board
                    winning_draw = draw
                    winners.append(board)

            # check if any column is just None

            for i in range(5):
                column = []
                for row in board:
                    column.append(row[i])
                if column == [None, None, None, None, None]:
                    winning_board = board
                    winning_draw = draw
                    winners.append(board)

        # remove all winners from boards so they can't win again
        for winner in winners:
            if winner and winner in bingo_boards:
                print('removing', len(bingo_boards), "remaining boards")
                bingo_boards.remove(winner)

    return (winning_draw, winning_board)


# call the function to work out which board won
draw, board = bingo_winner_board_thingy()
print("We have a winner!")
print(draw)
print(board)

# sum the remaining numbers in the winning board
total = 0
for row in board:
    for i in row:
        if i:
            total += i

# multiply by the last drawn number
print(f"The magic number is {total * draw}")
