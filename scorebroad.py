from turtle import Turtle


class ScoreBroad(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-7, 275)

        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 16, "normal"))

    def increment(self):
        self.clear()
        self.score += 1
        self.update_score()
