class Animal:
    def __init__(self,name,age, healthLevel, happinessLevel):
        self.name=name
        self.age=age
        self.healthLevel=healthLevel
        self.happinessLevel=happinessLevel

    def display_info(self):
        print(f"name :{self.name} and age : {self.age} and health: {self.healthLevel} and happiness:{self.happinessLevel}")

    def feed(self):
        self.healthLevel += 10
        self.happinessLevel += 10

