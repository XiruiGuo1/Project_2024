import random
##################################################################
# operation function: 
##################################################################

# add new 2 in each round
def add_new2(mat):
    row = random.randint(0,3)
    col = random.randint(0,3)

    while mat[row][col] !=0:
        row = random.randint(0,3)
        col = random.randint(0,3)
    
    mat[row][col] = 2

# function to update the matrix - assistant function
def move_singlerow_left(row):
    # find the none 0 ele
    new_row = [i for i in row if i!=0]

    for ele in range(len(new_row)-1): # [i for i in range(-1)] -> [] 
        if new_row[ele] == new_row[ele+1]:
            new_row[ele] *=2
            new_row[ele+1] = 0
    new_row =  [i for i in new_row if i!=0]
    return new_row + [0]*(4-len(new_row))

# function to update the matrix
def move(mat, dir):
    # left
    if dir == 'a':
        for i in range(4):
            mat[i]= move_singlerow_left(mat[i])
    
    # right
    if dir == 'd':
        for i in range(4):
            mat[i]= move_singlerow_left(mat[i][::-1])[::-1]

    # up
    elif dir == 'w':  
        for j in range(4):
            column = move_singlerow_left([mat[i][j] for i in range(4)])
            for i in range(4):
                mat[i][j] = column[i]
    # down
    elif dir == 's':  
        for j in range(4):
            column = move_singlerow_left([mat[i][j] for i in range(4)][::-1])[::-1]
            for i in range(4):
                mat[i][j] = column[i]
 

##################################################################
# initial mat and mat visulization
##################################################################
def initialize_mat():
    mat = [[0] * 4 for _ in range(4)]
    add_new2(mat)
    add_new2(mat)
    return mat

def print_mat(mat):
    for row in mat:
        print("\t".join(str(cell) if cell != 0 else '.' for cell in row))
    
##################################################################
# check_game_over 
##################################################################
def check_game_over(mat):
    for row in mat:
        if 2048 in row:
            print("Congratulations! You've reached 2048!")
            return True
    if any(0 in row for row in mat):
        return False
    for i in range(4):
        for j in range(4):
            if (i < 3 and mat[i][j] == mat[i + 1][j]) or (j < 3 and mat[i][j] == mat[i][j + 1]):
                return False
    print("Game Over! No more moves.")
    return True

