from animal import Animal




class Tiger(Animal):
    def __init__(self,name,age=2,color="white", healthLevel=4, happinessLevel=9):
        super().__init__(name,age, healthLevel, happinessLevel)
        self.color=color
      

