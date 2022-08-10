import random


board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5 ,0 ,0 ,0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8 ,0],
         [0, 0, 0 ,4, 1 ,9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]
# board = [[0 for _ in range(9)] for _ in range(9)]

# board = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 1, 0, 0 ,0 ,0 ,0],
#          [0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0 ,0],
#          [0, 0, 0 ,0, 0 ,0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# board = [[4, 9, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 4, 0 ,3 ,0 ,6],
#          [7, 5, 0, 0, 9, 0, 1, 0, 0],
#          [9, 0, 2, 0, 0, 0, 0, 0, 5],
#          [0, 0, 0, 4, 0, 0, 0, 6, 0],
#          [0, 7, 0, 0, 0, 1, 0, 0, 0],
#          [5, 0, 0, 9, 8, 0, 6, 0 ,0],
#          [0, 4, 9 ,0, 0 ,7, 0, 0, 0],
#          [0, 2, 0, 0, 0, 3, 5, 0, 0]]

def entropy_check(board):
    lowest_ent = 10
    n_lowest_pos = [0, 0]
    n_poss = []
    entropy_board = []
    for y, col in enumerate(board):
        entropy_col = []
        for x, number in enumerate(col):
            if number != 0: 
                entropy_col.append('C')
                continue
            horizontal = board[y]
            vertical = list(zip(*board))[x]
            sections = []
            section_pos = y//3, x//3
            for col in board[section_pos[0]*3: 3*(section_pos[0] + 1)]:
                sections.extend(col[section_pos[1]*3: 3*(section_pos[1] + 1)])

            possibilities = [i for i in [n for n in range(1, 10)] if i not in set(horizontal + list(vertical) + sections)]
            entropy = len(possibilities)
            entropy_col.append(entropy)
            if entropy < lowest_ent:
                lowest_ent = entropy
                n_lowest_pos = [y, x]
                n_poss = possibilities
            elif entropy == lowest_ent:
                n_lowest_pos, n_poss = random.choice([[n_lowest_pos, n_poss], [[y, x], possibilities]])
              


        entropy_board.append(entropy_col)

    # print(n_lowest_pos, n_poss)
    board[n_lowest_pos[0]][n_lowest_pos[1]] = random.choice(n_poss)
    return board, n_lowest_pos, entropy_board
       

def display(board):
    for y, col in enumerate(board):
        column = ""
        for i in range(0, len(col), 3):
            for n in col[i: i+3]:
                column += str(n) + ','
            column = column[:-1] +  '|'
        print(column[:-1])
        if (y + 1) % 3 == 0:
            print('-'*18)
    print('='*18)

if __name__ == "__main__": 
    display(board)

    while True:
        try:
            board, _, _ = entropy_check(board)
            display(board)
        except IndexError:
            print('done')
            break
            
