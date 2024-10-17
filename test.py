from cs1lib import *

# Paddle settings
paddle_width = 10
paddle_height = 80
left_paddle_x = 30
right_paddle_x = 460
left_paddle_y = 200
right_paddle_y = 200
paddle_speed = 10

# Ball settings
ball_x = 250
ball_y = 250
ball_radius = 10
ball_speed_x = 2
ball_speed_y = 2

# Move paddles based on key input
def move_paddles():
    global left_paddle_y, right_paddle_y
    if is_key_pressed("w") and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if is_key_pressed("s") and left_paddle_y < 400 - paddle_height:
        left_paddle_y += paddle_speed
    if is_key_pressed("i") and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if is_key_pressed("k") and right_paddle_y < 400 - paddle_height:
        right_paddle_y += paddle_speed

# Update ball position and handle collisions
def move_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    
    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Check for collisions with top and bottom walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= 400:
        ball_speed_y *= -1
    
    # Check for collisions with left paddle
    if (ball_x - ball_radius <= left_paddle_x + paddle_width and 
        left_paddle_y <= ball_y <= left_paddle_y + paddle_height):
        ball_speed_x *= -1
    
    # Check for collisions with right paddle
    if (ball_x + ball_radius >= right_paddle_x and 
        right_paddle_y <= ball_y <= right_paddle_y + paddle_height):
        ball_speed_x *= -1
    
    # Reset ball if it goes off screen
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= 500:
        ball_x = 250
        ball_y = 250
        ball_speed_x *= -1  # Reverse direction

# Draw paddles, ball, and background
def draw():
    clear()  # Clear screen
    
    # Draw paddles
    set_fill_color(1, 1, 1)  # White paddles
    draw_rectangle(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    draw_rectangle(right_paddle_x, right_paddle_y, paddle_width, paddle_height)
    
    # Draw ball
    set_fill_color(1, 1, 1)  # White ball
    draw_circle(ball_x, ball_y, ball_radius)
    
    # Move paddles and ball
    move_paddles()
    move_ball()

# Start the game loop
start_graphics(draw, framerate=60, width=500, height=400, key_press=noop, key_release=noop)
