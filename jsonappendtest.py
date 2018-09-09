import json
cheeseits = []
cheetos = {'Station': {'Pattycake': 'yes', 'Bakersman' : 'no'}}
crabs = []
testfile = ('c:\\Python27\\test.json')
    
def doughnut ():
    global cheeseits
    global testfile
    with open(testfile, 'r') as f:
        cheeseits = json.load(f)
    f.close()
    
def holes ():
    global cheeseits
    global testfile
    with open(testfile, 'w+') as f:
        crabs = {'taco' : 'salad'}
        hotdogs = cheeseits['Station']
        hotdogs.update(crabs)
        json.dump(cheeseits, f)
    f.close()
    
doughnut()
holes()
        
    
