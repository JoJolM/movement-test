import time
import robot2
import geometry

def main():
	ROB = robot2.Robot(5,15,2)
	geo = geometry.Geometry(ROB)
	print("ROB initialized")
	quit = False
	while quit == False :
		order = input("input order\n")

		if order == "move":
			direction = input("input direction forward (f) or backwards (r)\n")
			ROB.move(direction)
		if order == "roll":
			ROB.showRotation()
			degrees = float(input("input roll angle in °\n"))
			ROB.Roll(degrees)

		if order == "quit":
			quit = True
		if not quit: 
			geo.Update()

		geo.displayCoords()
		
	print(ROB.distance)
	#ROB.showActuator()


main()