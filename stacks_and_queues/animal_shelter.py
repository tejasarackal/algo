class Dog:
    name = None

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Cat:
    name = None

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class AnimalShelter:

    def __init__(self):
        self.cats, self.dogs, self.animals = [], [], []

    def enque(self, animal):
        if type(animal) == Cat:
            self.cats.append(animal)
            self.animals.append(animal)
        elif type(animal) == Dog:
            self.dogs.append(animal)
            self.animals.append(animal)
        else:
            print('unknown animal')

    def dequeueAny(self):
        if self.animals:
            animal = self.animals.pop()
            if type(animal) == Cat:
                self.cats.pop()
            elif type(animal) == Dog:
                self.dogs.pop()
            return animal
        return None

    def dequeueDog(self):
        if self.dogs and self.animals:
            animal = self.dogs.pop()
            self.animals.remove(animal)
            return animal
        return None

    def dequeueCat(self):
        if self.cats and self.animals:
            animal = self.cats.pop()
            self.animals.remove(animal)
            return animal
        return None


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enque(Cat('A'))
    shelter.enque(Cat('B'))
    shelter.enque(Dog('C'))
    shelter.enque(Cat('D'))
    print(shelter.dequeueAny())
    print(shelter.dequeueCat())
    print(shelter.dequeueAny())
    print(shelter.dequeueDog())
    print(shelter.dequeueAny())
