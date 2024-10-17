'''
Author: Sreshth Tiwari
Date: 14 October 2024
Purpose: Implement copy of Pong game using CS1Lib
'''

from cs1lib import *

paddle_movement_height = 10

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

ball_radius = 10
ball_x = screen_height/2
ball_y = screen_height/2

ball_direction_x = 1
ball_direction_y = 1
ball_velocity = 5

game_started = False
show_text = True

def main_draw():
    global show_text

    clear()

    draw_paddles()
    move_paddles()
    draw_ball()
    move_ball()
    set_clear_color(0,0,0)

    if show_text:
        set_stroke_color(1,1,1)
        set_font_size(14)
        draw_text("Press Spacebar to Start Game", screen_width/2 - 5.5*28, screen_height/2 - 100)


def draw_ball():
    global ball_x, ball_y, ball_radius
    draw_circle(ball_x, ball_y, ball_radius)

def move_ball():
    global ball_x, ball_y, game_started, ball_radius, right_paddle_x, left_paddle_x, paddle_width, ball_velocity, ball_direction_x, ball_direction_y

    if not game_started:
        return
    
    ball_x += ball_direction_x*ball_velocity
    ball_y += ball_direction_y*ball_velocity

    #if ball touches paddle
    if ball_x-ball_radius == right_paddle_x-paddle_width and right_paddle_y<=ball_y<=right_paddle_y+paddle_height:
        print(ball_x)
        ball_direction_x*=-1

    if ball_x-ball_radius == left_paddle_x+paddle_width and left_paddle_y<=ball_y<=left_paddle_y+paddle_height:
        print(ball_x)
        ball_direction_x*=-1

    #if ball touches up or down walls
    if ball_y+ball_radius == screen_height:
        ball_direction_y*=-1

    if ball_y-ball_radius == 0:
        ball_direction_y*=-1

    #if ball touches left or right walls
    if ball_x+ball_radius == screen_width:
        end_game()

    if ball_x-ball_radius == 0:
        end_game()


def draw_paddles():
    global screen_width, screen_height, paddle_height, paddle_width, right_paddle_x, right_paddle_y, left_paddle_x, left_paddle_y, right_up, right_down, left_up, left_down

    set_fill_color(1, 1, 1)

    draw_rectangle(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    draw_rectangle(right_paddle_x, right_paddle_y, paddle_width, paddle_height)    

def move_paddles():
    global left_down, left_up, right_down, right_up, left_paddle_y, right_paddle_y, paddle_height, paddle_movement_height

    if left_up and left_paddle_y>=0:
        left_paddle_y-=paddle_movement_height

    if left_down and left_paddle_y<=screen_height-paddle_height-paddle_movement_height:
        left_paddle_y+=paddle_movement_height

    if right_up and right_paddle_y>=0:
        right_paddle_y-=paddle_movement_height

    if right_down and right_paddle_y<=screen_height-paddle_height-paddle_movement_height:
        right_paddle_y+=paddle_movement_height

def handle_paddle_movements(key_pressed):
    global left_down, left_up, right_down, right_up

    if key_pressed == "a":
        left_up = True
    
    if key_pressed == "z":
        left_down = True

    if key_pressed == "k":
        right_up = True
    
    if key_pressed == "m":
        right_down = True

def start_game():
    global game_started, show_text
    show_text = False
    #some sort of countdown

    game_started = True

def end_game():
    global game_started, show_text,ball_x, ball_y, screen_width, screen_height, left_paddle_x, left_paddle_y, right_paddle_y, right_paddle_x

    ball_y = screen_height/2
    ball_x = screen_width/2
    
    left_paddle_x = 0
    left_paddle_y = 0

    right_paddle_x = screen_width - paddle_width
    right_paddle_y = screen_height - paddle_height

    show_text = True

    game_started = False

def handle_key_press(key_pressed):
    global screen_height, left_paddle_y, right_paddle_y, game_started

    if game_started:
        handle_paddle_movements(key_pressed)

    if key_pressed == "q":
        cs1_quit()

    if key_pressed == " ":
        start_game()

    if key_pressed == "o":
        end_game()

def handle_key_release(key_released):

    global left_down, left_up, right_down, right_up

    if key_released == "a":
        left_up = False
    
    if key_released == "z":
        left_down = False

    if key_released == "k":
        right_up = False
    
    if key_released == "m":
        right_down = False

start_graphics(main_draw, width=screen_width, height=screen_height, key_press=handle_key_press, key_release=handle_key_release)