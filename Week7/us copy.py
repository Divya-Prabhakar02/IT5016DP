class BestFrd():
    def __init__(self,name,location,holiday):
        self.name = name
        self.location = location
        self.holiday = holiday
        
    def gettogether(self):
        if self.holiday.lower():
            print(f"I wanna meet {self.name} at the end of the year.As she lives in {self.location} ")
        else:
            print("Can't Meet!!!!!!!!!!!")

frd1 = BestFrd("Bani","India" ,"approved")
frd2 = BestFrd("Nadia","Canada", "approved")
frd2.gettogether()





