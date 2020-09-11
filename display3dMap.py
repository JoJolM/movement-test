import pygame as pg 
import math


class Cube():
	"""docstring for Cube"""
	def __init__(self):
		
		self.points = ()
		self.edges = ()
		self.surfaces = (
			(0,1,2,3),
			(3,2,7,6),
			(6,7,5,4),
			(4,5,1,0),
			(1,5,7,2),
			(4,0,3,6)
			)
		self.generateCube(50)

	def addPoint(self,x,y,z):
		self.points += ((x,y,z),)

	def showPoints(self):
		print(self.points)

	def addEdge(self,Edge_1,Edge_2):
		self.edges+=((Edge_1,Edge_2),)

	def generateCube(self,cube_size):
		m=0
		n=3
		o=4
		for i in range(0,8):
			self.addPoint(((-1)**(m//2))*cube_size,((-1)**(n//2))*cube_size,((-1)**(o//4))*cube_size)
			m+=1
			if n<8:
				n+=1
			else:
				n+=2
			o+=1

		#self.showPoints()

		self.addEdge(0,1)
		self.addEdge(0,3)
		self.addEdge(0,4)
		self.addEdge(2,1)
		self.addEdge(2,3)
		self.addEdge(2,7)
		self.addEdge(6,3)
		self.addEdge(6,4)
		self.addEdge(6,7)
		self.addEdge(5,1)
		self.addEdge(5,4)
		self.addEdge(5,7)


class Cone():
	def __init__(self): #,ox,oy,oz,roll,pitch,yaw
		self.points= ()
		self.edge = () #16 arrètes 
		self.surfaces = ()		
		# self.roll = roll 
		# self.pitch = pitch
		# self.yaww = yaw
		
		self.generatePoints(.25,16)

	def generatePoints(self,r,res): #génère les points 
		angle = 2*math.pi / res
		self.addPoint(0,0,2*r)
		for n in range(0,res+1):
			self.addPoint(r*math.cos(n*angle),r*math.sin(n*angle),0)
		self.genEdge(res)
		self.genSurfaces(res)
		# print(self.points)
		# print(self.edge)

	def addPoint(self,x,y,z):
		self.points += ((x,y,z),)

	def genEdge(self,res):
		for n in range(2,res+1):
			self.edge += ((n-1,n),) 
		self.edge += ((res,1),)
		for n in range(1,res+1):
			self.edge += ((0,n),)

	def genSurfaces(self,res):
		surface_finale = ()
		for n in range(1,res+1):
			self.surfaces += ((0,n,n+1),)

		for n in range(1,res+1):
			surface_finale += (n,)
		self.surfaces += (surface_finale,)





