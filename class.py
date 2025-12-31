class Dog:
    def __init__(self, name, breed, nickname):
        self.name = name
        self.breed = breed
        self.nickname = nickname

# Create dog objects - using positional arguments
dog1 = Dog("Buddy", "Golden Retriever", "Bud")
dog2 = Dog("Max", "Beagle", "Maxie")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodle", nickname="Chaz")

print(dog1.name)   # Buddy
print(dog2.breed)  # Beagle
print(dog1.nickname) # Bud
print(dog3.name)   # Charlie



