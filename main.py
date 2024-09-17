import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FOOD_DISTANCE, WALL_DISTANCE, SNAKE_DISTANCE

if __name__ == '__main__':

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < FOOD_DISTANCE:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if (snake.head.xcor() > WALL_DISTANCE or snake.head.xcor() < -WALL_DISTANCE
                or snake.head.ycor() > WALL_DISTANCE or snake.head.ycor() < -WALL_DISTANCE):
            scoreboard.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < SNAKE_DISTANCE:
                scoreboard.reset()
                snake.reset()  

    screen.exitonclick()
