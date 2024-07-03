import json

class PythonPet:
    def __init__(self,name:str,age:int,
                 cleanliness:int=100,happiness:int=100,water:int=100,hunger:int=100,
                 happyMod:int=5,diet:dict=None,toyBox:dict=None):
        """
        Initializes a pet

        Params:
            name(str): The name of the pet.
            age(int): The age of the pet.
            cleanliness(int,optional): The cleanliness of the pet. Defaults to 100.
            happiness(int,optional): The happiness of the pet. Defaults to 100.
            water(int,optional): The water of the pet. Defaults to 100.
            hunger(int,optional): The hunger of the pet. Defaults to 100.
            diet(dict,optional): The diet of the pet. Defaults to "omnivore".
        """

        self.name=name
        self.age=age
        self.cleanliness=cleanliness
        self.happiness=happiness
        self.water=water
        self.hunger=hunger
        self.diet=diet
        self.toyBox=toyBox
        self.happyMod=happyMod
    
    def feed(self,food:str)->None|Exception:
        """
        PythonPet feeds.

        Params:
            food(str): The food of the pet.
        """

        try:
            if food in self.diet:
                self.hunger+=self.diet[food]
            else:
                raise Exception(f"Error: {self.name} doesn't like that food!")
            if self.hunger>100:
                self.hunger=100
            if food=="water":
                self.water+=10
            if self.water>100:
                self.water=100
        except Exception as e:
            return e

    def play(self,toy:str)->None|Exception:
        """
        PythonPet plays.

        Params:
            toy(str): How the pet plays.
        """

        toyDict=self.toyBox
        decrement=int(toyDict[toy]/2)

        try:
            if toy not in toyDict:
                raise Exception(f"Error: {self.name} doesn't know how to play {toy}!")
            if self.hunger-decrement<=0 or self.water-decrement<=0:
                raise Exception(f"Error: {self.name} is hungry or thirsty!")
            else:
                self.water-=decrement
                self.hunger-=decrement
                self.cleanliness-=decrement
                self.happiness+=toyDict[toy]
            if self.happiness>=100:
                self.happiness=100
        except Exception as e:
            return e

    def bathe(self)->None|Exception:
        """
        PythonPet bathes.
        """

        try:
            if self.cleanliness<=60:
                self.cleanliness=100
                self.happiness+=10
                if self.happiness>100:
                    self.happiness=100
            else:
                raise Exception(f"{self.name} doesn't need to bathe yet!")
        except Exception as e:
            return e

    def isDead(self,killSwitch=False)->bool:
        """
        Checks if PythonPet is dead.

        Params:
            killSwitch(bool,optional): If killSwitch is True, PythonPet is killed. Defaults to False.

        Returns:
            True if hunger, water, and happiness are all 0.
        """

        if self.hunger==0 and self.water==0:
            return True
        if killSwitch:
            self.hunger=0
            self.water=0
            self.cleanliness=0
            return True
        else:
            return False

    def zeroStats(self):
        """
        Handling underflow of stats.
        """

        if self.hunger<0:
            self.hunger=0
        if self.water<0:
            self.water=0
        if self.cleanliness<0:
            self.cleanliness=0
        if self.happiness<0:
            self.happiness=0

    def happyModAdjuster(self):
        """
        Adjusts the happiness modifier for each stat at or below 50.
        """

        stats:list=[]
        self.happyMod=5

        #This looks so ugly but it works.
        if self.hunger<50 and "isHungry" not in stats:
            stats.append("isHungry")
        elif "isHungry" in stats:
            stats.remove("isHungry")
        if self.water<50 and "isDehydrated" not in stats:
            stats.append("isDehydrated")
        elif "isDehydrated" in stats:
            stats.remove("isDehydrated")
        if self.happiness<50 and "isBored" not in stats:
            stats.append("isBored")
        elif "isBored" in stats:
            stats.remove("isBored")
        if self.cleanliness<50 and "isDirty" not in stats:
            stats.append("isDirty")
        elif "isDirty" in stats:
            stats.remove("isDirty")

        print(stats)

        for _ in stats:
            self.happyMod+=5

    def savePet(self):
        with open(f"Pets/{self.name}.json","w") as save:
            json.dump(self.__dict__,save,indent=2)

    def loadPet(self,saveFile:str=None):
        with open(f"{saveFile}","r") as load:
            self.__dict__=json.load(load)
