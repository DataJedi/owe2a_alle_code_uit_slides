# Code behorend bij les 5 van course 2a (Python II)

# Voorbeeld Auto 1
class auto:
    def setSnelheid(self, v):
        self.snelheid = v

    def getSnelheid(self):
        return self.snelheid
######################################

# Voorbeeld Auto 2
class auto:
    def setSnelheid(self, v):
        if v>0 and v<200:
            self.snelheid = v
        else:
            print ("Onmogelijk")

    def getSnelheid(self):
        return self.snelheid
######################################

# Voorbeeld Auto 3
class auto:
    def setSnelheid(self, v):
        if v>0 and v<200:
            self.__snelheid = v
        else:
            print ("Onmogelijk")

    def getSnelheid(self):
        return self.__snelheid
######################################

# Opdracht 1
class boom:
    def setHoogte(self,cm):
        self.hoogte = cm
        
    def setBlaadjes(self, blad):
        self.type_blaadjes = blad
        
    def getHoogte(self):
        return self.hoogte
    
    def getBlaadjes(self):
        return self.type_blaadjes
######################################

# Voorbeeld Auto 5
class auto:

    def __init__(self,v):
        self.setSnelheid(v)
        
    def setSnelheid(self, v):
        if v>0 and v<200:
            self.__snelheid = v
        else:
            print ("Onmogelijk")

    def getSnelheid(self):
        return self.__snelheid
######################################

# Opdracht 2
class boom:
    def __init__(self, blad, hoogte)
        self.setHoogte(hoogte)
        self.setBlaadjes(blad)
        
    def setHoogte(self,cm):
        self.hoogte = cm
        
    def setBlaadjes(self, blad):
        self.type_blaadjes = blad
        
    def getHoogte(self):
        return self.hoogte
    
    def getBlaadjes(self):
        return self.type_blaadjes
######################################

# Opdracht 3
class boom:
    def __init__(self, blad, hoogte):
        self.setHoogte(hoogte)
        self.setBlaadjes(blad)
        
    def setHoogte(self,cm):
        self.hoogte = cm
        
    def setBlaadjes(self, blad):
        self.type_blaadjes = blad
        
    def getHoogte(self):
        return self.hoogte
    
    def getBlaadjes(self):
        return self.type_blaadjes

class kerstboom (boom):
    def setDeco (self, deco):
        self.deco_lijst = deco
        
    def getDeco(self):
        return self.deco_lijst
######################################

# Voorbeeld Auto 6
class auto:

    def __init__(self,v):
        self.setSnelheid(v)
        
    def setSnelheid(self, v):
        if v>0 and v<200:
            self.__snelheid = v
        else:
            print ("Onmogelijk")

    def getSnelheid(self):
        return self.__snelheid

class elektrische_auto (auto):

    def __init__ (self, v, charge):
        auto.__init__(self, v)
        self.lading = charge

    def setLading(self, charge):
        self.lading = charge
        
    def getLading(self):
        return self.lading
######################################    

# Opdracht 4
class boom:
    def __init__(self, blad, hoogte):
        self.setHoogte(hoogte)
        self.setBlaadjes(blad)
        
    def setHoogte(self,cm):
        self.hoogte = cm
        
    def setBlaadjes(self, blad):
        self.type_blaadjes = blad
        
    def getHoogte(self):
        return self.hoogte
    
    def getBlaadjes(self):
        return self.type_blaadjes

class kerstboom (boom):
    def __init__(self,hoogte):
        boom.__init__(self, "naaldvormig",hoogte)
        
    def setDeco (self, deco):
        self.deco_lijst = deco
        
    def getDeco(self):
        return self.deco_lijst
######################################
