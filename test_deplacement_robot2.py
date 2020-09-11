import time
import display3dMap as d3m
import robot3
import geometry
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame as pg
rep_points = ((0,0,0),(1,0,0),(0,1,0),(0,0,1))
rep_edge = ((0,1),(0,2),(0,3))
colors = [
		(1,1,1),
		(0,1,1),
		(0,0,1),
		(1,1,1),
		(0,1,1),
		(0,0,1),
		(1,1,1),
		(0,1,1),
		(0,0,1),
		(1,1,1),
		(0,1,1),
		(0,0,1),
		(1,1,1),
		(0,1,1),
		(0,0,1),
		(1,1,1)
		
	]

def displayCube(Cube,geo,cone_pos):
	n =1 
	m=0
	""" Affichage du cube """
	glBegin(GL_QUADS)
	for edge in Cube.edges:
		glColor3fv((0,1,0))
	glEnd()
	glLineWidth(1)
	""" affichage du repère """
	glBegin(GL_LINES)
	for edge in Cube.edges:
		for point in edge:
			glVertex3fv(Cube.points[point])
	""" le sens positif des axes est représenté en :
			
			- magenta pour x 
			- jaune pour y 
			- cyan pour z

	"""
	for edge in rep_edge:
		if n == 1:
			glColor3fv((1,1,0))
		if n == 2:
			glColor3fv((0,1,1))
		if n == 3:
			glColor3fv((1,0,1))
		for point in edge:
				glVertex3fv(rep_points[point])
		n+=1
	glEnd()

	glLineWidth(3)
	""" affichage de la trajectoire """
	glBegin(GL_LINES)
	glColor3fv((1,0,0))
	if len(geo.edge)>0:
		if len(geo.edge) == 1:
			for edge in geo.edge:
				for point in edge:
					glVertex3fv(geo.points[point])
					m+=1
		else:
			for edge in geo.edge:
				for point in edge:
					glVertex3fv(geo.points[point])
	glEnd()

	glBegin(GL_QUADS)
	
	for surface in cone_pos.surfaces:
		x=0
		for point in surface:
			glColor3fv(colors[x])
			x+=1
			glVertex3fv(cone_pos.points[point])
	glEnd()

def main():
	print("init")
	pg.init()
	pg.display.init()
	cube_ref = d3m.Cube()
	cone_pos = d3m.Cone()
	screen = (800,600)
	pg.display.set_mode(screen, pg.DOUBLEBUF|pg.OPENGL)
	gluPerspective(90, (screen[0]/screen[1]), 0.1, 500.0)
	glTranslatef(0.0,0.0,-5)
	glRotatef(0, 0, 0, 0)
	ROB = robot3.Robot(5,15,2)
	geo = geometry.Geometry(ROB)
	print("ROB initialized")
	order = ''
	quit = False
	while quit == False :

		for event in pg.event.get() :
			if event.type == pg.QUIT:
				pg.quit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					order = input("input order\n")
					break
				# --- Rotations ---
				if event.key == pg.K_LEFT:
					glRotatef(2, 0,-10,0)
				if event.key == pg.K_RIGHT:
					glRotatef(2, 0,10,0)
				if event.key == pg.K_UP:
					glRotatef(2, 10,0,0)
				if event.key == pg.K_DOWN:
					glRotatef(2, -10,0,0)
				if event.key == pg.K_q:
					glRotatef(2, 0,0,10)
				if event.key == pg.K_e:
					glRotatef(2, 0,0,-10)

				#--- Translations ---
				if event.key == pg.K_w:
					glTranslatef(0.0,1.0,0.0)	
				if event.key == pg.K_s:
					glTranslatef(0.0,-1.0,0.0)
				if event.key == pg.K_a:
					glTranslatef(1.0,0.0,0.0)
				if event.key == pg.K_d:
					glTranslatef(-1.0,0.0,0.0)

				#--- Zoom ---
				if event.key == pg.K_KP9:
					glTranslatef(0.0,0.0,1.0)
				if event.key == pg.K_KP3:
					glTranslatef(0.0,0.0,-1.0)

				if event.key == pg.K_ESCAPE:
					pg.quit()

		if order == "move":
			direction = input("input direction forward (f) or backwards (r)\n")
			ROB.move(direction)
			geo.Update()
			print(geo.edge)
			print(geo.points)
			print(ROB.angles)
			order = ''

		if order == "roll":
			ROB.showRotation()
			degrees = float(input("input roll angle in °\n"))
			ROB.Roll(degrees)
			order = ''

		if order == "coordinates":
			geo.displayCoords()
			order = ''

		if order == "quit":
			pg.quit()
			quit = True
		# if not quit: 
		# 	geo.Update()
		
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		displayCube(cube_ref,geo,cone_pos)
		pg.display.flip()
		pg.time.wait(10)
	
	#print(ROB.distance)
	#ROB.showActuator()


main()