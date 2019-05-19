#classes
#init is basically a constructor, while self is the new object i'm creating similar to this

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)
