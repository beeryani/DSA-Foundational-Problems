'''
An attempt to understand Object Oriented Programming in Python.
Topics at focus:
Understanding __init__, constructor in Python
Understanding significance of `self`
Trying to implement a Linked List for future use cases 
https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html#:~:text=The%20__init__%20method%20is%20the%20Python%20equivalent%20of,is%20only%20used%20within%20classes.
'''

class Dog:
    def __init__(self,dogBreed = None,dogEyeColor = None) : ### initialised the variables with None to set that to default
        self.breed = dogBreed
        self.eye_color = dogEyeColor

## initialise the object
Doggo = Dog("Chonky Boi","Blue")

## accessing objects that we have declared
print(f"This is my cutie boi, {Doggo.breed}, he has {Doggo.eye_color} eyes")

### second way to initialise
Tiger = Dog()
Tiger.breed = "German Shephard"

###initiated the class with added objects and their values later on.
print(f"{Tiger.breed} is a marshal dog breed!")

### Let's make another class
'''
Important Note:
Always declare an init method before making different methods in the class. VV Imp!
'''

class Beer:
    def __init__(self, beerType = None, beerOrigin = None): ## creating a different method
        self.beerType = beerType
        self.beerOrigin = beerOrigin
    def show(self): ## adding a new method
        print(f"This is the best {self.beerType}, from {self.beerOrigin}")
    

Corona = Beer()

Corona.beerType = "Lager"
Corona.beerOrigin = "Mexico"

print(f"I really like Corona, it is a {Corona.beerType}, from {Corona.beerOrigin}")
## calling the new method
Corona.show()

'''
Types of Variables:
Class Variables: Scope limited to the class being called
Instance Variable : Scope limited to the method within the class i.e. you need to call the method to access these variables
'''

'''
Type of Inheritence within Classes:
1. Single Inheritence
2. Multi-level Inheritence
3. Hierarchial Inheritence
4. Multiple Inheritence
5. Hybrid Inheritence
'''
#******Single Inheritence Example*********

class Animal: ### Parent Class
    def __init__(self, bark):
        self.loudSound = bark
        print(self.loudSound)

class Dog(Animal): #### Child Class
    def __init__(self, nameOfDog = None):
        self.name = nameOfDog

## initializing the instance

Bruno = Dog()
Bruno.name = "Bruno"
Bruno.loudSound = "Bark Bark"

print(f"{Bruno.name} is a good boy, but he creates a {Bruno.loudSound}")

'''
By passing the parent class in the child class, you can access the methods of parent class by initiating the child class
'''

