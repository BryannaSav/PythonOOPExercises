class Patient(object):
    def __init__ (self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.bednumber = None

class Hospital(object):
    def __init__ (self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.availbed=1
    def admit(self, x):
        if self.capacity==0:
            print "The hospital is full, sorry!"
            return self
        else:
            self.patients.append(x)
            x.bednumber=self.availbed
            x.idnum=self.availbed
            self.capacity -= 1
            self.availbed += 1
            print "{} Admitted!".format(self.patients[x.bednumber-1].name)
        return self
    def discharge(self, patname):
        for i in range(0, len(self.patients)):
            if self.patients[i]==patname:
                self.patients[i].bednumber=None
                print "{} has left the hospital!".format(self.patients[i].name)
                self.patients.pop(i)
                self.capacity+=1
            return self
        return self


beth=Patient("Beth", "Cats")
mark=Patient("Mark", ["kiwi","latex"])
health=Hospital("Health",100)
health.admit(beth).admit(mark).admit(beth).discharge(mark)


'''
Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?

Patient:
Attributes:
    Id: an id number
    Name
    Allergies
    Bed number: should be none by default
Hospital
Attributes:
    Patients: an empty array
    Name: hospital name
    Capacity: an integer indicating the maximum number of patients the hospital can hold.
Methods:
    Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full. 
    Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
'''