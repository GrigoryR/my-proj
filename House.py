class House:
    def __init__(self, pID, pStreetAddr, pCity = "Philadelphia", pState = "PA", pZip, pAptCount):
        self.pID = pID
        self.pAptCount = pAptCount
        self.pCity = pCity
        self.pState = pState
        self.pStreetAddr = pStreetAddr
        self.pZip = pZip
    @property
    def p(self):
        return self._p
    @pID.setter
    def pID(self,pID):
        self._pID = pID
    
    @property
    def pAptCount(self):
        return self._pAptCount
    @pAptCount.setter
    def pAptCount(self,pAptCount)
        self._pAptCount = pAptCount
    @property
    def pCity(self):
        return self._pCity
    @pCity.setter
    def pCity(self,pCity)
        self._pCity = pCity
    @property
    def pState(self):
        return self._pState
    @pState.setter
    def pState(self,pState)
        self._pState = pState
    @property
    def pStreetAddr(self):
        return self._pStreetAddr
    @pStreetAddr.setter
    def pStreetAddr(self,pStreetAddr)
        self._pStreetAddr = pStreetAddr
    @property
    def pZip(self):
        return self._pZip
    @pZip.setter
    def pZip(self,pZip)
        self._pZip = pZip
        
    
