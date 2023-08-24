from turtle import Turtle

Y_POSITION = 280
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


def _get_high_score():
    with open("data.txt") as data:
        content = data.read()
        return int(content) if content.isdigit() else 0


def _save_high_score(score):
    with open("data.txt", mode="w") as data:
        data.write(str(score))


class ScoreBoard(Turtle):
    _score = 0

    def __init__(self):
        super().__init__()
        self._high_score = _get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=Y_POSITION)
        self._display_score()

    def _display_score(self):
        self.clear()
        self.write(f"Score: {self._score} High Score: {self._high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self._score += 2
        self._display_score()

    def reset(self):
        if self._score > self._high_score:
            self._high_score = self._score
            _save_high_score(self._high_score)
        self._score = 0
        self._display_score()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
