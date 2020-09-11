import pygame as pg

pg.init()
pg.display.init()
screen = pg.display.set_mode((1000,765))
pg.display.set_caption('Simulation interface')
indicator_state = [pg.image.load('./assets/blank_indicator.png'),pg.image.load('./assets/red_indicator.png')]
Robot = [pg.image.load('./assets/module-central.png')]
verrins = pg.image.load('./assets/verrin.png')
bras = [pg.image.load('./assets/bras_h.png'),pg.image.load('./assets/bras_b.png')]
module_teco = pg.image.load('./assets/module_cote.png')
pos_indicator = pg.Surface.get_rect(indicator_state[0])
pos_indicator = pos_indicator.move(10,10)
#pos_verrins = [(402,125),(402,165),(522,125),(522,165)]
#pos_modules = [(302,110),(622,110)]
pos_verrins = [pg.Surface.get_rect(verrins),pg.Surface.get_rect(verrins)
			  ,pg.Surface.get_rect(verrins),pg.Surface.get_rect(verrins)]
for i in range(0,4):
	print(i)
	if i ==0:
		pos_verrins[i] = pos_verrins[i].move(-70,0)
	if i ==1:
		pos_verrins[i] = pos_verrins[i].move(-70,-40)
	if i ==2:
		pos_verrins[i] = pos_verrins[i].move(472,125)
	else:
		pos_verrins[i] = pos_verrins[i].move(472,165)


pos_bras = [pg.Surface.get_rect(bras[0]),pg.Surface.get_rect(bras[0]),
			pg.Surface.get_rect(bras[1]),pg.Surface.get_rect(bras[1])]
for i in range(0,4):
	if i==0:
		pos_bras[i] = pos_bras[i].move(0,-140)
	if i==1:
		pos_bras[i] = pos_bras[i].move(-320,-140)
	if i==2:
		pos_bras[i] = pos_bras[i].move(332,200)
	else:
		pos_bras[i] = pos_bras[i].move(652,200)

pos_modules = [pg.Surface.get_rect(module_teco),pg.Surface.get_rect(module_teco)]	
for m in range(0,2):
	if m == 0:
		pos_modules[m] = pos_modules[m].move(302,110)
	else:
		pos_modules[m] = pos_modules[m].move(622,110)

pos_MC = pg.Surface.get_rect(Robot[0])
pos_MC = pos_MC.move(412,110)
key = pg.key.get_pressed()

def display(blink,n):
	for i in pos_verrins:
		screen.blit(verrins, i)
	for m in range(0,4):
		if m<2:
			screen.blit(bras[0],pos_bras[m])
		else:
			screen.blit(bras[1],pos_bras[m])
	for pos in pos_modules:
		screen.blit(module_teco, pos)
	# for j in range(0,2):
	# 	pos_verrins[j].move(-10*((-1)**(n%5)),0)
	# 	pos_modules[0].move(-10*((-1)**(n%5)),0)
	# for k in range(2,4):
	# 	pos_verrins[k].move(10*((-1)**(n%5)),0)
	# 	pos_modules[1].move(10*((-1)**(n%5)),0)  
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