class dog:
    species = "animal"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
ricky = dog("ricky", "labrador retriever")
max = dog("max", "shih tzu")
print("ricky is a {}".format(ricky.species))
print("max is also a {}".format(max.species))
print("{} is a {}".format( ricky.name, ricky.breed))
print("{} is a {}".format( max.name, max.breed))