class Apartment(House): #Apartment inherits from House
    def __init__(self, pID, aptNo, rent, isVacant = False):
        self.pID = pID
        self.aptNo = aptNo
        self.rent = rent
        self.isVacant = isVacant
