'''
Author: Sreshth Tiwari
Date: 14 October 2024
Purpose: Implement copy of Pong game using CS1Lib
'''

from cs1lib import *
import time


# ideas
# changing colors, ball speed increases, score counter, countdown

player_one_score = 0
player_two_score = 0

r_value = 1
g_value = 1
b_value = 1

# defining important variables

UP_LEFT_KEY = "a"
UP_RIGHT_KEY = "k"
DOWN_LEFT_KEY = "z"
DOWN_RIGHT_KEY = "m"

PADDLE_MOVEMENT_HEIGHT = 10

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80

left_paddle_x = 0
left_paddle_y = 0

right_paddle_x = SCREEN_WIDTH - PADDLE_WIDTH
right_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT

right_up = False
right_down = False

left_up = False
left_down = False

BALL_RADIUS = 10
ball_x = SCREEN_HEIGHT/2
ball_y = SCREEN_HEIGHT/2

ball_direction_x = 1
ball_direction_y = 1
BALL_VELOCITY = 10

game_started = False
show_text = True

def main_draw():
    global show_text, BALL_VELOCITY

    clear()
    set_clear_color(0.2,0.2, 0.2)

    draw_scoreboard_and_details()

    draw_paddles()
    move_paddles()

    draw_ball()
    move_ball()
    
    #checking to see if game is over and start text needs to be displayed
    if show_text:
        set_stroke_color(1,1,1)
        set_font_size(14)
        draw_text("Press Spacebar to Start Game", SCREEN_WIDTH/2 - 5.5*28, SCREEN_HEIGHT + 60)

def draw_scoreboard_and_details():
    global SCREEN_HEIGHT, SCREEN_WIDTH
    set_stroke_color(1, 1, 1)
    
    # half line
    draw_line(int(SCREEN_WIDTH/2), 0, int(SCREEN_WIDTH/2), SCREEN_HEIGHT)

    # score
    set_font_size(30)
    draw_text(str(player_one_score), int(SCREEN_WIDTH/2)-50, 50)
    draw_text(str(player_two_score), int(SCREEN_WIDTH/2)+20, 50)

    # bottom divide
    draw_line(0, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)

def draw_ball():
    global ball_x, ball_y, BALL_RADIUS, r_value, g_value, b_value

    set_fill_color(r_value, g_value, b_value)

    draw_circle(ball_x, ball_y, BALL_RADIUS)

def move_ball():
    global ball_x, ball_y, game_started, BALL_RADIUS, right_paddle_x, left_paddle_x, PADDLE_WIDTH, BALL_VELOCITY, ball_direction_x, ball_direction_y, player_one_score, player_two_score

    # dont do anything if game hasn't started
    if not game_started:
        return
    
    # move the ball by updating its x and y coordinates
    ball_x += ball_direction_x*BALL_VELOCITY
    ball_y += ball_direction_y*BALL_VELOCITY

    # check if ball touches right paddle
    if ball_x-BALL_RADIUS == right_paddle_x-PADDLE_WIDTH and right_paddle_y<=ball_y<=right_paddle_y+PADDLE_HEIGHT:
        print(ball_x)
        ball_direction_x*=-1

    # check if ball touches left paddle
    if ball_x-BALL_RADIUS == left_paddle_x+PADDLE_WIDTH and left_paddle_y<=ball_y<=left_paddle_y+PADDLE_HEIGHT:
        print(ball_x)
        ball_direction_x*=-1

    # check if ball touches up or down walls
    if ball_y+BALL_RADIUS == SCREEN_HEIGHT:
        ball_direction_y*=-1

    if ball_y-BALL_RADIUS == 0:
        ball_direction_y*=-1

    #if ball touches left or right walls
    if ball_x+BALL_RADIUS == SCREEN_WIDTH:
        time.sleep(0.2)
        player_one_score+=1
        end_game()

    if ball_x-BALL_RADIUS == 0:
        time.sleep(0.2)
        player_two_score+=1
        end_game()

