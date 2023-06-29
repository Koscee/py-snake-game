from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    _segment_unit_width = 20
    _no_of_segment = 3

    def __init__(self):
        self.segments: list[Turtle] = []
        self._create()
        self.head = self.segments[0]

    def _create(self):
        for i in range(0, self._no_of_segment):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=-(i * self._segment_unit_width), y=0)
            self.segments.append(new_segment)

    def move(self):
        """moves snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            nxt_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(nxt_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
