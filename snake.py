from turtle import Turtle
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
  
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
    
    
  def create_snake(self):
    x_position = 0
    for i in range(3):
      segment = Turtle(shape = "square")
      segment.color("white")
      segment.penup()
      segment.goto(x= x_position, y=0)
      self.segments.append(segment)
      x_position -= 20
      
  
  #extend when snake ate food    
  def extend(self):
      segment = Turtle(shape = "square")
      segment.color("white")
      segment.penup()
      segment.goto(self.segments[-1].position())
      self.segments.append(segment)
      

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num -1].xcor()
      new_y = self.segments[seg_num -1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
      
    self.head.forward(MOVE_DISTANCE)
  
  #define control of snake 
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
    
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
  
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
    