class Rectangle:
  def __init__ (self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.height < 50 and self.width < 50:
      picture = ""
      for i in range(self.height):
        for j in range(self.width):
          if j < self.width - 1:
            picture += "*"
          else:
            picture += "*\n"
      return picture
    else:
      return "Too big for picture."

  def get_amount_inside(self, fit):
    nwidth = self.width // fit.width
    nheight = self.height // fit.height
    return nwidth * nheight

  def __str__(self):
    line = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return line


class Square(Rectangle):
  def __init__(self, side, height=None):
    Rectangle.__init__(self, side, height=None)
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    line = "Square(side=" + str(self.width) + ")"
    return line
