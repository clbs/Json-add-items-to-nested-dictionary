import json
cheeseits = []
cheetos = {'Station': {'Pattycake': 'yes', 'Bakersman' : 'no'}}
crabs = []
testfile = ('c:\\Python27\\test.json')
# comment out after first run
#with open(testfile, 'w+') as f:
#    json.dump(cheetos, f)
    
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
        print(crabs)
        print(cheeseits)
        hotdogs = cheeseits['Station']
        hotdogs.update(crabs)
        json.dump(cheeseits, f)
        print(hotdogs)
        print("!")
    f.close()
    
doughnut()

holes()
        
    
