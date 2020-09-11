import pygame as pg

pg.init()
pg.display.init()
screen = pg.display.set_mode((1000,765))
pg.display.set_caption('Simulation interface')
indicator_state = [pg.image.load('./assets/blank_indicator.png'),pg.image.load('./assets/red_indicator.png')]
Robot = [pg.image.load('./assets/module-central.png')]
verrins = pg.image.load('./assets/verrin.png')
module_teco = pg.image.load('./assets/module_cote.png')
pos_indicator = pg.Surface.get_rect(indicator_state[0])
pos_indicator = pos_indicator.move(10,10)
pos_verrins = [(402,125),(402,165),(522,125),(522,165)]
pos_modules = [(302,110),(622,110)]

pos_MC = pg.Surface.get_rect(Robot[0])
pos_MC = pos_MC.move(412,110)
key = pg.key.get_pressed()

def display(blink,n):
	for i in pos_verrins:
		screen.blit(verrins, i)
	for pos in pos_modules:
		screen.blit(module_teco, pos)  
	screen.blit(Robot[0],pos_MC)
	screen.blit(indicator_state[blink],pos_indicator)
	
	pg.display.flip()


def main():
	blink = 0
	n=0
	
	while True:
		display(blink,n)

		n+=1
		blink += (-1)**n
		for event in pg.event.get():
			if (event.type == pg.QUIT) or (event.type == pg.K_ESCAPE):
				quit()
		pg.time.wait(500)
main()