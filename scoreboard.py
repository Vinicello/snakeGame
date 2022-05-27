from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()
        self.speed("fastest")

    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = ALIGNMENT, font = FONT)