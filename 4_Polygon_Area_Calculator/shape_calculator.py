class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self): # string representation of Square object
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    picture = ""
    for i in range(0, self.height):
      picture += "".rjust(self.width,"*") + "\n"

    return picture

  def get_amount_inside(self, shape):
      width_fit = self.width // shape.width
      height_fit = self.height // shape.height
      return width_fit * height_fit

class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)
    
  def __str__(self): # string representation of Square object
    return f"Square(side={self.height})"

  def set_side(self, side):
    self.height = side
    self.width = side

  def set_width(self,side):
    self.height = side
    self.width = side

  def set_height(self,side):
    self.height = side
    self.width = side