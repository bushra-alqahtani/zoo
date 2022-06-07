from animal import Animal


class Cat(Animal):
    def __init__(self,name,age=4, healthLevel=3, happinessLevel=10):
            super().__init__(name,age, healthLevel, happinessLevel)
          
