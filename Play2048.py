from Operation import *

##################################################################
# play game: 
##################################################################
def play_2048():
    mat = initialize_mat()
    print("Welcome to 2048! Use 'w', 'a', 's', 'd' to move. Reach 2048 to win.")
    print_mat(mat)

    while True:
        move_direction = input("Enter move (w/a/s/d): ").strip().lower()
        if move_direction not in {'w', 'a', 's', 'd'}:
            print("Invalid input. Please use 'w', 'a', 's', or 'd'.")
            continue
        
        move(mat, move_direction)
        add_new2(mat)
        print_mat(mat)

        # Check for game over or win
        if check_game_over(mat):
            restart = input("Play again? (y/n): ").strip().lower()
            if restart == 'y':
                mat = initialize_mat()
                print_mat(mat)
            else:
                break

if __name__ == '__main__':
    play_2048()
