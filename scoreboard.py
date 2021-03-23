from turtle import Turtle

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.score = 0
    self.goto(x = 0, y = 250)
    self.pencolor("white")
    self.hideturtle()
    self.show_score()
 
   
  def add_score(self):
    self.score += 1
    self.clear()
 
     
  def show_score(self):
    self.write(f"Score : {self.score}", False, align = "center", font = ("Arial", 15, "bold"))
 
        
  def game_over(self):
    self.goto(0,0)
    self.write("Game over", False, align = "center", font = ("Arial", 15, "bold"))
  

    