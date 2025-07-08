# Hungry-Snake-Game
🎮 A classic Snake game built with Python Turtle — includes scoring, pause/resume, game over screen, and wrap-around world. Simple, fun, and beginner-friendly!
# 🐍 Snake Game – Python Turtle Edition

An enhanced version of the classic Snake game built using Python's `turtle` module. This project includes a scoring system, wrap-around borders, game over detection, and pause/start functionality.

---

## 🎮 Features

- ✅ **Classic Snake Movement**
- 🎯 **Food Collection and Growth**
- 🧠 **Self-Collision Detection**
- 🧾 **Score Tracking**
- ⏯ **Pause / Resume Support** (`Spacebar`)
- 🪙 **Start Screen and Game Over Display**
- 🔄 **Wrap-around World (no walls)**

---

## 🖥️ Requirements

- Python 3.x
- No external libraries required – uses built-in `turtle` and `random`

---

## 🚀 How to Run

1. Clone or download this repository.
2. Navigate to the project folder.
3. Run the game using:

```bash
python snake_game_enhanced.py
```

🎮 Controls

| Key   | Action             |
| ----- | ------------------ |
| ↑     | Move Up            |
| ↓     | Move Down          |
| ←     | Move Left          |
| →     | Move Right         |
| Space | Start / Pause Game |


You said:
Debug: import turtle
import random
 
w = 500
h = 500
food_size = 10
delay = 100
 
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}
 
def reset():
    global snake, snake_dir, food_position, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()
     
def move_snake():
    global snake_dir
 
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
 
     
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
 
     
        if not food_collision():
            snake.pop(0)
 
 
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
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
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False
 
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)
 
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance
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
    if snake_dir!= "up":
        snake_dir = "down"
 
def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"
 
 
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("blue")
screen.setup(500, 500)
screen.tracer(0)
 
 
pen = turtle.Turtle("square")
pen.penup()
 
 
food = turtle.Turtle()
food.shape("square")
food.color("yellow")
food.shapesize(food_size / 20)
food.penup()
 
 
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
 
 
reset()
turtle.done()


ChatGPT said:
Your Snake game code is mostly solid, but it has a critical bug that causes the following error at runtime:

❌ Error:
python
Copy
Edit
ValueError: non-integer stop for randrange()
This is caused by this line in the get_random_food_position() function:

python
Copy
Edit
x = random.randint(- w / 2 + food_size, w / 2 - food_size)
The problem is that you're passing floating-point numbers (because / in Python 3 always returns float) into random.randint(), which requires integers.

✅ Fix:
Change all / to // (integer division) in these lines:

python
Copy
Edit
x = random.randint(- w // 2 + food_size, w // 2 - food_size)
y = random.randint(- h // 2 + food_size, h // 2 - food_size)
🛠 Updated get_random_food_position() function:
python
Copy
Edit
def get_random_food_position():
    x = random.randint(- w // 2 + food_size, w // 2 - food_size)
    y = random.randint(- h // 2 + food_size, h // 2 - food_size)
    return (x, y)
✅ Optional Improvement:
You're calling screen.setup(500, 500) twice:

python
Copy
Edit
screen.setup(w, h)
...
screen.setup(500, 500)
You can safely remove the second one to avoid redundancy.

Let me know if you'd like any improvements like:

scoring system

game over message

restart key

increasing speed as snake grows









You said:
give the rectified code


ChatGPT said:
Here is your fully rectified Snake game code with the integer division bug fixed and unnecessary duplicate setup removed:

python
Copy
Edit
import turtle
import random
 
w = 500
h = 500
food_size = 10
delay = 100
 
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}
 
def reset():
    global snake, snake_dir, food_position, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()
     
def move_snake():
    global snake_dir
 
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
 
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
 
        if not food_collision():
            snake.pop(0)
 
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
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
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False
 
def get_random_food_position():
    x = random.randint(- w // 2 + food_size, w // 2 - food_size)
    y = random.randint(- h // 2 + food_size, h // 2 - food_size)
    return (x, y)
 
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

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
 
# Setup screen
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("blue")
screen.tracer(0)
 
# Create pen
pen = turtle.Turtle("square")
pen.penup()
 
# Create food
food = turtle.Turtle()
food.shape("square")
food.color("yellow")
food.shapesize(food_size / 20)
food.penup()
 
# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
 
# Start game
reset()
turtle.done()
✅ Fixes and Improvements:
Replaced / with // in random.randint(...) to ensure integers.

Removed duplicate screen.setup(500, 500) call.

Clean formatting and consistency for better readability.

Let me know if you'd like to:

Add a scoring system

Display "Game Over" when snake hits itself

Add a start screen or pause/resume feature









You said:
Add a scoring system

Display "Game Over" when snake hits itself

Add a start screen or pause/resume feature


ChatGPT said:
Here is your enhanced Snake game with the following features added:

✅ New Features Added:
Scoring System – Tracks score and displays it on screen.

Game Over Display – Shows a “Game Over” message on collision.

Start Screen + Pause/Resume – Press Space to start or pause/resume the game.

🐍 Full Enhanced Code:
python
Copy
Edit
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
🕹 Controls:
Arrow Keys → Move the snake.

Space → Start or pause/resume the game.

Let me know if you'd like to:

Add a high score tracker

Add sound effects

Add walls instead of wrap-around

Customize colors, speed, or controls

Want a .py file version or GitHub readme too?









You said:
.py version


ChatGPT said:
Your enhanced Snake game has been saved as a .py file.

👉 Click here to download it

Let me know if you'd like a GitHub README, a .zip version with assets, or instructions to run it on Windows or Linux. 









You said:
github readme


ChatGPT said:
Here's a clean and professional GitHub README.md for your enhanced Snake game project:

📄 README.md
markdown
Copy
Edit
# 🐍 Snake Game – Python Turtle Edition

An enhanced version of the classic Snake game built using Python's `turtle` module. This project includes a scoring system, wrap-around borders, game over detection, and pause/start functionality.

---

## 🎮 Features

- ✅ **Classic Snake Movement**
- 🎯 **Food Collection and Growth**
- 🧠 **Self-Collision Detection**
- 🧾 **Score Tracking**
- ⏯ **Pause / Resume Support** (`Spacebar`)
- 🪙 **Start Screen and Game Over Display**
- 🔄 **Wrap-around World (no walls)**

---

## 🖥️ Requirements

- Python 3.x
- No external libraries required – uses built-in `turtle` and `random`

---

## 🚀 How to Run

1. Clone or download this repository.
2. Navigate to the project folder.
3. Run the game using:

```bash
python snake_game_enhanced.py
🎮 Controls
Key	Action
↑	Move Up
↓	Move Down
←	Move Left
→	Move Right
Space	Start / Pause Game
```


🧩 Future Enhancements (Optional Ideas)

💾 High Score Saving

🔊 Sound Effects

🌈 Themes / Skins

🧱 Walls and Difficulty Modes

📱 Mobile / Web version (via Kivy or Pygame.js)


🛠️ Built With

Python

turtle graphics module

📄 License

This project is open source and free to use under the MIT License.

🙋‍♀️ Author

Made with ❤️ by Krishika Singh – contributions welcome!
