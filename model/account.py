

class Account:

    def __init__(self,
                 canViewDetails=None,
                 createdDate=None,
                 disabled=None,
                 entitlements=None,
                 id=None,
                 lastLoginDate=None,
                 name=None,
                 resourceName=None,
                 technologic=None):
        self.canViewDetails = canViewDetails
        self.createdDate = createdDate
        self.disabled = disabled
        self.entitlements = entitlements
        self.id = id
        self.lastLoginDate = lastLoginDate
        self.name = name
        self.resourceName = resourceName
        self.technologic = technologic

    def __repr__(self):
        return f'Account --- canViewDetails:{self.canViewDetails}, ' \
               f'createdDate: {self.createdDate}, ' \
               f'disabled: {self.disabled}, ' \
               f'entitlements: {self.entitlements}, ' \
               f'id: {self.id}, ' \
               f'lastLoginDate: {self.lastLoginDate}, ' \
               f'name: {self.name}, ' \
               f'resourceName: {self.resourceName}, ' \
               f'technologic: {self.technologic}'

