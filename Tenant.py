class Tenant:
    def __init__(self, TenantId, FirstName, LastName):
        self._TenantId = TenantId
        self._FirstName = FirstName
        self._LastName = LastName
    
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
