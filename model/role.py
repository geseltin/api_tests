

class Role(displayName=None,
           description=None,
           roleType="СЦУДП",
           requestable=True,
           owner=None):

    def __init__(self):
        self.displayName = displayName
        self.description = description
        self.roleType = roleType
        self.requestable = requestable
        self.owner = owner

    def __repr__(self):
        return f'Role with parametres: {self.displayName}, ' \
                f'{self.description}, ' \
                f'{self.roleType}, ' \
                f'{self.requestable}, ' \
                f'{self.owner}'


    def __eq__(self, other):
        return (self.displayName,
                self.description,
                self.roleType,
                self.requestable,
                self.owner) == (other.displayName,
                                other.description,
                                other.roleType,
                                other.requestable,
                                other.owner)

    def role_data_as_json(self):
        json={"displayName": self.displayName,
              "description": self.description,
              "roleType": self.roleType,
              "requestable": self.requestable,
              "owner": self.owner}
        return json