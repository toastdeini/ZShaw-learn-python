## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a __init__ that takes self and name params
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a __init__ that takes self and name params
        self.name = name

## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name params
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## To be explained?
        super(Employee, self).__init__(name)
        ## From self get the salary attribute and set it to salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee with salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()