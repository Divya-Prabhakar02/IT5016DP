class BestFrd():
    def __init__(self,name,location):
        self.name = name
        self.location = location
        
    def gettogether(self):
        print(f"I wanna meet {self.name} at the end of the year.As she lives in {self.location} ")

frd1 = BestFrd("Bani","India")
frd2 = BestFrd("Nadia","Canada")
frd2.gettogether()



