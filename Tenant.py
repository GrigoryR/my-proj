class Tenant:
    def __init__(self, TenantId, FirstName, LastName):
        self._TenantId = TenantId
        self._FirstName = FirstName
        self._LastName = LastName
    
    def __init__(self):
        pass
    
    @property
    def TenantId(self):
        return self._TenantId
    
    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId
    
    @property
    def FirstName(self):
        return self._FirstName
    
    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName
    
    @property
    def LastName(self):
        return self._LastName
    
    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName
    
    @property
    def MoveInDate(self):
        return self._MoveInDate
        
    @MoveInDate.setter
    def MoveInDate(self, MoveInDate):
        self._MoveInDate = MoveInDate
    
    @property
    def MoveOutDate(self):
        return self._MoveOutDate
        
    @MoveOutDate.setter
    def MoveOutDate(self, MoveOutDate):
        self._MoveOutDate = MoveOutDate
    
    @property
    def CurrentTenant(self):
        if MoveOutDate == None:
            self._CurrentTenant = True
        else:
            self._CurrentTenant = False
        return self._CurrentTenant
    
    #Functionality
    def AddNewTenant():
        pass
    
    def ArchivePastTenant():
        pass
    
    def GetAllTenants():
        pass
    
    def GetCurrentTenants():
        pass
    
    def GetTenantById(TenantId):
        pass
    
    def UpdateTenant(Tenant):
        pass
