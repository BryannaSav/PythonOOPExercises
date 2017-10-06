class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Its price is ${}, its max speed is {}mph, and it has ridden {} miles.".format( self.price, self.max_speed, self.miles)
        return self
    def ride(self): 
        print "Riding"
        self.miles+=10
        return self
    def reverse(self): 
        print "Reversing"
        if self.miles >= 5:
            self.miles-=5
        return self
bike1=Bike(25,5)
bike2=Bike(100,25)
bike3=Bike(200,40)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()


