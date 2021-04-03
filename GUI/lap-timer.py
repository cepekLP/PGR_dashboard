import time

class LapTimer():
	def __init__(self, x1, y1, x2, y2):
		if x1 > x2:
			self.x1 = x1
			self.x2 = x2
		else:
			self.x1 = x2
			self.x2 = x1

		self.a = x1 * y2 - y1 * x2
		self.b = x1 - x2
		self.c = y1 - y2

		self.time = 0.0
		self.last_time = 0.0
		self.best_time = 0.0

		self.lap_counter = 0
		self.last_x = 0.0
		self.last_y = 0.0

	
	def init_position(x, y):
		self.last_x = x
		self.last_y = y


	def check(x, y):
		a = self.last_x * y - self.last_y * x
		b = self.last_x - x
		c = last_y - y
		d = last_x - x
		e = self.b * c - self.c * d

		cross_x = (self.a * b - self.b * a) / e

		if cross_x >= self.x1 and cross_x <= self.x2:
			self.last_time = time.gmtime() - self.time
			self.time = time.gmtime()			
			if self.last_time < self.best_time or self.lap_counter == 0 : self.best_time = self.last_time
			self.lap_counter+=1

		self.last_x = x
		self.last_y = y

		return (self.time, self.last_time, self.best_time, self.lap_counter)

