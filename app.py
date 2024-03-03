import turtle
import random

width = 500
length = 500
food_size = 15
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
    snake_dir = "right"
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
        if snake[-1][0] > width / 2:
            snake[-1][0] -= width
        elif snake[-1][0] < - width / 2:
            snake[-1][0] += width
        elif snake[-1][1] > length / 2:
            snake[-1][1] -= length
        elif snake[-1][1] < -length / 2:
            snake[-1][1] += length

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
    x = random.randint(- width / 2 + food_size, width / 2 - food_size)
    y = random.randint(- length / 2 + food_size, length / 2 - food_size)
    return (x, y)


def get_distance(initial, final):
    initial_x, initial_y = initial
    final_x, final_y = final
    distance = ((final_y - initial_y) ** 2 + (final_x - initial_x) ** 2) ** 0.5
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


screen = turtle.Screen()
screen.setup(width, length)
screen.title("Snake Xenia")
screen.bgcolor("white")
screen.setup(700, 500)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(food_size / 20)
food.penup()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
turtle.done()
