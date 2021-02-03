import pygame
import random
import time

pygame.init()
x=True
disp=1
q=1
r=1
flag=1
h=670
w=1290
screen=pygame.display.set_mode((w, h))
clock=pygame.time.Clock()

pygame.display.set_caption('Rummy')
font=pygame.font.SysFont(None, 16)
f=pygame.font.SysFont(None, 32)

bg=pygame.image.load(r"C:\\Users\\Neha\\Desktop\\back.jpg")

def deck1():
	y=[2,3,4,5,6,7,8,9,'T','J','Q','K','A']
	y=list(map(str,y))
	x=[ r +'_'+ s for r in y for s in ['clubs', 'diamonds', 'hearts', 'spades'] ]
	x+=['C','C']
	random.shuffle(x)
	return x

def draw13(list):
	return list[:13]

def drawai13(list):
	return list[13:26]

"""def discard(list):
	return list[26]"""

def stock(list):
	return list[27:]

def createimg(card):
	image = {}
	for c in card:
		image[c]=pygame.image.load(r"C:\\Users\\Neha\\Desktop\\playing_cards"+'\\'+c+".png")
      	
	return image

def addcard(d13, baap):
	d13.append(baap[0])
	"""temp=baap[27]
	for i in range(27,len(stock(baap))-1):
		baap[i]=baap[i+1]
	baap[-1]=temp"""

def addfromdisc(d13,baap):
	d13.append(baap[0])
	
pygame.display.flip()

cardsall=deck1()
cardsall*=2
card_list=draw13(cardsall)
disc=[cardsall[26]]
stock=cardsall[27:]
ai=drawai13(cardsall)
stockimg=pygame.image.load(r"C:\\Users\\Neha\\Desktop\\playing_cards"+'\\'+"stock"+".jpg")
stockhover=pygame.image.load(r"C:\\Users\\Neha\\Desktop\\playing_cards"+'\\'+"stockhover"+".jpg")

