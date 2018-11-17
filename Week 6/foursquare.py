import turtle


SQUARE = 50
color = "white"
already_pressed = []
white_counter = 0
black_counter = 0
total_moves_count = 0
   
def draw_board(n):
    
    ''' Function: draw_board
        Parameters: n, an int for # of squares
        Returns: nothing
        Does: Draws an nxn board with a green background
    '''

    turtle.setup(n * SQUARE + SQUARE, n * SQUARE + SQUARE)
    turtle.screensize(n * SQUARE, n * SQUARE)
    turtle.bgcolor('white')

    # Create the turtle to draw the board
    othello = turtle.Turtle()
    othello.penup()
    othello.speed(0)
    othello.hideturtle()

    # Line color is black, fill color is green
    othello.color("black", "forest green")
    
    # Move the turtle to the upper left corner
    corner = -n * SQUARE / 2
    othello.setposition(corner, corner)
  
    # Draw the green background
    othello.begin_fill()
    for i in range(4):
        othello.pendown()
        othello.forward(SQUARE * n)
        othello.left(90)
    othello.end_fill()

    # Draw the horizontal lines
    for i in range(n + 1):
        othello.setposition(corner, SQUARE * i + corner)
        draw_lines(othello, n)

    # Draw the vertical lines
    othello.left(90)
    for i in range(n + 1):
        othello.setposition(SQUARE * i + corner, corner)
        draw_lines(othello, n)


######## third column ############
    othello.begin_fill()
    othello.color("white")
    othello.hideturtle()
    othello.up()
    othello.goto(45, 25)
    othello.down()
    othello.circle(20)
    othello.up()
    othello.end_fill()

    othello.begin_fill()
    othello.color("black")
    othello.hideturtle()
    othello.up()
    othello.goto(45, -25)
    othello.down()
    othello.circle(20)
    othello.up()
    othello.end_fill()

####### second column #################
    othello.begin_fill()
    othello.color("white")
    othello.hideturtle()
    othello.up()
    othello.goto(-5, -25)
    othello.down()
    othello.circle(20)
    othello.up()
    othello.end_fill()

   
    othello.begin_fill()
    othello.color("black")
    othello.hideturtle()
    othello.up()
    othello.goto(-5, 25)
    othello.down()
    othello.circle(20)
    othello.up()
    othello.end_fill()



def draw_piece(item1, item2, color):

    othello = turtle.Turtle()
    othello.speed(0)
    
    othello.begin_fill()
    othello.color(color)
    othello.hideturtle()
    othello.up()
    othello.goto(item1, item2)
    othello.down()
    othello.circle(20)
    othello.up()
    othello.end_fill()


def draw_lines(turt, n):
    turt.pendown()
    turt.forward(SQUARE * n)
    turt.penup()


def change_players():

    global color
    
    if color == "white":
        color = "black"
    elif color == "black":
        color = "white"
    return color       


def check_total_moves(move1, move2):

        if move1 > move2:
            print("black wins")
        elif move1 < move2:
            print("white wins")
        elif move1 == move2:
            print("tie")
            
def color_increment(color):
    global white_counter
    global black_counter
    global total_moves_count
    
    if color == "white":
        white_counter += 1
        total_moves_count += 1
        
    elif color == "black":
        black_counter += 1
        total_moves_count += 1

    return [black_counter, white_counter]


def clicked(x, y):
    turtle.hideturtle()
    turtle.clear()
    grid_x = int(abs(x // SQUARE + 2))
    grid_y = int(abs(y  // SQUARE - 1))
    space = (grid_y, grid_x)
    global color
    global already_pressed

    space_grid = {(0,0):[-75,55],(0,1):[-25,55],(0,2):[25,55],
                  (0,3):[75,55],
                  (1,0):[-75,5], (1,3):[75,5],
                  (2,0):[-75,-45], (2,3):[75,-45],
                  (3,0):[-75,-95],(3,1):[-25,-95],(3,2):[25,-95]
                  ,(3,3):[75,-95]}

    quad_start = [(2,1),(2,2),(1,1),(1,2)]
    
    if space in already_pressed:
        print("you already pressed here")

    elif space not in space_grid.keys():
        print("out of bounds")
            
    elif space not in already_pressed:
        color = change_players()
        players_total = color_increment(color)
                   
        for key, value in space_grid.items():
            if space == key:
                draw_piece(value[0],value[1], color)
                already_pressed.append(key)
        
    if total_moves_count == 12:
        check_total_moves(players_total[0] ,players_total[1])

        
    
def click_on_board():
    turtle.onscreenclick(clicked)

   
def create_board():

    draw_board(4)
    click_on_board()
    

create_board()
