class Point():
  def __init__(self, x, y):
    self.x, self.y = x, y
  def __sub__(self, other):
    dx = self.x - other.x
    dy = self.y - other.y
    return ((dx**2+dy**2))**0.5
  def __repr__(self):
    return 'Point({}, {})'.format(self.x, self.y)
# End class Point 

class Straight_line():
  def __init__(self, p1, p2):
    self.p1, self.p2 = p1, p2
    self.m, self.c = self.gradient, self.zero
  @property
  def gradient(self):
    dx = self.p2.x - self.p1.x
    dy = self.p2.y - self.p1.x
    if dx == 0:
      return float('inf')
    return dy / dx
  @property
  def zero(self):
    dx = self.p2.x - self.p1.x
    if dx == 0:
      return float('inf')
    return self.p1.y - self.gradient * self.p1.x
  def __repr__(self):
    return 'y = {} x + {}'.format(self.m, self.c)
#End class Straight_line

A = Point(0, 0)
B = Point(1, 1)
r = Straight_line(A, B)
print(r)
