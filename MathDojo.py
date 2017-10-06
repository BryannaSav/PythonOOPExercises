class MathDojo(object):
    def __init__(self):
        pass
        self.tot=0
    def add(self, *num):
        self.num=num
        for i in range (0,len(num)):
            if isinstance(num[i], (list,tuple)):
                for j in range(0,len(num[i])):
                    self.tot = self.tot + num[i][j]
            else:
                self.tot = self.tot + num[i]
        return self
    def subtract(self, *num):
        self.num=num
        for i in range (0,len(num)):
            if isinstance(num[i], (list,tuple)):
                for j in range(0,len(num[i])):
                    self.tot = self.tot - num[i][j]
            else:
                self.tot = self.tot - num[i]
        return self
    def result(self):
        print self.tot
        return self

example=MathDojo()
example.add([2,4],6,(2,2)).subtract(2,[4,6]).result()