while x:
	
	
	if len(disc)>0:
		discimg=pygame.image.load(r"C:\\Users\\Neha\\Desktop\\playing_cards"+'\\'+disc[0]+".png")
	imgdict=createimg(card_list)
	mouse=pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	screen.blit(bg, (0, 0))
	a,b=10,10
	X,Y=550,170

	j=1
	for i in imgdict:
		screen.blit(imgdict[i], (a, b))
		text = font.render(str(j), True, (0,0,0))
		screen.blit(text,(a+40,b+110))
		if j<=13:
			screen.blit(stockimg,(a,(550-96)))
		a+=90
		j+=1
	
	if q==(-1):
		pygame.draw.rect(screen, (0,0,0),(600,580,150,45))
		t=f.render("CLICK HERE", True, (255,255,255))
		screen.blit(t,(608,590))
		text=f.render("Click the button to have computer's turn", True, (0,0,0))
		screen.blit(text,(10,590))
		if 600<mouse[0]<800 and 590<mouse[1]<635:
			pygame.draw.rect(screen, (0,0,0),(597,577,156,51))
			t=f.render("CLICK HERE", True, (255,255,255))
			screen.blit(t,(608,590))
			if click[0]==1:
				#text=f.render("computer's turn", True, (0,0,0))
				#screen.blit(text,(10,590))
		
		#time.sleep(5)
			
				x=random.randrange(0,13,1)
				if r==1:
					temp=ai[x]
					ai[x]=disc[0]
					disc[0]=temp
					r*=(-1)
				else:
					#temp=ai[x]
					disc.insert(0,ai[x])
					ai[x]=stock[0]
					stock=stock[1:]
					r*=(-1)
				q*=(-1)

	if disp==1 and not(flag==(-1)):
		if (550<mouse[0]<621) and (Y<mouse[1]<Y+96):
			pygame.draw.rect(screen,(0,0,0),(547,Y-3,77,102))
			pygame.draw.rect(screen,(255,255,255),(548,Y-2,75,100))
			if click[0]==1 and flag==1:
				addfromdisc(card_list, disc)
				disc.remove(disc[0])
				disp*=(-1)
	if len(disc)>0:
		screen.blit(discimg,(X,Y))

	if flag==1 and not(disp==(-1)):
		if (640<mouse[0]<711) and (Y<mouse[1]<Y+96):
			screen.blit(stockhover,(X+88,Y-2))
			if click[0]==1:
				addcard(card_list, stock)
				stock.remove(stock[0])
				flag*=(-1)
	
	screen.blit(stockimg,(X+90,Y))	

	if not(flag==-1 or disp==-1 or (q==-1)):
		text=f.render("Click a card from discard or stock pile to add it to your deck", True, (0,0,0))
		screen.blit(text,(10,590))

	if flag==-1 or disp==-1:
		if q==1:
			#time.sleep(5)
			text=f.render("Click the card from your deck to be discarded", True, (0,0,0))
			screen.blit(text,(10,590))
			
			if (10<mouse[0]<81) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[0]
					disc.insert(0,card_list[0])
					card_list=card_list[1:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)
					

		
			elif (100<mouse[0]<171) and (10<mouse[1]<106):
				if click[0]==1:
					disc.insert(0,card_list[1])
					card_list=card_list[0:1]+card_list[2:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (190<mouse[0]<261) and (10<mouse[1]<106):
				if click[0]==1:
					disc.insert(0,card_list[2])
					#cardsall[26]=card_list[2]
					card_list=card_list[0:2]+card_list[3:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (280<mouse[0]<351) and (10<mouse[1]<106):
				if click[0]==1:
					disc.insert(0,card_list[3])
					#cardsall[26]=card_list[3]
					card_list=card_list[0:3]+card_list[4:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (370<mouse[0]<441) and (10<mouse[1]<106):
				if click[0]==1:
					disc.insert(0,card_list[4])
					#cardsall[26]=card_list[4]
					card_list=card_list[0:4]+card_list[5:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (460<mouse[0]<531) and (10<mouse[1]<106):
				if click[0]==1:
					disc.insert(0,card_list[5])
					#cardsall[26]=card_list[5]
					card_list=card_list[0:5]+card_list[6:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (550<mouse[0]<621) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[6]
					disc.insert(0,card_list[6])
					card_list=card_list[0:6]+card_list[7:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (640<mouse[0]<711) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[7]
					disc.insert(0,card_list[7])
					card_list=card_list[0:7]+card_list[8:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (730<mouse[0]<801) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[8]
					disc.insert(0,card_list[8])
					card_list=card_list[0:8]+card_list[9:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (820<mouse[0]<891) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[9]
					disc.insert(0,card_list[9])
					card_list=card_list[0:9]+card_list[10:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (910<mouse[0]<981) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[10]
					disc.insert(0,card_list[10])
					card_list=card_list[0:10]+card_list[11:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (1000<mouse[0]<1071) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[11]
					disc.insert(0,card_list[11])
					card_list=card_list[0:11]+card_list[12:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (1090<mouse[0]<1161) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[12]
					disc.insert(0,card_list[12])
					card_list=card_list[0:12]+card_list[13:]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

			elif (1180<mouse[0]<1251) and (10<mouse[1]<106):
				if click[0]==1:
					#cardsall[26]=card_list[13]
					disc.insert(0,card_list[13])
					card_list=card_list[0:13]
					if flag==(-1):
						flag*=(-1)
					else:
						disp*=(-1)
					q*=(-1)

	if not((1175<mouse[0]<1175+150) and (580<mouse[1]<580+40)):
		pygame.draw.rect(screen, (0,0,0),(1175,580,140,40))
		text=f.render("DECLARE", True, (255,255,255))
		screen.blit(text,(1177,590))

	else:
		pygame.draw.rect(screen, (20,20,20),(1170,575,150,50))
		text=f.render("DECLARE", True, (255,255,255))
		screen.blit(text,(1177,590))
		if click[0]==1:
			text=f.render("GAME ENDS", True, (0,0,0))
			screen.blit(text,(w//2,h//2))
			#
			x*=0

	if len(stock)==1:
		stock+=disc[::-1]
		#stock=stock[::-1]
		disc=disc[:1]


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			#time.sleep(3)
			x=False



	pygame.display.update()
	clock.tick(10)
