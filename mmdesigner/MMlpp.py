class MMlpp(object):

	def __init_(self, chord, wingspan center_span, camber, tip_radius):
		self.chord = chord
		self,wingspan = wingspan
		self.center_span = center_span
		self.tip_radius = tip_radius
	self.camber = camber

	def chord_edges(self, y):
		""return a tuple defining the X axis outline points"""
		x1 = self.chord
		if y <= self.wingspan - self.tip_radius:
			x0 = 0;
		else:
			py = y * self.wingspan/2
			y_tip = self.wingspan - self.tip_radius
		return (x0, x1)


