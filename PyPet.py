class PyPet:
    def __init__(self,name:str,age:int,
                 cleanliness:int=100,happiness:int=100,water:int=100,hunger:int=100,
                 diet:dict=None):
        """
        Initializes a pet

        Args:
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
    
    def feed(self,food:str):
        """
        PyPet feeds.

        Args:
            food(str): The food of the pet.
        """

        try:
            if food in self.diet:
                self.hunger+=self.diet[food]
            if self.hunger>100:
                self.hunger=100
            if food=="water":
                self.water+=10
            if self.water>100:
                self.water=100
        except Exception as e:
            print(e)
    def play(self,toy:str):
        """
        PyPet plays.

        Args:
            toy(str): How the pet plays.
        """
        ToyDict={"ball":10,
                 "swing":20,
                 "tug o' war":30,
                 "olympic running":50,
                 "strong man competition":80}

        try:
            if self.water<30 or self.hunger<30:
                raise Exception(f"Error: {self.name} is hungry or thirsty!")
            if toy not in ToyDict:
                raise Exception(f"Error: {self.name} doesn't know how to play {toy}!")
            else:
                self.water-=ToyDict[toy]
                self.hunger-=ToyDict[toy]
                self.cleanliness-=int(ToyDict[toy]*1.5)
                self.happiness+=ToyDict[toy]
            if self.happiness>100:
                self.happiness=100
        except Exception as e:
            return e
    def bathe(self):
        """
        PyPet bathes.
        """
        try:
            self.cleanliness=100
            self.happiness+=10
            if self.happiness>100:
                self.happiness=100
        except Exception as e:
            return e