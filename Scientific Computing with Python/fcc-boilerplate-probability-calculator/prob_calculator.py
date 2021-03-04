import copy
import random
# Consider using the modules imported above.

import collections

class Hat:
  def __init__(self, **balls):
    self.hat = balls
    self.contents = []
    for i in self.hat:
      for j in range(self.hat[i]): 
        self.contents.append(i)
    
  def draw(self, number):
    if len(self.contents) >= number:
      self.drawn = random.sample(self.contents, number)
    else:
      self.drawn = random.sample(self.contents, len(self.contents))    
    for i in self.drawn:
      if i in self.contents:
        self.contents.remove(i)
    return self.drawn

  def onlydraw(self, number):
    if len(self.contents) >= number:
      self.drawn = random.sample(self.contents, number)
    else:
      self.drawn = random.sample(self.contents, len(self.contents))    
    return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
  success = 0
  for i in range(num_experiments):
    result = True
    drawn_urn = (hat.onlydraw(num_balls_drawn)).copy()
    count = collections.Counter(drawn_urn)
    for j in expected_balls:
      if count[j] < expected_balls[j]:
        result = False
    if result is True:
      success += 1
        
  return success / num_experiments
