import random

class Position:
    def __init__(self, checkable=None,
                 children=None,
                 disabled=False,
                 disabledDate=None,
                 expanded=False,
                 fromEks=False,
                 fullName=None,
                 hasChildren=False,
                 hasRootOrg=False,
                 id=None,
                 name=None,
                 clientId=None,
                 iconCls='position',
                 orgLeaf=False,
                 parentId=None,
                 type='position',
                 parent=None,
                 parentRoot=False,
                 uiExtensions=None):

        self.checkable = checkable
        self.children = children
        self.disabled = disabled
        self.disabledDate = disabledDate
        self.expanded = expanded
        self.fromEks = fromEks
        self.fullName = fullName
        self.hasChildren = hasChildren
        self.hasRootOrg = hasRootOrg
        self.id = id
        self.name = name or self._generate_position_name()
        self.clientId = clientId
        self.iconCls = iconCls
        self.orgLeaf = orgLeaf
        self.parentId = parentId
        self.type = type
        self.parent = parent
        self.parentRoot = parentRoot
        self.uiExtensions = uiExtensions

    def __repr__(self):
        return f'Position - id: {self.id}, name: {self.name}, clientId: {self.clientId}, disabled: {self.disabled}, ' \
               f'disabledDate: {self.disabledDate}, fromEks: {self.fromEks}, parentId: {self.parentId}, ' \
               f'parentRoot: {self.parentRoot}, parent: {self.parent}'

    def __eq__(self, other):
        return (self.id, self.name, self.clientId, self.disabled, self.disabledDate, self.fromEks ) == \
               (other.id, other.name, other.clientId, other.disabled, other.disabledDate, other.fromEks  )

    def _generate_position_name(self):
        position_name = random.choice(['Специалист', 'Старший специалист', 'Ведущий специалист', 'Главный специалист',
                                       'Заместитель', 'Руководитель', 'Младший специалист', 'Джун', 'Мидл', 'Сеньор',
                                       'Стажёр', 'Инженер', 'Старший инженер', 'Главный инженер'])
        return position_name

    def return_position_data_as_json(self):
        json_data = {'clientId': self.clientId, 'iconCls': self.iconCls, 'id': self.id,
                     'name': self.name, 'orgLeaf': self.orgLeaf, 'parentId': self.parentId, 'type': self.type}
        return json_data
