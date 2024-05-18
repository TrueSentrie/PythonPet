from pygame import Surface
from PyPet import PyPet
import pygame

pygame.init()

#Window setup
windowSize=[800,500]
screen=pygame.display.set_mode(windowSize)
pygame.display.set_caption("Pet Game")

#Font
font=pygame.font.SysFont("Arial",30)
colorsDict={"white":[255,255,255],
            "black":[0,0,0]}

#Button Images
playImg=pygame.image.load("Buttons/Play.png").convert_alpha()
feedImg=pygame.image.load("Buttons/Feed.png").convert_alpha()
batheImg=pygame.image.load("Buttons/Bathe.png").convert_alpha()
starveImg=pygame.image.load("Buttons/Starve.png").convert_alpha()
dehydrateImg=pygame.image.load("Buttons/Dehydrate.png").convert_alpha()
dirtyImg=pygame.image.load("Buttons/Dirty.png").convert_alpha()
deathImg=pygame.image.load("Buttons/Death.png").convert_alpha()

#Class for the buttons
class Button:
    """
    Initializes a new button at the specified position with the given image.

    Args:
        x (int): The x-coordinate of the button's top-left corner.
        y (int): The y-coordinate of the button's top-left corner.
        image (pygame.Surface): The image displayed for the button.

    Attributes:
        image (pygame.Surface): The image displayed for the button.
        rect (pygame.Rect): The rectangle representing the button's position and size.
        clicked (bool): A flag indicating whether the button has been clicked.
    """
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def buttonHandler(self) -> bool:
        """
        Returns:
             True if the button has been clicked, False otherwise.
        """
        mousePos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked is False:
                self.clicked=True
                return self.clicked
        screen.blit(self.image,(self.rect.x,self.rect.y))
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False

###Renders text on screen
def pygamePrint(text:str, x:int, y:int, textFont:str=font, color:tuple=colorsDict["white"])->Surface:
    """
    Args:
        text(str): The text to be displayed.
        x(int): The x-coordinate of the text's top-left corner.
        y(int): The y-coordinate of the text's top-left corner.
        textFont(pygame.Font,optional): The font used to render the text.
        color(tuple,optional): The RGB color of the text.
    """
    img=textFont.render(text,True,color)
    screen.blit(img,(x,y))
    surf=len(text)*8
    size=(surf,80)
    return Surface(size)

###Creating the buttons
#Food buttons
appleButton=Button(410,10,pygamePrint("apple",410,10).convert_alpha())

#Interact buttons
feedButton=Button(250,10,feedImg)
playButton=Button(250,100,playImg)
batheButton=Button(250,190,batheImg)
starveButton=Button(410,10,starveImg)
dehydrateButton=Button(410,100,dehydrateImg)
dirtyButton=Button(410,190,dirtyImg)
deathButton=Button(410,280,deathImg)

###Create diet dictionaries
herbivoreDict={"salad":10,"artichoke":13,"pineapple":15}
carnivoreDict={"bacon":10,"steak":13,"chicken":15}
omnivoreDict={**herbivoreDict,**carnivoreDict}

###Initialize PyPet
P1=PyPet("Jim",100,diet=omnivoreDict)

###Initialize PyPet stats decrement events
makeHungry=pygame.USEREVENT+1
makeThirsty=pygame.USEREVENT+2
makeDirty=pygame.USEREVENT+3
makeSad=pygame.USEREVENT+4
keepTime=pygame.USEREVENT+5
#                      Event | Time in milliseconds
pygame.time.set_timer(makeHungry,20000)
pygame.time.set_timer(makeThirsty,40000)
pygame.time.set_timer(makeDirty,80000)
pygame.time.set_timer(makeSad,300000)
pygame.time.set_timer(keepTime,1000)

run=True
devMode=False
timeKeeper=0

while run: 

    screen.fill((52,78,91))
    if feedButton.buttonHandler():
        P1.feed("salad")
        P1.feed("water")
        print("Feeding PyPet...")
    if playButton.buttonHandler():
        P1.play("swing")
        print("Playing with PyPet...")
    if batheButton.buttonHandler():
        P1.bathe()
        print("Bathing PyPet...")
    if devMode:
        if starveButton.buttonHandler():
            print("Starving PyPet...")
            P1.hunger=0
        if dehydrateButton.buttonHandler():
            print("Dehydrating PyPet...")
            P1.water=0
        if dirtyButton.buttonHandler():
            print("Dirtying PyPet...")
            P1.cleanliness=0
        if deathButton.buttonHandler():
            print("Killing PyPet...")
            P1.hunger=0
            P1.water=0
            P1.cleanliness=0
            P1.happiness=0

    pygamePrint(f"Name: {P1.name}", 10, 10)
    pygamePrint(f"Age: {P1.age}", 10, 50)
    pygamePrint(f"Hunger: {P1.hunger}", 10, 90)
    pygamePrint(f"Water: {P1.water}", 10, 130)
    pygamePrint(f"Happiness: {P1.happiness}", 10, 170)
    pygamePrint(f"Cleanliness: {P1.cleanliness}", 10, 210)

    #Event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKQUOTE:
                if devMode:
                    devMode=False
                else:
                    devMode=True
        #Decrement PyPet stats
        if event.type==makeHungry:
            P1.hunger-=1
            print("Hunger -1")
        if event.type==makeThirsty:
            P1.water-=1
            print("Thirst -1")
        if event.type==makeDirty:
            P1.cleanliness-=1
            print("Cleanliness -1")
        if event.type==makeSad:
            P1.happiness-=1
            print("Happiness -1")
        if event.type==keepTime:
            timeKeeper+=1
            print(f"{timeKeeper}")
        
    pygame.display.update()

pygame.quit()