from config import pr, SCREEN_HEIGHT,SCREEN_WIDTH
from button import Button, ToggleButton
from game import Game
import random



### Setting Screen Size

pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Orbis")
game = Game()


## Generate 2D Grid 
def gen_matrix2D(rows, columns):
    arr2D = [[0] * columns for _ in range(rows)]
    return arr2D


cell_nums = 40
cell_height = 0
cell_width = 0

cell_height = SCREEN_HEIGHT // cell_nums
cell_width = SCREEN_WIDTH // cell_nums
Matrix2D = gen_matrix2D(cell_nums, cell_nums)

### Game loop
while not pr.window_should_close():
    ### Update
    game.update()

    mouse_coords = pr.get_mouse_position()

    
    i = int(mouse_coords.x // cell_width)
    j = int(mouse_coords.y // cell_height)
    mouse_bounds_x = True if mouse_coords.x < SCREEN_WIDTH else False
    mouse_bounds_y = True if mouse_coords.y < SCREEN_HEIGHT else False
    if pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and mouse_bounds_x and mouse_bounds_y:
        if 0 <= i<= cell_nums and 0 <= j <= cell_nums:
            print(i,j)
            Matrix2D[i][j] = 1

    new_Grid = gen_matrix2D(cell_nums, cell_nums)
    for i in range(len(Matrix2D)):
        for j in range(len(Matrix2D[i])):
            if Matrix2D[i][j] == 1 and j == (len(Matrix2D[i]) - 1):
                new_Grid[i][j] = 1
            if j < (len(Matrix2D[i])) - 1:
                if Matrix2D[i][j] == 1 and Matrix2D[i][j+1] == 0:
                    new_Grid[i][j+1] = 1
                if Matrix2D[i][j] == 1 and Matrix2D[i][j+1] == 1:
                    rand_choice = random.random()
                    if i == 0:
                        if Matrix2D[i][j] == 1 and Matrix2D[i][j+1] == 0:
                            new_Grid[i][j+1] = 1
                        elif Matrix2D[i][j] == 1 and Matrix2D[i][j+1] == 1:
                            if Matrix2D[i+1][j+1] == 0:
                                new_Grid[i+1][j+1] = 1
                            else:
                                new_Grid[i][j] = 1
                    elif i == len(Matrix2D) - 1:
                        if Matrix2D[i][j] == 1 and Matrix2D[i][j+1] == 0:
                            new_Grid[i][j+1] = 1
                        elif Matrix2D[i][j] == 1 and Matrix2D[i][j+1] == 1:
                            if Matrix2D[i-1][j+1] == 0:
                                new_Grid[i-1][j+1] = 1
                            else:
                                new_Grid[i][j] = 1
                    else:
                        if Matrix2D[i-1][j+1] == 0 and rand_choice > 0.5:
                            new_Grid[i-1][j+1] = 1
                        elif Matrix2D[i+1][j+1] == 0:
                            new_Grid[i+1][j+1] = 1
                        else:
                            new_Grid[i][j] = 1
                        
            
    Matrix2D = new_Grid
    
    
    ### Draw
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
    for i in range(len(Matrix2D)):
        for j in range(len(Matrix2D[i])):
            if Matrix2D[i][j] == 0:
                pr.draw_rectangle_lines(i * cell_width, j * cell_height, cell_width, cell_height, pr.BLACK)
            if Matrix2D[i][j] == 1:
                pr.draw_rectangle(i * cell_width, j * cell_height, cell_width, cell_height, pr.BLACK)
    game.draw()

    pr.end_drawing()
pr.close_window()