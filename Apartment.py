class Apartment(House): #Apartment inherits from House
    def __init__(self, pID, aptNo, rent, isVacant = False):
        self.pID = pID
        self.aptNo = aptNo
        self.rent = rent
        self.isVacant = isVacant
        
    @property
    def pID(self):
        return self._pID
    
    @setter.pID
    def pID(self, pID):
        self._pID = pID
        
    @property
    def aptNo(self):
        return self._aptNo
    
    @setter.pID
    def aptNo(self, aptNo):
        self._aptNo = aptNo
        
    @property
    def rent(self):
        return self._rent
    
    @setter.rent
    def pID(self, rent):
        self._rent = rent
        
    @property
    def isVacant(self):
        return self._isVacant
    
    @setter.isVacant
    def isVacant(self, isVacant):
        self._isVacant = isVacant
