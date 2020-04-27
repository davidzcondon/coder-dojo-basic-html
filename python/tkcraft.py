from tkinter import *
from dataclasses import dataclass
import logging

@dataclass
class Point:
    x: int
    y: int

    def right(self, width):
        return Point(self.x + width, self.y)

    def left(self, width):
        return Point(self.x - width, self.y)

    def up(self, height):
        return Point(self.x, self.y - height)

    def down(self, height):
        return Point(self.x, self.y + height)

def create_line(canvas, point1, point2):
	return canvas.create_line(point1.x, point1.y, point2.x, point2.y)

def create_rectangle(canvas, point1, point2):
	return canvas.create_rectangle(point1.x, point1.y, point2.x, point2.y)

def create_rectangle_wh(canvas, point1, width, height, color="black"):
	return canvas.create_rectangle(point1.x, point1.y, point1.x + width, point1.y + height, outline=color)
	
logging.basicConfig(level=logging.DEBUG)

tk = Tk()
tk.title("TkCraft by David")

current_position = Point(0,0)

canvas = Canvas(tk, width=800, height=600)
canvas.pack()

BOX_WIDTH = 50
BOX_HEIGHT = 50
NUM_BOXES_IN_ROW = 12
NUM_ROWS = 10
START_GRID_X = 50
START_GRID_Y = 50

def draw_row(point, num_boxes):
	boxes = []
	for i in range (0, num_boxes):
		box = create_rectangle_wh(canvas, point, BOX_WIDTH, BOX_HEIGHT)
		boxes.append(box)
		point = point.right(BOX_WIDTH)
	return boxes

def draw_grid(point, num_rows, num_boxes_in_row):
	logging.debug("Drawing Grid")
	rows = []
	for i in range (0, num_rows):
		logging.debug("Drawing Row " + str(i))
		row = draw_row(point, num_boxes_in_row)
		rows.append(row)
		point = point.down(BOX_HEIGHT)
	return rows

grid = draw_grid(Point(START_GRID_X, START_GRID_Y), NUM_ROWS, NUM_BOXES_IN_ROW)


def move(event):
	global current_position
	global grid

	logging.debug("Entering Move Function " + str(event))

	if event.keysym == 'Up':
		current_position = Point(current_position.x, current_position.y - 1)		
		if current_position.y == -1:
			current_position.y = NUM_ROWS - 1			
		draw_selected_box_in_grid(grid, current_position)
	elif event.keysym == 'Down':
		draw_normal_box_in_grid(grid, current_position)
		current_position = Point(current_position.x, current_position.y + 1)		
		if current_position.y == NUM_ROWS:
			current_position.y = 0			
		draw_selected_box_in_grid(grid, current_position)
	elif event.keysym == 'Left':
		draw_normal_box_in_grid(grid, current_position)
		current_position = Point(current_position.x - 1, current_position.y)		
		if current_position.x == -1:
			current_position.x = NUM_BOXES_IN_ROW - 1			
		draw_selected_box_in_grid(grid, current_position)
	else:
		draw_normal_box_in_grid(grid, current_position)
		current_position = Point(current_position.x + 1, current_position.y)		
		if current_position.x == NUM_BOXES_IN_ROW:
			current_position.x = 0			
		draw_selected_box_in_grid(grid, current_position)


def draw_box_in_grid(grid, position, color):
	logging.debug("draw_box_in_grid position = " + str(position))
	row = grid[position.y]
	box = row[position.x]
	canvas.itemconfig(box, outline=color)
	canvas.lift(box, "all")


def draw_selected_box_in_grid(grid, position):
	logging.debug("draw_selected_box_in_grid " + str(position))
	draw_box_in_grid(grid, position, color="red")


def draw_normal_box_in_grid(grid, position):
	logging.debug("draw_normal_box_in_grid " + str(position))
	draw_box_in_grid(grid, position, color="black")


draw_selected_box_in_grid(grid, current_position)

canvas.bind_all('<KeyPress-Up>', move)
canvas.bind_all('<KeyPress-Down>', move)
canvas.bind_all('<KeyPress-Left>', move)
canvas.bind_all('<KeyPress-Right>', move)

logging.debug("Entering Mainloop Function")
tk.mainloop()



