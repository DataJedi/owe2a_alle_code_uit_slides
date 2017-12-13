################
# Dictionaries #
################

# Voordelen van dictionaries (1-3)
lijst1 = ["koe","geit","mier","slang","mus"]
lijst2 = [4,4,6,0,2]

dieren = ["koe","geit","mier","slang","mus"]
poten = [4,4,6,0,2]

dier_vraag = input("Het aantal poten van een ")
teller = 0

for dier in dieren:
    if dier == dier_vraag:
        print("Een",dier,"heeft",poten[teller],"poten.")
    teller +=1
#################################

# Voordelen van dictionaries (4)
dieren = {"koe":4,
          "geit":4,
          "mier":6,
          "slang":0,
          "mus":2}
dier_vraag = input("Het aantal poten van een ")
print("Een",dier_vraag,"heeft",dieren[dier_vraag],"poten.")

# welke dieren hebben 6 poten?
teller = 0
lijst = list(dieren.values())
for aantal in lijst:
    if aantal == 6:
        print(list(dieren.keys())[teller])
    teller += 1
#################################

# keys() en values()
print(dieren.keys())
print(dieren.values())
#################################

# zoeken en keyerrors
print(dieren["geit"])
#print(dieren["alpaca"]) #uitzetten anders werkt de rest vd code niet
#################################

# Opdracht 1

animal_dict = {"zoogdieren":['dolfijn','alpaca','koe'],
               "insecten":['mier','bladluis','bij'],
               "gevederden":['papegaai','mus','uil']}               

print(animal_dict.keys())
print(animal_dict.values())
print(animal_dict["zoogdieren"])

teller = 0
lijst = list(animal_dict.values())
for dieren in lijst:
    if "papegaai" in dieren:
        print("Een papegaai behoort tot de",list(animal_dict.keys())[teller])
    teller += 1
#################################

# Opdracht 2
animal_dict["vissen"]=['zebravis','gup','clownsvis']
print(animal_dict)
del animal_dict["gevederden"]
print(animal_dict)
#################################

# Dolfijn is nu een vis
animal_dict = {"zoogdieren":['dolfijn','alpaca','koe'],
               "insecten":['mier','bladluis','bij'],
               "gevederden":['papegaai','mus','uil'],
               "vissen":['zebravis','gup','clownsvis']}

# verwijder dolfijn uit zoogdieren
print(type(animal_dict["zoogdieren"]))
animal_dict['zoogdieren'].remove('dolfijn')

# voeg dolfijn toe aan vissen
animal_dict['vissen'].append('dolfijn')

print(animal_dict)
#################################


########
# Sets #
########

# Unieke waardes
boerderij = set(["lama","koe","kip","varken","lama"])
dierentuin = set(["lama","giraffe","leeuw","flamingo","olifant"])
print(boerderij)
print(dierentuin)
#################################

# Opdracht 3
planeten = set()
planeten.add("Mercurius")
planeten.add("Venus")
planeten.add("Aarde")
planeten.add("Mars")
planeten.add("Jupiter")
planeten.add("Saturnus")
planeten.add("Uranus")
planeten.add("Neptunus")
planeten.add("Pluto")
print(planeten)
#################################

# Union
beesteboel = boerderij.union(dierentuin)
print(beesteboel)

# Intersection
beesteboel = boerderij.intersection(dierentuin)
print(beesteboel)

# Difference
beesteboel = boerderij.difference(dierentuin)
print(beesteboel)

#Symmetric difference
beesteboel = boerderij.symmetric_difference(dierentuin)
print(beesteboel)
#################################

# Opdracht 4
hemellichamen = set(["Aarde","Zon","Pluto"])
print(planeten.symmetric_difference(hemellichamen))
print(planeten.intersection(hemellichamen))
zonnestelsel = planeten.union(hemellichamen)
print(zonnestelsel)
#################################

# Issubset / issuperset
vee = set(["koe","kip","varken"])

print(vee.issubset(boerderij))
print(vee.issubset(dierentuin))
print(boerderij.issuperset(vee))

# Remove
boerderij.remove("koe")
print(boerderij)
#################################

# Opdracht 5
print(zonnestelsel.issuperset(planeten))
print(zonnestelsel.issuperset(hemellichamen))
planeten.remove("Pluto")
print(planeten)
#################################

# Wat print deze code?
set1 = set([1,2,3,4,5])
set2 = set([4,5,6,7,8])
set2.add(9)
print(set2)
# {4, 5, 6, 7, 8, 9}

print(set1.union(set2))
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1.intersection(set2))
# {4, 5}
print(set1.difference(set2))
# {1, 2, 3}
print(set1.symmetric_difference(set2))
# {1, 2, 3, 6, 7, 8, 9}
print(set1.issubset(set2))
# False
print(set1.issuperset(set2))
# False
set2.remove(9)
print(set2)
# {4, 5, 6, 7, 8}
#################################


################
# Serializatie #
################

# Pickle
import pickle

def bepaalBi():
    meer = 'j'
    try:
        with open("studenten.dat", 'rb') as input_file:
            bi1 = pickle.load(input_file)
    except IOError:
        bi1 = set()

    while meer.lower() == 'j':
        print ("Studenten in Bi1: ",bi1)
        student = input('Student: ')
        bi1.add (student)
        meer = input ("Doorgaan (j/n)")

    with open("studenten.dat", 'wb') as output_file:
        pickle.dump(bi1, output_file)


def main():
    bepaalBi()

#main()
#################################

# Opdracht 6
planeten = set()
planeten.add("Mercurius")
planeten.add("Venus")
planeten.add("Aarde")
planeten.add("Mars")
planeten.add("Jupiter")
planeten.add("Saturnus")
planeten.add("Uranus")
planeten.add("Neptunus")
planeten.add("Pluto")

hemellichamen = set(["Aarde","Zon","Pluto"])

import pickle

zonnestelsel = planeten.union(hemellichamen)

with open("zonnestelsel.dat", 'wb') as output_file:
    pickle.dump(zonnestelsel, output_file)

with open("zonnestelsel.dat", 'rb') as input_file:
    ons_zonnestelsel = pickle.load(input_file)
    
print(ons_zonnestelsel)




