import robot3
import math 

class Geometry():
	"""
		module servant à calculer la position relative à sa position initiale
	"""
	def __init__(self,Robot):
		self.Rob = Robot
		self.x = 0
		self.y = 0
		self.z = 0 
		self.n = 1 
		self.points = ()
		self.addPoint()
		self.edge = ()

	def Update(self):
		# self.x += self.Rob.prevMove*(math.cos(self.Rob.yaw)+math.sin(self.Rob.pitch))
		# self.y += self.Rob.prevMove*(math.sin(self.Rob.yaw)+math.cos(self.Rob.roll))
		# self.z += self.Rob.prevMove*(math.sin(self.Rob.roll)+math.cos(self.Rob.pitch))


		
		projXyPrevMove = self.Rob.prevMove*(math.cos(self.Rob.pitch))

		self.x += projXyPrevMove*(math.cos(self.Rob.yaw))
		self.y += projXyPrevMove*(math.sin(self.Rob.yaw))
		self.z += self.Rob.prevMove*(math.sin(self.Rob.pitch))
		

		""" --------- !!!!! Partie du code à effacer si il n'y a pas un petit mouvement de rotation !!!!! ----------
		                          sur le module central lors d'un virage 
		"""
		if self.Rob.direct == "f":
			if self.Rob.angles[0] != 0:
				print("does smth")
				self.x += 0.25*math.cos(self.Rob.angles[0])
				self.y += (0.25*math.sin(self.Rob.angles[0]))*math.cos(self.Rob.roll)
				self.z += (0.25*math.sin(self.Rob.angles[0]))*math.sin(self.Rob.roll)
		elif self.Rob.angles[1] != 0:
			if self.Rob.angles[1] != 0:
				print("does smth")
				self.x += 0.25*math.cos(self.Rob.angles[1])
				self.y += (0.25*math.sin(self.Rob.angles[1]))*math.cos(self.Rob.roll)
				self.z += (0.25*math.sin(self.Rob.angles[1]))*math.sin(self.Rob.roll)
		""" --------------------------------------------------------------------------------------------"""
		
		self.addPoint()
		if len(self.points)>=2:
			self.addEdge()


		

	def displayCoords(self):
		print("x = "+str(round(self.x)))
		print("y = "+str(round(self.y)))
		print("z = "+str(round(self.z)))

	def addPoint(self):
		#self.points += ((self.x/10,self.y/10,self.z/10),)
		self.points += ((self.y/10,self.z/10,self.x/10),)

	def addEdge(self):
		self.edge += ((self.n-1,self.n),) 
		self.n+=1

