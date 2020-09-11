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
	def __init__(self,x,y,z,pitch,yaw): #,ox,oy,oz,pitch,yaw
		self.points= ()
		self.edge = () #16 arrètes 
		self.surfaces = ()
		self.x = x/10	
		self.y = y/10 
		self.z = z/10 	
		self.pitch = pitch
		self.yaw = yaw
		
		self.generatePoints(.25,16)

	def generatePoints(self,r,res): #génère les points 
		angle = 2*math.pi / res

		a = (math.cos(self.pitch/2)*math.sin(self.yaw/2) - math.sin(self.pitch/2)*math.sin(self.yaw/2)*(self.x**2+self.y*(self.y+1)+self.z*(self.z+1)))/10
		b = ((math.cos(self.pitch/2)*math.sin(self.yaw/2) + math.sin(self.pitch/2)*math.cos(self.yaw/2))*self.x + math.sin(self.pitch/2)*math.sin(self.yaw/2)*((self.y+1)*(self.z+1)-self.z*self.y))/10
		c = ((math.cos(self.pitch/2)*math.sin(self.yaw/2)*self.y + math.sin(self.pitch/2)*math.cos(self.yaw/2)*(self.y+1)) + math.sin(self.yaw/2)*math.sin(self.pitch/2)*(self.z*self.x - self.x*(self.z+1)))/10
		d = ((math.cos(self.pitch/2)*math.sin(self.yaw/2)*(self.y+1) + math.cos(self.yaw/2)*math.sin(self.pitch/2)*self.z) + math.sin(self.yaw/2)*math.sin(self.pitch/2)*(self.x*self.y - (self.y+1)*self.x))/10
		for n in range(0,res+2):

			if n == 0:
				""" génération du vecteur normal """
				x = self.x + 2*r
				y = self.y
				z = self.z

			else:
				""" génération des vecteurs constituant la base """
				x = self.x
				y = self.y + r*math.cos(n*angle) 
				z = self.z + r*math.sin(n*angle)

			""" Calcul de la nouvelle position avec la rotation prise en compte  avec quaternions """


			x2 = a*(a*x + c*z - d*y) + b*(b*x + c*y + d*z) - c*(a*z + b*y - c*x) + d*(a*y - b*z + d*x)
			y2 = a*(a*y - b*z + d*x) + b*(a*z + b*y - c*x) + c*(b*x + c*y + d*z) - d*(a*x + c*z - d*y)
			z2 = a*(a*z + b*y - c*x) - b*(a*y - b*z + d*z) + c*(a*x + c*z - d*y) + d*(b*x + c*y + d*z)
			print("=========")
			print(x2)
			print(y2)
			print(z2)
			# print(a)
			# print(b)
			# print(c)
			# print(d)
			x+= x2
			y+= y2
			z+= z2

			self.addPoint(y,z,x)





		print("==============================")
		self.genEdge(res)
		self.genSurfaces(res)
		print(self.points)
		#print(self.edge)
		print("==============================")

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





