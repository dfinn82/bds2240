#figure out cost of driving, assume 25mph

from breezypythongui import EasyFrame

class WorthIt(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Worth the Trip?",row=0,column=0)
        
        #MPG, city miles
        c = 0
        self.addLabel(text="MPG",row=1,column=c)
        self.mpg = self.addFloatField(value=0.0,row=2,column=c)
        
        #Miles, total round trip
        c = 1
        self.addLabel(text="Miles",row=1,column=c)
        self.miles = self.addFloatField(value=0.0,row=2,column=c)
        
        #Hourly rate, how much you think your time is worth
        c = 2
        self.addLabel(text="Hourly Rate",row=1,column=c)
        self.hourly = self.addFloatField(value=0.0,row=2,column=c)

        #Price of a gallon of gas
        c = 3
        self.addLabel(text="Gas Price",row=1,column=c)
        self.gas = self.addFloatField(value=0.0,row=2,column=c)
        
        self.addLabel(text="Total Cost",row=3,column=0)
        self.totalCost = self.addFloatField(value=0.0,state = "readonly",precision=2,row=4,column=0)
        self.addLabel(text="Minutes at 25MPH",row=3,column=1)
        self.driveTime = self.addFloatField(value=0.0,state = "readonly",precision=2,row=4,column=1)
        self.addButton(text="Calculate",row=5,column=0,command=self.calc)
    
    #figure out how much it will cost to drive X miles
    def calc(self):
        mpg = self.mpg.getNumber()
        miles = self.miles.getNumber()
        hourly = self.hourly.getNumber()
        gas = self.gas.getNumber()
        drivetime = ( miles / 25 ) * 60 
        cost = ( miles / mpg ) * gas + ( drivetime * (hourly / 60))
        self.totalCost.setNumber(cost)
        self.driveTime.setNumber(drivetime)
        

def main():
    WorthIt().mainloop()

if __name__ == '__main__':
    main()
    