def draw_paddles():
    global SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_HEIGHT, PADDLE_WIDTH, right_paddle_x, right_paddle_y, left_paddle_x, left_paddle_y, right_up, right_down, left_up, left_down, r_value, g_value, b_value

    set_fill_color(r_value, g_value, b_value)

    # draw left paddle
    draw_rectangle(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # draw right paddle
    draw_rectangle(right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)    

def move_paddles():
    global left_down, left_up, right_down, right_up, left_paddle_y, right_paddle_y, PADDLE_HEIGHT, PADDLE_MOVEMENT_HEIGHT

    # move left paddle up
    if left_up and left_paddle_y>=0:
        left_paddle_y-=PADDLE_MOVEMENT_HEIGHT

    # move left paddle down
    if left_down and left_paddle_y<=SCREEN_HEIGHT-PADDLE_HEIGHT-PADDLE_MOVEMENT_HEIGHT:
        left_paddle_y+=PADDLE_MOVEMENT_HEIGHT

    # move right paddle up
    if right_up and right_paddle_y>=0:
        right_paddle_y-=PADDLE_MOVEMENT_HEIGHT

    # move right paddle down
    if right_down and right_paddle_y<=SCREEN_HEIGHT-PADDLE_HEIGHT-PADDLE_MOVEMENT_HEIGHT:
        right_paddle_y+=PADDLE_MOVEMENT_HEIGHT

def handle_paddle_movements(key_pressed):
    global left_down, left_up, right_down, right_up

    if key_pressed == UP_LEFT_KEY:
        left_up = True
    
    if key_pressed == DOWN_LEFT_KEY:
        left_down = True

    if key_pressed == UP_RIGHT_KEY:
        right_up = True
    
    if key_pressed == DOWN_RIGHT_KEY:
        right_down = True

def start_game():
    global game_started, show_text, left_paddle_x, left_paddle_y, right_paddle_x, right_paddle_y, SCREEN_WIDTH, PADDLE_WIDTH, SCREEN_HEIGHT, PADDLE_HEIGHT

    show_text = False
    game_started = True

    left_paddle_x = 0
    left_paddle_y = 0

    right_paddle_x = SCREEN_WIDTH - PADDLE_WIDTH
    right_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT

def end_game():
    global game_started, show_text,ball_x, ball_y, SCREEN_WIDTH, SCREEN_HEIGHT, left_paddle_x, left_paddle_y, right_paddle_y, right_paddle_x, BALL_VELOCITY

    ball_y = SCREEN_HEIGHT/2
    ball_x = SCREEN_WIDTH/2
    
    left_paddle_x = 0
    left_paddle_y = 0

    right_paddle_x = SCREEN_WIDTH - PADDLE_WIDTH
    right_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT

    set_stroke_color(1,1,1)
    set_font_size(14)
    draw_text("Game Over", SCREEN_WIDTH/2 - 5.5*28, SCREEN_HEIGHT + 60)

    show_text = True
    game_started = False

def handle_key_press(key_pressed):
    global SCREEN_HEIGHT, left_paddle_y, right_paddle_y, game_started

    if game_started:
        handle_paddle_movements(key_pressed)

    if key_pressed == "q":
        cs1_quit()

    if key_pressed == " ":
        start_game()

def handle_key_release(key_released):
    global left_down, left_up, right_down, right_up

    if key_released == UP_LEFT_KEY:
        left_up = False
    
    if key_released == DOWN_LEFT_KEY:
        left_down = False

    if key_released == UP_RIGHT_KEY:
        right_up = False
    
    if key_released == DOWN_RIGHT_KEY:
        right_down = False

start_graphics(main_draw, width=SCREEN_WIDTH, height=SCREEN_HEIGHT+100, key_press=handle_key_press, key_release=handle_key_release)