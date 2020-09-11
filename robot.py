""" code pour simulation du comportement du Robot """
import math

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
		""" 
			[dmin, dmax] = cm
			[V_Verrins] = cm*s^-1 

		"""
		self.module_avant = Module("AV")
		self.module_arriere = Module("AR")
		self.dmax = dmax
		self.dmin = dmin
		self.V_verrins = V_verrins
		self.verrins = [Verrin(dmax),Verrin(dmax),Verrin(dmax),Verrin(dmax)]
		self.d_verrins = [0,0,0,0]
		self.distance = 0
		self.n = 0


	def sumDist(self):
		print("somme distance\n")
		"""
			sert à retourner la somme des longueurs des verrins 
		"""
		if self.verrins[0].getLength() < self.verrins[1].getLength() :

			if self.verrins[2].getLength() < self.verrins[3].getLength():
				return self.verrins[0].getLength() + self.verrins[2].getLength()
			else:
				return self.verrins[0].getLength() + self.verrins[3].getLength()

		else:
			if self.verrins[2].getLength() < self.verrins[3].getLength():
				return self.verrins[1].getLength() + self.verrins[2].getLength()
			else:
				return self.verrins[1].getLength() + self.verrins[3].getLength()


	def distMeasure(self):
		print("mesure distance")
		self.distance += self.sumDist()

	def ShowDistMeasure(self):
		print(self.distance)

	def getDistMeasure(self):
		return self.distance


	def move(self,direct,distance):
		print("déplacement")
	
		while(distance>self.distance):
			print("cycle déplacement")
			d_rest=distance-self.distance
			print("distance restante = " + str(d_rest))
			if direct == "f":
				self.module_avant.Unblock()
				self.module_avant.showBlockState()
				"""cas ou la distance à parcourir est superieure à 2*dmax et il restera assez de place pour """
				if ( ((d_rest - 2*self.dmax)>=self.dmin) or (d_rest-2*self.dmax==0) ):
					for i in self.verrins:
						i.move(self.dmax)

				else:
					""" cas ou la distance à parcourir est inferieur au double 
						de l'élongation maximale des verrins"""
					if ((d_rest >= self.dmax) and ((d_rest - self.dmax)>=0)):
						for i in range(0,2):
							(self.verrins[i]).move(self.dmax)
						for i in range(2,4):
							(self.verrins[i]).move(d_rest-self.dmax)
					else:
						for i in range(0,2):
							(self.verrins[i]).move(d_rest)

				self.showActuator()
				self.distMeasure()
				self.ShowDistMeasure()
				self.saveActuatorLength()
				self.n +=1

				self.module_avant.Block()
				self.module_avant.showBlockState()
				""" fin de la première élongation, début de la contraction """
				self.module_arriere.Unblock()
				self.module_arriere.showBlockState()
				j=0
				for i in self.verrins:
					i.move(-self.d_verrins[j])
					j+=1
				self.showActuator()
				self.distMeasure()
				self.ShowDistMeasure()
				self.saveActuatorLength()
				self.n +=1

				self.module_arriere.Block()
				self.module_arriere.showBlockState()
				""" fin du cycle """
			
			else: 
				self.module_arriere.Unblock()
				self.module_arriere.showBlockState()
				"""cas ou la distance à parcourir est superieure à 2*dmax et il restera assez de place pour """
				if ( ((d_rest - 2*self.dmax)>=self.dmin) or (d_rest-2*self.dmax==0) ):
					for i in self.verrins:
						i.move(self.dmax)

				else:
					""" cas ou la distance à parcourir est inferieur au double 
						de l'élongation maximale des verrins"""
					if ((d_rest >= self.dmax) and ((d_rest - self.dmax)>=0)):
						for i in range(2,4):
							(self.verrins[i]).move(self.dmax)
						for i in range(0,2):
							(self.verrins[i]).move(d_rest-self.dmax)
					else:
						for i in range(2,4):
							(self.verrins[i]).move(d_rest)

				self.showActuator()
				self.distMeasure()
				self.ShowDistMeasure()
				self.saveActuatorLength()
				self.n +=1

				self.module_arriere.Block()
				self.module_arriere.showBlockState()
				""" fin de la première élongation, début de la contraction """
				self.module_avant.Unblock()
				self.module_avant.showBlockState()
				j=0
				for i in self.verrins:
					i.move(-self.d_verrins[j])
					j+=1
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

	def saveActuatorLength(self):
		print("sauvegarde longueurs")
		j=0
		for i in self.verrins:
			self.d_verrins[j] = i.getLength()
			j+=1