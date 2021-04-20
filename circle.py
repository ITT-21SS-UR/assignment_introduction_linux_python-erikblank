import turtle
import time
import sys

rad = 0
step = 1

def goto_left_down_corner():
    turtle.pu()
    turtle.goto(0, -rad)
    turtle.pd()
    turtle.goto(-rad, -rad)
    turtle.goto(-rad, 0)
    
def goto_right_down_corner():
    turtle.goto(rad, -rad)
    turtle.goto(rad, 0)
    
def goto_right_top_corner():
    turtle.goto(rad, rad)
    turtle.goto(0, rad)
    turtle.goto(rad, rad)
    turtle.goto(rad, 0)
    
def goto_left_top_corner():
    turtle.goto(-rad, rad)
    turtle.goto(-rad, 0)


def draw_corner(x_start, y_start, x_dir, y_dir):
    count = 1
    while count != rad:
        turtle.goto(x_start+count*x_dir, rad*y_dir)
        turtle.goto(x_start+count*x_dir + step*x_dir, rad*y_dir)
        turtle.goto(x_start, y_start+count*y_dir)
        turtle.goto(x_start, y_start+count*y_dir + step*x_dir)
        count = count + step


if __name__ == "__main__":
    rad = int(sys.argv[1])
    goto_left_down_corner()
    draw_corner(-rad, 0, 1, -1) 
    goto_right_down_corner()
    draw_corner(rad, 0, -1, -1)
    goto_right_top_corner()
    draw_corner(rad, 0, -1, 1)
    goto_left_top_corner()
    draw_corner(-rad, 0, 1, 1)
    
    time.sleep(2)



