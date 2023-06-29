from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    _segment_unit_width = 20
    _initial_segment_count = 3

    def __init__(self):
        self.segments: list[Turtle] = []
        self._create()
        self.head = self.segments[0]

    def _create(self):
        for i in range(0, self._initial_segment_count):
            position = (-(i * self._segment_unit_width), 0)
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """adds a new segment to the snake."""
        self.add_segment(self.segments[-1].pos())

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
