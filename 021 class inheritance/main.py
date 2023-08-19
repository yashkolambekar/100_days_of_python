class Animal():
    def __init__(self):
        self.num_eyes = 2
        print("Animal intiated")
    
    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    # def __init__(self):
    #     super().__init__()

    # def breathe(self):
    #     super().breathe()
    #     print("But we are doing the breathing under water")

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
# nemo.breathe()