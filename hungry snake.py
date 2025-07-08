import turtle
import random

# Game settings
w = 500
h = 500
food_size = 10
delay = 100

# Directions
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Game state
running = False
paused = False
score = 0

def reset():
    global snake, snake_dir, food_position, score, running, paused
    snake = [[0, 0], [0, 20], [0, 40]]
    snake_dir = "up"
    score = 0
    update_score()
    food_position = get_random_food_position()
    food.goto(food_position)
    running = True
    paused = False
    move_snake()

def move_snake():
    global snake_dir, running, paused

    if not running or paused:
        return

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_dir][0]
    new_head[1] += offsets[snake_dir][1]

    # Collision with self
    if new_head in snake[:-1]:
        game_over()
        return

    snake.append(new_head)

    if not food_collision():
        snake.pop(0)

    # Border wrapping
    if snake[-1][0] > w / 2:
        snake[-1][0] -= w
    elif snake[-1][0] < -w / 2:
        snake[-1][0] += w
    elif snake[-1][1] > h / 2:
        snake[-1][1] -= h
    elif snake[-1][1] < -h / 2:
        snake[-1][1] += h

    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    screen.update()
    turtle.ontimer(move_snake, delay)

def food_collision():
    global food_position, score
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        score += 1
        update_score()
        return True
    return False

def update_score():
    score_writer.clear()
    score_writer.goto(-w//2 + 10, h//2 - 30)
    score_writer.write(f"Score: {score}", align="left", font=("Arial", 16, "bold"))

def get_random_food_position():
    x = random.randint(-w // 2 + food_size, w // 2 - food_size)
    y = random.randint(-h // 2 + food_size, h // 2 - food_size)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

# Controls
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

def toggle_pause():
    global paused, running
    if not running:
        reset()
    else:
        paused = not paused
        if not paused:
            move_snake()

def game_over():
    global running
    running = False
    pen.clearstamps()
    game_writer.goto(0, 0)
    game_writer.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
    screen.update()

# Screen setup
screen = turtle.Screen()
screen.setup(w, h)
screen.title("🐍 Enhanced Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Snake pen
pen = turtle.Turtle("square")
pen.color("lime")
pen.penup()

# Food
food = turtle.Turtle()
food.shape("square")
food.color("yellow")
food.shapesize(food_size / 20)
food.penup()

# Score display
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("white")
score_writer.penup()

# Game over writer
game_writer = turtle.Turtle()
game_writer.hideturtle()
game_writer.color("red")
game_writer.penup()

# Key bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(toggle_pause, "space")

# Start message
game_writer.goto(0, 0)
game_writer.write("Press SPACE to Start", align="center", font=("Arial", 20, "bold"))
screen.update()

turtle.done()
