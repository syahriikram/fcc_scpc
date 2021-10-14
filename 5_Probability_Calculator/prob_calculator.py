import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs): # add in options for ball
    self.contents = []
    for key,value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_of_balls):
    if num_of_balls > len(self.contents):
        return self.contents
    
    balls_drawn = []
    for i in range(num_of_balls):
      picked_ball = random.choice(self.contents)
      balls_drawn.append(picked_ball)
      self.contents.remove(picked_ball)
      
    return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  match_count = 0

  for i in range(num_experiments):
    tmp_hat = copy.deepcopy(hat)
    balls_drawn = tmp_hat.draw(num_balls_drawn)
    dict_balls_drawn = {}

    for ball in balls_drawn:
      if ball not in dict_balls_drawn:
        dict_balls_drawn[ball] = 1
      else:
        dict_balls_drawn[ball] += 1
    
    check = False
    for key,value in expected_balls.items():
      if key in dict_balls_drawn.keys():
        if value <= dict_balls_drawn[key]:
          check = True
        else:
          check = False
          break
      else:
        check = False
        break

    if check:
      match_count += 1

  probability = match_count / num_experiments
  return probability
