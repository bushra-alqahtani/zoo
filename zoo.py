
from lion import Lion
from tiger import Tiger
from cat import Cat

class Zoo:
    def __init__(self, zoo_name):
        self.animal = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animal.append(Lion(name))

    def add_tiger(self, name):
        self.animal.append(Tiger(name))

    def add_cat(self, name):
        self.animal.append(Cat(name))
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animal:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_cat("uuyh")
zoo1.add_cat("khhnbiuy")
zoo1.print_all_info()
