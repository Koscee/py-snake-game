from turtle import Turtle

Y_POSITION = 280
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class ScoreBoard(Turtle):
    _score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=Y_POSITION)
        self._display_score()

    def _display_score(self):
        self.clear()
        self.write(f"Score: {self._score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self._score += 2
        self._display_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)