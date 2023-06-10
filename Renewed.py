import math
from random import randrange
from random import randint

#The Venue Class
class Venue:
    count_venues=[]
    def __init__(self, name, capacity):
        self.name = str(name)
        self.capacity = int(capacity)
        Venue.count_venues.append(self)
        
    def __del__(self):
        Venue.count_venues.remove(self)
    
    @staticmethod
    def bit():
        a = len(Venue.count_venues)
        global bitstring_venue, bitstring_venue2 
        bitstring_venue = ""
        bitstring_venue2 = ""
        for i in range (math.ceil(math.log(a, 2))):
            bitstring_venue += str(randrange(0,2))
            bitstring_venue2 += str(randrange(0,2))
        #print(bitstring_venue, bitstring_venue2)
        return bitstring_venue, bitstring_venue2

#Available venues in faculty of engineering
elf = Venue("ELF", 500)
tetfund = Venue("TETfund", 250)
necb1 = Venue("NECB 1", 200)
necb2 = Venue("NECB 2", 200)
necb3 = Venue("NECB 3", 200)
gd1 = Venue("GD 1", 100)
gd2 = Venue("GD 2", 100)
gd3 = Venue("GD 3", 100)
gd4 = Venue("GD 4", 100)     
neb1 = Venue("New Engineering Block 1", 200)
neb2 = Venue("New Engineering Block 2", 200)
neb3 = Venue("New Engineering Block 3", 200)
neb4 = Venue("New Engineering Block 4", 200)
neb5 = Venue("New Engineering Block 5", 200)     
fl3 = Venue("FL 3", 100)
fl4 = Venue("FL 4", 100)
ptdfhall = Venue("PTDFhall", 250)
ptdf1 = Venue("PTDF 1", 100)
ptdf2 = Venue("PTDF 2", 100)



class subjects:
    count = []

    def __init__(self, name, number_of_stude nts, hours):
        self.name = name
        self.number_of_students = int(number_of_students)
        self.hours = int(hours)
        subjects.count.append(self)
    
    def __del__(self):
        subjects.count.remove(self)

    @staticmethod
    def bit():
        a = len(subjects.count)
        global bitstring, bitstring2
        bitstring= ''
        bitstring2 = ''
        for i in range (math.ceil(math.log(a, 2))):
            bitstring += str(randrange(0,2))
            bitstring2 += str(randrange(0,2))
        return bitstring, bitstring2


### To randomly fill the subjects offered
### Approx 10 courses per dept level, for 5 levels, in 8 depts totalling 400 courses    
subjects_dict = {}

for i in range(40):
    subjects_dict['maths' + str(i)] = subjects('maths', 200, 4)
    subjects_dict['chem' + str(i)] = subjects('chemistry', 150, 3)
    subjects_dict['phy' + str(i)] = subjects('physics', 150, 3)
    subjects_dict['cpe' + str(i)] = subjects('Computer', 120, 2)
    subjects_dict['geo' + str(i)] = subjects('Geography', 140, 2)
    subjects_dict['sta' + str(i)] = subjects('Statistics', 100, 2)
    subjects_dict['his' + str(i)] = subjects('History', 200, 2)
    subjects_dict['dat' + str(i)] = subjects('data pro', 100, 2)
    subjects_dict['ele' + str(i)] = subjects('Electrical Electronics', 200, 1)
    subjects_dict['gst' + str(i)] = subjects('General Studies 1', 300, 2)



# Accessing the created objects
global bitstring, bitstring2
subjects_dict