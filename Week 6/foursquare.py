import turtle

SQUARE = 50
SPACE_GRID = {(0,0):[-75,55],(0,1):[-25,55],(0,2):[25,55],
              (0,3):[75,55],
              (1,0):[-75,5], (1,3):[75,5],
              (2,0):[-75,-45], (2,3):[75,-45],
              (3,0):[-75,-95],(3,1):[-25,-95],(3,2):[25,-95]
              ,(3,3):[75,-95]}

QUAD_START = [(2,1),(2,2),(1,1),(1,2)]


class Board: 

    def __init__(self):
        
        self.already_pressed = []

    def draw_four_disks(self,othello):
        white_x = 45
        white_y = 25
        black_x = 45
        black_y = -25
        for i in range(2): 
            othello.begin_fill()
            othello.color("white")
            othello.hideturtle()
            othello.up()
            othello.goto(white_x, white_y)
            othello.down()
            othello.circle(20)
            othello.up()
            othello.end_fill()
            white_x = white_x - SQUARE
            white_y = white_y - SQUARE
   
        for i in range(2): 
            othello.begin_fill()
            othello.color("black")
            othello.hideturtle()
            othello.up()
            othello.goto(black_x, black_y)
            othello.down()
            othello.circle(20)
            othello.up()
            othello.end_fill()
            black_x = black_x - SQUARE
            black_y = black_y + SQUARE


    def draw_bg(self, othello, n):
               
        othello.begin_fill()
        for i in range(4):
            othello.pendown()
            othello.forward(SQUARE * n)
            othello.left(90)
        othello.end_fill()


    def draw_vert_hor_lines(self, othello, n, corner):
        # Draw the horizontal lines
        for i in range(n + 1):
            othello.setposition(corner, SQUARE * i + corner)
            self.draw_lines(othello, n)

        # Draw the vertical lines
        othello.left(90)
        for i in range(n + 1):
            othello.setposition(SQUARE * i + corner, corner)
            self.draw_lines(othello, n)

       
    def draw_board(self,n):
        
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

        self.draw_bg(othello,n)
        self.draw_vert_hor_lines(othello, n, corner)
        self.draw_four_disks(othello)


    def draw_piece(self, item1, item2, color):

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


    def draw_lines(self,turt, n):
        turt.pendown()
        turt.forward(SQUARE * n)
        turt.penup()

class Players:
    
    def __init__(self):
        self.color = "white"

        
    def change_players(self):

        if self.color == "white":
            self.color = "black"
        elif self.color == "black":
            self.color = "white"
            
        return self.color       


class Moves:
    
    def __init__(self):
        self.white_counter = 0
        self.black_counter = 0
        self.total_moves_count = 0
    
    def check_total_moves(self, move1, move2):

            if move1 > move2:
                print("black wins")
            elif move1 < move2:
                print("white wins")
            elif move1 == move2:
                print("tie")
                
    def color_increment(self, color):

        if color == "white":
            self.white_counter += 1
            self.total_moves_count += 1
            
            
        elif color == "black":
            self.black_counter += 1
            self.total_moves_count += 1
            print(self.total_moves_count)
                      
        return [self.black_counter, self.white_counter]

class Game:

    def __init__(self):
        self.board = Board()
        self.players = Players()
        self.moves = Moves()
    
    def clicked(self, x, y):
        turtle.hideturtle()
        turtle.clear()
        grid_x = int(abs(x // SQUARE + 2))
        grid_y = int(abs(y  // SQUARE - 1))
        space = (grid_y, grid_x)
        color = self.players.color
        already_pressed = self.board.already_pressed
        players_total = [0,0]
        
        if space in already_pressed:
            print("you already pressed here")

        elif space not in SPACE_GRID.keys():
            print("out of bounds")
                
        elif space not in already_pressed:
            color = self.players.change_players()
            players_total = self.moves.color_increment(color)

                       
            for key, value in SPACE_GRID.items():
                if space == key:
                    self.board.draw_piece(value[0],value[1], color)
                    already_pressed.append(key)
            
        if self.moves.total_moves_count == 12:
            self.moves.check_total_moves(players_total[0] ,players_total[1])
        

            
        
    def click_on_board(self):
        
        turtle.onscreenclick(self.clicked)

       
    def create_board(self):

        self.board.draw_board(4)
        self.click_on_board()
        

def main():

    game = Game()
    game.create_board()



main()

