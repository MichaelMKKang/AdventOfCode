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

    num_boards = int((len(lines)-1)/6)
    board_list = []
    match_list = []
    win_list = [0]*num_boards

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
                win_list[b] = 1

        if sum(win_list)==len(win_list)-1:      #assuming there are no ties for last place
            lose = win_list.index(0)
            print('losing board index is {}'.format(lose))
        
        if sum(win_list)==len(win_list):        #only hits here with "lose" index value
            print('lost on number {}'.format(n))
            print('found losing board sum: ',get_score(board_list[lose],match_list[lose]))
            print('Score: ',n * get_score(board_list[lose],match_list[lose]))
            break
