# Python Pet
___
This is a project that I plan to keep up with, adding more features along the way. The end goal is to have something 
of a pet shop game. The project uses [PyGame](https://www.pygame.org/wiki/Contribute) to produce a GUI over [TKinter](https://tkdocs.com/resources/index.html) as I found it easier to create 
the necessary elements using PyGame such as:
1. Timers for decrementing pet stats
2. Event handling
3. Ways to provide information to the user that I find easier to implement

## Structure of the program
___
The pet gets instantiated through a class with several values:

1. Age*
2. Name*
3. Hunger
4. Thirst
5. Happiness
6. Hygiene
7. Happiness Modifier*
8. Diet*
9. Toy Box*

<sup>*Currently hard coded but plan to make soft coded.</sup>   

### Pet dictionaries
For the `Diet` and `Toy Box` values, a dictionary is required for the input which I have set up in the project like this:
```python3
herbivoreDict={"salad":10,"artichoke":13,"pineapple":15}
carnivoreDict={"bacon":10,"steak":13,"chicken":15}
omnivoreDict={**herbivoreDict,**carnivoreDict}

toys={"ball":10,"swing":20,"tug o' war":30,"olympic running":50,"strong man competition":80}
```
As of right now, the only values from the dictionaries being used are the first for both `omnivoreDict` and `toy`. I 
plan to make the feed button bring you to a new scene where you choose what food to feed and how to play with your pet.

### Happiness decay
The Happiness Modifier is used as an initial value, set to 5 by default, in a method that decrements the pet's happiness 
based on the number of stats below 50. The way this is done is by using an empty list, `stats`, and checking if each stat 
is below 50 and adding `isDirty`, `isBored`, `isDehydrated`, and/or `isHungry` if they are not already in `stats`. For 
every stat in the list, the modifier is increased by 5.

### Feeding and playing with the pet
The `feed` method will take a food name as input and check if it's within the pet's diet dictionary. If it is then 
the key is added to the pets current food and water stat. The play method works essentially the same way. Both methods 
will return an and exception if the items are not found in their respective dictionaries.

### Bathing the pet
The `bathe` method sets the pet's Hygiene to max and adds 10 to happiness.

### Making sure the pet is alive
The `isDead` method checks will return True if hunger and thirst are both 0. It also accepts one boolean argument that 
defaults to `False`. If `True` is passed, the method will set hunger and thirst to 0 and return `True`.

### Stat decrement
In order to get the stats to go down over time, I used the `USEREVENT` method from pygame to make my own timers.
```python3
makeHungry=pygame.USEREVENT+1
hungryTime=30000

pygame.time.set_timer(makeHungry,hungryTime)

if event.type==makeHungry:
    P1.hunger-=1
    print("Hunger -1")
```

### Handling Multiple Pets
A pet will have its own save file named after it with the data stored in a JSON file. I created two methods to save and 
load pet data. Pressing "S" will call the `savePet` method which will take all the values of the class and convert them 
into a JSON string using Python's builtin `json` module. Pressing "L" call the `loadPet` method, opening a file explorer 
window prompting a file to be selected. Once again I use the `json` module to load the values from the file to the pet.
