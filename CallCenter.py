class Call(object):
    def __init__(self, idnum, name, number, time, reason):
        self.idnum=idnum
        self.name=name
        self.number=number
        self.time=time
        self.reason=reason
    def display(self):
        print self.idnum
        print self.name
        print self.number
        print self.time
        print self.reason

class CallCenter(object):
    def __init__(self):
        self.calls=[]
        self.queuesize=0
    def add(self, call):
        self.calls.append(call)
        self.queuesize  += 1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queuesize -= 1
        return self
    def info(self):
        for i in range (0, len(self.calls)):
            print self.calls[i].name
            print self.calls[i].number
            print self.queuesize
        return self



        
hub=CallCenter()
call1=Call(1, "John","555-5555",1300,"information")
call2=Call(2, "Mary", "222-2222", 1100, "help")
hub.add(call1).add(call2).info().remove()


