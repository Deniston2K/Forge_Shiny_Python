import turtle
import utils_for_random_shapes_and_color
from random import randint

t=turtle.Turtle()

sides=randint(3,8)

utils_for_random_shapes_and_color.move(t, 100, 100)
shape_color=utils_for_random_shapes_and_color.get_random_colors()
t.color(shape_color)
t.begin_fill()
utils_for_random_shapes_and_color.draw_polygon(t, sides, 100)
t.end_fill()
print("Yes!We've done it!")
turtle.done()