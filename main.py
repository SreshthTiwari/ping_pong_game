from cs1lib import *

screen_height = 400
screen_width = 400

paddle_width = 20
paddle_height = 80

left_paddle_x = 0
left_paddle_y = 0

right_paddle_x = screen_width - paddle_width
right_paddle_y = screen_height - paddle_height

right_up = False
right_down = False

left_up = False
left_down = False

def main_draw():
    clear()

    draw_paddles()
    move_paddles()
    set_clear_color(0,0,0)

def draw_paddles():
    global screen_width, screen_height, paddle_height, paddle_width, right_paddle_x, right_paddle_y, left_paddle_x, left_paddle_y, right_up, right_down, left_up, left_down

    set_fill_color(1, 1, 1)

    draw_rectangle(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    draw_rectangle(right_paddle_x, right_paddle_y, paddle_width, paddle_height)    

def move_paddles():
    global left_down, left_up, right_down, right_up, left_paddle_y, right_paddle_y, paddle_height

    if left_up and left_paddle_y>=0:
        left_paddle_y-=5
        left_up = False

    if left_down and left_paddle_y<=screen_height-paddle_height:
        left_paddle_y+=5
        left_down = False

    if right_up and right_paddle_y>=0:
        right_paddle_y-=5
        right_up = False

    if right_down and right_paddle_y<=screen_height-paddle_height:
        right_paddle_y+=5
        print(right_paddle_y, screen_height)    
        right_down = False

def handle_key_press(key_pressed):
    global left_down, left_up, right_down, right_up, screen_height, left_paddle_y, right_paddle_y

    if key_pressed == "a":
        print("move up left")
        left_up = True
        left_down = False
    
    if key_pressed == "z":
        left_down = True
        print("move down left", left_down, left_paddle_y)
        left_up = False

    if key_pressed == "k":
        right_up = True
        print("move up right")
        right_down = False
    
    if key_pressed == "m":
        right_up = False
        print("move down right")
        right_down = True


start_graphics(main_draw, width=screen_width, height=screen_height, key_press=handle_key_press)