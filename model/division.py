import random

class Division:

    def __init__(self,
                 fullName=None,
                 shortName=None,
                 hr_obj_id=None,
                 bukrs=None,
                 parentOrgs=[None],
                 companyAdOu=None,
                 oid=None,
                 globalId=None):
        full_division_name = self._generate_division_name()

        self.fullName = fullName or full_division_name[0] + ' ' + full_division_name[1]
        self.shortName = shortName or full_division_name[1]
        self.hrObjId = hr_obj_id
        self.bukrs = bukrs or self._generate_bukrs()
        self.parentOrgs = parentOrgs
        self.companyAdOu = companyAdOu
        self.oid = oid
        self.globalId = globalId

    def __repr__(self):
        return f'Division: fullName: {self.fullName}, shortName: {self.shortName}, hrObjId: {self.hrObjId}, ' \
               f'bukrs: {self.bukrs}, parentOrg: {self.parentOrgs}, companyAdOu: {self.companyAdOu}, oid: {self.oid}' \
               f', globalId: {self.globalId}'

    def _generate_division_name(self):
        first_name_part = random.choice(['Управление', 'Отдел', 'Подразделение', 'Департамент'])
        second_name_part = random.choice(['секретариата', 'администрирования', 'разработки', 'проектирования', 'делопроизводства'])
        full_divison_name = [first_name_part, second_name_part]
        return full_divison_name

    def _generate_bukrs(self):
        bukrs = ''
        for number in range(4):
            bukrs += str(random.randint(0, 9))
        return bukrs

    def return_division_data_as_json(self):
        json_data = {'bukrs': self.bukrs,
                     'companyAdOu': self.companyAdOu,
                     'fullName': self.fullName,
                     'globalId': self.globalId,
                     'hr_obj_id': self.hrObjId,
                     'parentOrgs': self.parentOrgs,
                     'shortName': self.shortName}
        return json_data

    def __eq__(self, other):
        return (self.bukrs, self.companyAdOu, self.fullName, self.shortName, self.oid) == \
               (other.bukrs, other.companyAdOu, other.fullName, other.shortName, other.oid)

