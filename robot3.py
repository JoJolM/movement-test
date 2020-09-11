""" code pour simulation du comportement du Robot """
import math
import geometry

class Verrin():

	def __init__(self,dmax):
		"""self.dmin = dmin"""
		self.length = 0
		self.dmax = dmax

	def move(self,x):
		print("elongation verrin")
		if self.length + x <= self.dmax and self.length + x >= 0:
			self.length += x
		else:
			if self.length + x <= self.dmax :
				print("lol")

	def getLength(self):
		return self.length

	def showLength(self):
		print(self.length)


class Module():

	def __init__(self,name):
		self.block = True
		self.name = name

	def Unblock(self):
		print("debloquage module")
		if self.block == True :
			self.block = False

	def Block(self):
		print("bloquage")
		if self.block == False:
			self.block = True

	def getBlockState(self):
		return self.block

	def showBlockState(self):
		if self.block == True:
			print("le module "+ self.name + " est bloqué")
		else : 
			print("le module "+ self.name + " n'est pas bloqué")		


class Robot():

	def __init__(self,dmin,dmax,V_verrins):
		
		self.module_avant = Module("AV")
		self.module_arriere = Module("AR")
		""" données à mettre dans un fichier conf si créé"""
		""" 
			[dmin, dmax] = cm
			[V_Verrins] = cm*s^-1 

		"""
		self.dmax = dmax
		self.dmin = dmin
		self.V_verrins = V_verrins
		self.d_vv = 4.5
		""" -------------------------------------------- """
		self.roll = 0
		self.pitch = 0
		self.yaw = 0

		self.verrins = [Verrin(dmax),Verrin(dmax),Verrin(dmax),Verrin(dmax)]
		self.d_verrins = [0,0,0,0]
		self.prevMove = 0
		self.distance = 0
		self.n = 0
		self.direct = ''


	def sumDist(self):
		print("somme distance\n")
		"""
			sert à retourner la somme des longueurs des verrins 
		"""
		if self.d_verrins[0] < self.d_verrins[1] :
			print("somme dist angle -")
			

			if self.d_verrins[2] < self.d_verrins[3]:
				return ((self.verrins[0].getLength()-self.d_verrins[0]) + (self.verrins[2].getLength()-self.d_verrins[2]))
			else:
				return ((self.verrins[0].getLength()-self.d_verrins[0]) + (self.verrins[3].getLength()-self.d_verrins[3]))

		else:
			print("somme dist angle +")
			if self.d_verrins[2] < self.d_verrins[3]:
				print(((self.verrins[1].getLength()-self.d_verrins[1]) + (self.verrins[2].getLength()-self.d_verrins[2])))
				return ((self.verrins[1].getLength()-self.d_verrins[1]) + (self.verrins[2].getLength()-self.d_verrins[2]))
			else:
				print(((self.verrins[1].getLength()-self.d_verrins[1]) + (self.verrins[3].getLength()-self.d_verrins[3])))
				return ((self.verrins[1].getLength()-self.d_verrins[1]) + (self.verrins[3].getLength()-self.d_verrins[3]))

	def angleMeasurements(self):
		""" pour voir indexation des verrins consulté le schéma explicatif
			
			angles = [angle créé par les verrins 1 et 2, angle créé par les verrins 3 et 4]
			[angles[0],angles[1]] = rad
			sens positif = sens trigonométrique

		"""
		self.angles = [0,0]
		if self.verrins[0].getLength() != self.verrins[1].getLength() :
			self.angles[0] = math.atan((self.verrins[1].getLength()-self.verrins[0].getLength())/self.d_vv)
		if self.verrins[2].getLength() != self.verrins[3].getLength() :
			self.angles[1] = math.atan((self.verrins[2].getLength()-self.verrins[3].getLength())/self.d_vv)

	def measureRotation(self):
		print("measureRotation")
		if self.roll == 0:
			if self.direct == "f":
				self.yaw += (self.angles[0])
			else:
				self.yaw += (self.angles[1])

		else:
			if self.direct == "f":
				print(self.angles[0])
				print(math.tan(self.angles[0]))
				self.pitch += (math.atan(math.tan(self.angles[0])*math.sin(self.roll)))
				self.yaw   += (math.atan(math.tan(self.angles[0])*math.cos(self.roll)))
			else:
				self.pitch += (math.atan(math.tan(self.angles[1])*math.sin(self.roll)))
				self.yaw   += (math.atan(math.tan(self.angles[1])*math.cos(self.roll)))

	def distMeasure(self):
		print("mesure distance")
		self.distance += self.sumDist()

	def ShowDistMeasure(self):
		print("distance  = "+str(self.distance))

	def getDistMeasure(self):
		return self.distance


	def move(self,direct):
		print("déplacement")
		self.direct = direct
		self.prevMove = 0
	
		#d_rest=distance-self.distance
		#print("distance restante = " + str(d_rest))
		if self.direct == "f":
			print("begin cycle")
			self.module_avant.Unblock()
			self.module_avant.showBlockState()
			k=1
			for i in self.verrins :
				d = float(input("enter distance for actuator number "+str(k)+"\n"))
				i.move(d)
				k+=1

			self.angleMeasurements()

			if self.verrins[1]!=self.verrins[0]:
				self.measureRotation()

			self.showAngles()
			self.showRotation()
			self.showActuator()
			#self.distMeasure()
			#self.saveActuatorLength()
			self.ShowDistMeasure()
			self.module_avant.Block()
			self.module_avant.showBlockState()
			self.n+=1
			""" fin de la première élongation, début de la contraction """
			self.module_arriere.Unblock()
			self.module_arriere.showBlockState()

			if input("auto-return ? Yes(y) No(n)\n")=="n":
				j=1
				for i in self.verrins:
					dr = float(input("enter return distance for actuator number "+str(j)+"\n"))
					i.move(-dr)
					self.d_verrins[j-1]  = dr 
					j+=1
			else:
				j=0
				for i in self.verrins:
					i.move(-self.d_verrins[j])
					j+=1

			#self.angleMeasurements()
			self.showAngles()
			self.showRotation()
			self.updatePrevMove()
			self.showPrevMove()
			self.showActuator()
			self.distMeasure()
			self.ShowDistMeasure()
			#self.saveActuatorLength()
			self.module_arriere.Block()
			self.module_arriere.showBlockState()
			self.n +=1
			""" fin du cycle """
		
		else: 
			self.module_arriere.Unblock()
			self.module_arriere.showBlockState()
			"""cas ou la distance à parcourir est superieure à 2*dmax et il restera assez de place pour """
			self.n +=1
			for m in range(2,4):
				d=int(input("enter distance for actuator number "+str(m)+"\n"))
				self.verrins[m].move(d)
			for m in range(0,2):
				d=int(input("enter distance for actuator number "+str(m)+"\n"))
				self.verrins[m].move(d)

			self.angleMeasurements()

			if self.verrins[3]!=self.verrins[2]:
				self.measureRotation()

			self.showAngles()
			self.showRotation()
			self.showActuator()
			self.updatePrevMove()
			self.saveActuatorLength()
			self.distMeasure()
			self.showPrevMove()
			self.ShowDistMeasure()
			self.module_arriere.Block()
			self.module_arriere.showBlockState()
			self.n += 1
			""" fin de la première élongation, début de la contraction """
			self.module_avant.Unblock()
			self.module_avant.showBlockState()
			if input("auto-return ? Yes(y) No(n)\n")=="n":
				for m in range(2,4):
					d=int(input("enter return distance for actuator number "+str(m)+"\n"))
					self.verrins[m].move(-d)
				for m in range(0,2):
					d=int(input("enter return distance for actuator number "+str(m)+"\n"))
					self.verrins[m].move(-d)
			else:
				j=0
				for i in self.verrins:
					i.move(-self.d_verrins[j])
					j+=1
			#self.angleMeasurements()
			self.showAngles()
			self.showRotation()
			self.showActuator()
			self.distMeasure()
			self.ShowDistMeasure()
			self.saveActuatorLength()
			self.n +=1

			self.module_avant.Block()
			self.module_avant.showBlockState()
			""" fin du cycle """
	def showActuator(self):
		print("affichage longueurs verrins")
		for i in self.verrins:
			i.showLength()
	def showAngles(self):
		j=1
		for i in self.angles:

			print("angle #"+str(j)+" : "+str(round(math.degrees(i)))+"°")
			j+=1

	def showRotation(self):
		print("yaw   : "+str(round(math.degrees(self.yaw)))+"°")
		print("pitch : "+str(round(math.degrees(self.pitch)))+"°")
		print("roll  : "+str(round(math.degrees(self.roll)))+"°")
		
	def getRotation(self):
		return(self.roll,self.pitch,self.yaw)

	def updatePrevMove(self):
		if self.direct == "f":
			print("fuu")
			self.prevMove= self.sumDist()
		else:
			self.prevMove= self.sumDist()

	def showPrevMove(self):
		print("prev move =" + str(self.prevMove))

	def saveActuatorLength(self):
		print("sauvegarde longueurs")
		j=0
		for i in self.verrins:
			self.d_verrins[j] = i.getLength()
			j+=1

	def Roll(self,degrees):
		print("roll")
		self.roll += math.radians(degrees)
		self.showRotation()