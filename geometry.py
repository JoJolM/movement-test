import robot2
import math 

class Geometry():
	def __init__(self,Robot):
		print("uuuuu")
		self.Rob = Robot
		self.x = 0
		self.y = 0
		self.z = 0 

	def Update(self):
		print("lolsdfq")
		# self.x += self.Rob.prevMove*(math.cos(self.Rob.yaw)+math.sin(self.Rob.pitch))
		# self.y += self.Rob.prevMove*(math.sin(self.Rob.yaw)+math.cos(self.Rob.roll))
		# self.z += self.Rob.prevMove*(math.sin(self.Rob.roll)+math.cos(self.Rob.pitch))

		
		projXyPrevMove = self.Rob.prevMove*(math.cos(self.Rob.pitch))

		self.x += projXyPrevMove*(math.cos(self.Rob.yaw))
		self.y += projXyPrevMove*(math.sin(self.Rob.yaw))
		self.z += self.Rob.prevMove*(math.sin(self.Rob.pitch))

		

	def displayCoords(self):
		print("lolsdfq45")
		print("x = "+str(self.x))
		print("y = "+str(self.y))
		print("z = "+str(self.z))

