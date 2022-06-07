from animal import Animal


class Lion(Animal):
    def __init__(self,name,age=2, healthLevel=3, happinessLevel=3):
            super().__init__(name,age, healthLevel, happinessLevel)
           


