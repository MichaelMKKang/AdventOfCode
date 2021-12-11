import pandas as pd
import ast

def column_check(mb):
    for c in range(5):
        col_sum = 0
        for r in range(5):
            col_sum += mb[(5*r)+c]
        if col_sum==5:
            return True
    return False

def row_check(mb):
    for r in range(5):
        row_sum = 0
        for c in range(5):
            row_sum += mb[(5*r)+c]
        if row_sum==5:
            return True
    return False

# Oops, diagonals dont count
'''
def diag_check(mb):
    diag_sum=0
    for d in range(5):
        diag_sum += mb[(6*d)]
    if diag_sum==5:
        return True
    
    diag_sum=0
    for d in range(5):
        ...
'''

def victory_check(matchboard):
    if column_check(matchboard) or row_check(matchboard):
        return True
    else:
        return False

def get_score(board, mb):
    score = 0
    for i in range(len(board)):
        if mb[i]==0:
            score += int(board[i])
    return score



if __name__ == '__main__':
    with open('Day4 input.txt') as f:
        lines = f.readlines()

    # Get list of numbers to be drawn
    nums0 = '[' + lines[0][:-1] + ']'
    nums = ast.literal_eval(nums0)
    print(nums)

    # ingest boards into list of lists (each board is 25 elements length)
    # also spin up list of [0]*25 lists
    # write function to check victory. check 5n, 5n+1, 5n+2 etc for columns. check diags manually.
    #       These should each be sub functions...

    # NOTE: Need to have input have a newline character at the end
    # We ingest boards into a list of boards (each board being a 25 element list)
    #Also keep list of matches (each matchboard being a 25 element list of zeros at the start)

    num_boards = int((len(lines)-1)/6)
    board_list = []
    match_list = []

    for n in range(num_boards):
        data = lines[1:][(6*n)+1:(6*n)+6]
        board = []
        for d in data:
            data_proc = d[:-1].replace('  ',' ').lstrip().split(' ')
            for item in data_proc:
                board.append(item)
        board_list.append(board)
        match_list.append([0]*25)

    for n in nums:
        for b in range(len(board_list)):    #this indexes both boards and matchboards
            if str(n) in board_list[b]:
                i = board_list[b].index(str(n))
                match_list[b][i] = 1
            if victory_check(match_list[b]):
                print(n)
                print(match_list[b])
                print(board_list[b])
                print(get_score(board_list[b],match_list[b]))
                print(n * get_score(board_list[b],match_list[b]))
                break
        else:
            continue
        break
