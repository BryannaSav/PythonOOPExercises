class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addtax(self, tax):
        self.price *=(1+tax)
        return self
    def refund(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "new in box":
            self.status = "for sale"
        elif reason == "opened box":
            self.price *= .80
            self.status = "used"
        else:
            print "Reason not recognized"
        return self
    def displayInfo(self):
        print "Price: ${}".format(self.price)
        print "Item Name: {}".format(self.name)
        print "Weight: {}lb".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Cost: ${}".format(self.cost)
        print "Status: {}".format(self.status)
        return self


stuff=Product(100,"bauble",1,"generic",80)
