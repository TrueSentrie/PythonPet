from PythonPet import PythonPet
import pygame
from tkinter import filedialog
from os import getcwd

pygame.init()

windowSize=[800,500]
screen=pygame.display.set_mode(windowSize)
pygame.display.set_caption("PythonPet")

font=pygame.font.SysFont("Arial",30)
colorsDict={"white":[255,255,255],
            "black":[0,0,0]}

playImg=pygame.image.load("Buttons/Play.png").convert_alpha()
feedImg=pygame.image.load("Buttons/Feed.png").convert_alpha()
batheImg=pygame.image.load("Buttons/Bathe.png").convert_alpha()
starveImg=pygame.image.load("Buttons/Starve.png").convert_alpha()
dehydrateImg=pygame.image.load("Buttons/Dehydrate.png").convert_alpha()
dirtyImg=pygame.image.load("Buttons/Dirty.png").convert_alpha()
deathImg=pygame.image.load("Buttons/Death.png").convert_alpha()

class Button:
    def __init__(self,x,y,image):
        """
            Initializes a new button at the specified position with the given image.

            Args:
                x (int): The x-coordinate of the button's top-left corner.
                y (int): The y-coordinate of the button's top-left corner.
                image (pygame.Surface): The image displayed for the button.
            """

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

def pygamePrint(text:str, x:int, y:int, textFont:str=font, color:tuple=colorsDict["white"]):
    """
    Params:
        text(str): The text to be displayed.
        x(int): The x-coordinate of the text's top-left corner.
        y(int): The y-coordinate of the text's top-left corner.
        textFont(pygame.Font,optional): The font used to render the text.
        color(tuple,optional): The RGB color of the text.
    """
    img=textFont.render(text,True,color)
    screen.blit(img,(x,y))

feedButton=Button(250,10,feedImg)
playButton=Button(250,100,playImg)
batheButton=Button(250,190,batheImg)
starveButton=Button(410,10,starveImg)
dehydrateButton=Button(410,100,dehydrateImg)
dirtyButton=Button(410,190,dirtyImg)
deathButton=Button(410,280,deathImg)

herbivoreDict={"salad":10,"artichoke":13,"pineapple":15}
carnivoreDict={"bacon":10,"steak":13,"chicken":15}
omnivoreDict={**herbivoreDict,**carnivoreDict}

toys={"ball":10,"swing":20,"tug o' war":30,"olympic running":50,"strong man competition":80}

P1=PythonPet("Jim",
             10,
             diet=omnivoreDict,
             toyBox=toys)

makeHungry=pygame.USEREVENT+1
hungryTime=30000
makeThirsty=pygame.USEREVENT+2
thirstyTime=15000
makeDirty=pygame.USEREVENT+3
dirtyTime=40000
makeSad=pygame.USEREVENT+4
sadTime=60000
keepTime=pygame.USEREVENT+5

pygame.time.set_timer(makeHungry,hungryTime)
pygame.time.set_timer(makeThirsty,thirstyTime)
pygame.time.set_timer(makeDirty,dirtyTime)
pygame.time.set_timer(makeSad,sadTime)
pygame.time.set_timer(keepTime,1000)

run=True
debugMode=False
timeKeeper=0

while run: 

    screen.fill((52,78,91))

    if feedButton.buttonHandler():
        P1.feed("salad")
        P1.feed("water")
    if playButton.buttonHandler():
        P1.play("swing")
    if batheButton.buttonHandler():
        P1.bathe()

    if debugMode:
        if starveButton.buttonHandler():
            P1.hunger=0
        if dehydrateButton.buttonHandler():
            P1.water=0
        if dirtyButton.buttonHandler():
            P1.cleanliness=0
        if deathButton.buttonHandler():
            P1.isDead(True)

    while not debugMode and P1.isDead():
        pygame.display.update()
        pygamePrint(f"{P1.name} died.",10,360)
        pygamePrint("Press 'R' to restart.",10,420)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_r and P1.isDead():
                    P1.hunger = 100
                    P1.water = 100
                    P1.happiness = 100
                    P1.cleanliness = 100

    P1.zeroStats()

    pygamePrint(f"Name: {P1.name}", 10, 10)
    pygamePrint(f"Age: {P1.age}", 10, 50)
    pygamePrint(f"Hunger: {P1.hunger}", 10, 90)
    pygamePrint(f"Water: {P1.water}", 10, 130)
    pygamePrint(f"Happiness: {P1.happiness}", 10, 170)
    pygamePrint(f"Cleanliness: {P1.cleanliness}", 10, 210)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKQUOTE:
                if debugMode:
                    debugMode=False
                else:
                    debugMode=True
            if event.key==pygame.K_s:
                P1.savePet()
            if event.key==pygame.K_l:
                try:
                    P1.loadPet(filedialog.askopenfilename(initialdir=f"{getcwd()}\\Pets",
                                                          filetypes=(("JSON Files","*.json"),("All Files","*.*"))))
                except Exception as e:
                    print(e)

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
            P1.happyModAdjuster()
            P1.happiness-=P1.happyMod
            print(f"Happiness -{P1.happyMod}")
        if event.type==keepTime:
            timeKeeper+=1
            print(f"{timeKeeper}")
        
    pygame.display.update()

pygame.quit()