import random

class User:

    def __init__(self,
                 oid=None,
                 lastName=None,
                 firstName=None,
                 addName=None,
                 dateOfBirth=None,
                 telephoneNumber=None,
                 type="штатный",
                 workstart="1998-12-31T21:00:00.000Z",
                 workend="2050-12-30T21:00:00.000Z",
                 locale=None,
                 position={
    "id": "9afd1807-d2c0-4ae9-a3cb-eb333a25f404",
    "ids": [
        "-id-company-gk-ra",
        "895c3447-f048-499a-8424-6d7f7180467d",
        "61c5664b-b27a-4ed1-958f-3db08c1e62e2",
        "9afd1807-d2c0-4ae9-a3cb-eb333a25f404"
    ],
    "name": [
        "Госкорпорация \"Росатом\"",
        "ГК \"Росатом\"",
        "Нейтрон",
        "ГлавРеакт"
    ],
    "path": "/root/-id-company-gk-ra/895c3447-f048-499a-8424-6d7f7180467d/61c5664b-b27a-4ed1-958f-3db08c1e62e2/9afd1807-d2c0-4ae9-a3cb-eb333a25f404",
    "paths": [
        "Госкорпорация \"Росатом\"",
        "ГК \"Росатом\"",
        "Нейтрон",
        "ГлавРеакт"
    ],
    "type": "position"
},
                 contractNumber=None,
                 manager=None,
                 candContactEmployee=None,
                 candOwrp=None,
                 candPC=None,
                 candPhone=None,
                 candPlanStartDate=None,
                 candRnst=None,
                 candWorkPlace1=None,
                 candWorkPlace2=None,
                 category='A',
                 citizenship='RU',
                 costPlace=None,
                 countyOfBirth=None,
                 empNumber=None,
                 employeeType=None,
                 floorNumber=None,
                 funcManager='1ae49411-38db-4beb-8172-5f9c4969c8de',
                 gender="Male",
                 hrCategory='20',
                 hrGroup='1',
                 hrStatus='active',
                 hrSubstitute=None,
                 inn=None,
                 interNumber=None,
                 isCandidate=None,
                 locality='Никит',
                 locationCode='007',
                 main=None,
                 officeMobilePhoneNumber=None,
                 org=None,
                 passportIssueDate=None,
                 passportIssueDiv=None,
                 passportIssueDivCode=None,
                 passportNumber=None,
                 passportSeries=None,
                 placeOfBirth=None,
                 regionOfBirth=None,
                 roomNumber=None,
                 substitute=None,
                 uniqEmployeeId=None,
                 vipUser=None,
                 workplaceNumber=None):

        self.oid = oid
        self.lastName = lastName or self.generate_last_name()
        self.firstName = firstName or self.generate_first_name()
        self.additionalName = addName or self.generate_add_name()
        self.dateOfBirth = dateOfBirth or self.generate_date_of_birth()
        self.telephoneNumber = telephoneNumber or self.generate_telephone_number()
        self.type = type
        self.workend = workend
        self.workstart = workstart
        self.locale = locale
        self.position = position
        self.contractNumber = contractNumber
        self.manager = manager
        self.candContactEmployee = candContactEmployee
        self.candOwrp = candOwrp
        self.candPC = candPC
        self.candPhone = candPhone
        self.candPlanStartDate = candPlanStartDate
        self.candRnst = candRnst
        self.candWorkPlace1 = candWorkPlace1
        self.candWorkPlace2 = candWorkPlace2
        self.category = category #TODO генератор категории юзера
        self.citizenship = citizenship #TODO генератор выбора гражданства
        self.costPlace = costPlace
        self.countyOfBirth = countyOfBirth
        self.empNumber = empNumber
        self.employeeType = employeeType
        self.floorNumber = floorNumber
        self.funcManager = funcManager
        self.gender = gender
        self.hrCategory = hrCategory
        self.hrGroup = hrGroup
        self.hrStatus = hrStatus
        self.hrSubstitute = hrSubstitute
        self.inn = inn or self.generate_inn()
        self.interNumber = interNumber
        self.isCandidate = isCandidate
        self.locality = locality
        self.locationCode = locationCode #TODO генератор кода локации
        self.main = main
        self.officeMobilePhoneNumber = officeMobilePhoneNumber or self.generate_telephone_number()
        self.org = org
        self.passportIssueDate = passportIssueDate
        self.passportIssueDiv = passportIssueDiv
        self.passportIssueDivCode = passportIssueDivCode
        self.passportNumber = passportNumber or self.generate_passport_number()
        self.passportSeries = passportSeries or self.generate_passport_series()
        self.placeOfBirth = placeOfBirth
        self.regionOfBirth = regionOfBirth
        self.roomNumber = roomNumber
        self.substitute = substitute
        self.uniqEmployeeId = uniqEmployeeId
        self.vipUser = vipUser
        self.workplaceNumber = workplaceNumber


    def __repr__(self):
        return f'User with atributes --- oid: {self.oid}, ' \
               f'lastName: {self.lastName}, ' \
               f'firstName: {self.firstName}, ' \
               f'additionalName: {self.additionalName}, ' \
               f'dateOfBirth: {self.dateOfBirth}, ' \
               f'gender: {self.gender}, ' \
               f'citizenship: {self.citizenship}, ' \
               f'uniqEmployeeId: {self.uniqEmployeeId}, ' \
               f'inn: {self.inn}, ' \
               f'passportSeries: {self.passportSeries}, ' \
               f'passportNumber: {self.passportNumber}, ' \
               f'passportIssueDiv: {self.passportIssueDiv}, ' \
               f'passportIssueDivCode: {self.passportIssueDivCode}, ' \
               f'passportIssueDate: {self.passportIssueDate}, ' \
               f'countyOfBirth: {self.countyOfBirth}, ' \
               f'regionOfBirth: {self.regionOfBirth}, ' \
               f'placeOfBirth: {self.placeOfBirth}, ' \
               f'telephoneNumber: {self.telephoneNumber}, ' \
               f'type: {self.type}, ' \
               f'workstart: {self.workstart}, ' \
               f'workend: {self.workend}, ' \
               f'locale: {self.locale}, ' \
               f'contractNumber: {self.contractNumber}'

    def __eq__(self, other):
        return (self.lastName,
                self.firstName,
                self.additionalName,
                self.dateOfBirth,
                self.gender,
                self.citizenship,
                self.inn,
                self.passportSeries,
                self.passportNumber,
                self.passportIssueDiv,
                self.passportIssueDivCode,
                self.passportIssueDate,
                self.countyOfBirth,
                self.regionOfBirth,
                self.placeOfBirth,
                self.uniqEmployeeId) ==  (other.lastName,
                                           other.firstName,
                                           other.additionalName,
                                           other.dateOfBirth,
                                           other.gender,
                                           other.citizenship,
                                           other.inn,
                                           other.passportSeries,
                                           other.passportNumber,
                                           other.passportIssueDiv,
                                           other.passportIssueDivCode,
                                           other.passportIssueDate,
                                           other.countyOfBirth,
                                           other.regionOfBirth,
                                           other.placeOfBirth,
                                           other.uniqEmployeeId,)


    def return_user_data_as_json(self):
        json_data = {"additionalName": self.additionalName,
                     "candContactEmployee": self.candContactEmployee,
                     "candOwrp": self.candOwrp,
                     "candPC": self.candPC,
                     "candPhone": self.candPhone,
                     "candPlanStartDate": self.candPlanStartDate,
                     "candRnst": self.candRnst,
                     "candWorkPlace1": self.candWorkPlace1,
                     "candWorkPlace2": self.candWorkPlace2,
                     "category": self.category,
                     "citizenship": self.citizenship,
                     "costPlace": self.costPlace,
                     "countyOfBirth": self.countyOfBirth,
                     "dateOfBirth": self.dateOfBirth,
                     "empNumber": self.empNumber,
                     "employeeType": self.employeeType,
                     "firstName": self.firstName,
                     "floorNumber": self.floorNumber,
                     "funcManager": self.funcManager,
                     "gender": self.gender,
                     "hrCategory": self.hrCategory,
                     "hrGroup": self.hrGroup,
                     "hrStatus": self.hrStatus,
                     "hrSubstitute": self.hrSubstitute,
                     "inn": self.inn,
                     "interNumber": self.interNumber,
                     "isCandidate": self.isCandidate,
                     "lastName": self.lastName,
                     "locality": self.locality,
                     "locationCode": self.locationCode,
                     "main": self.main,
                     "officeMobilePhoneNumber": self.officeMobilePhoneNumber,
                     "org": self.org,
                     "passportIssueDate": self.passportIssueDate,
                     "passportIssueDiv": self.passportIssueDiv,
                     "passportIssueDivCode": self.passportIssueDivCode,
                     "passportNumber": self.passportNumber,
                     "passportSeries": self.passportSeries,
                     "placeOfBirth": self.placeOfBirth,
                     "position": self.position,
                     "regionOfBirth": self.regionOfBirth,
                     "roomNumber": self.roomNumber,
                     "substitute": self.substitute,
                     "telephoneNumber": self.telephoneNumber,
                     "uniqEmployeeId": self.uniqEmployeeId,
                     "vipUser": self.vipUser,
                     "workend": self.workend,
                     "workplaceNumber": self.workplaceNumber,
                     "workstart": self.workstart}
        return json_data

    def generate_last_name(self):
        last_name_collection = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Биткоинов", "Картошкин", "Болконский",
                                "Хренов", "Приколов", "Онегин", "Пушкин", "Ленин", "Сталин", "Брежнев", "Силуанов",
                                "Путин", "Медведев", "Зайцев", "Коровин", "Птицев", "Собакин", "Кошкин", "Пельмешкин",
                                "Дураков", "Огурцов", "Водкин", "Ивкин", "Тимофеев", "Андреев", "Соловьев", "Тараканов",
                                "Муравьев", "Абдулкахова", "Титов", "Васильев"]
        last_name = last_name_collection[random.randint(0, len(last_name_collection) - 1)]
        return last_name

    def generate_first_name(self):
        first_name_collection = ["Андрей", "Александр", "Сергей", "Тимофей", "Антон", "Петр", "Иван", "Николай",
                                 "Константин", "Анатолий", "Дмитрий", "Михаил", "Илья", "Джон", "Агафон", "Авдей",
                                 "Альберт", "Вадим", "Виталий", "Вячеслав", "Владимир", "Всеволод", "Геннадий", "Глеб",
                                 "Герасим", "Герман", "Григорий", "Даниил", "Денис", "Дорофей", "Демьян", "Евгений",
                                 "Назар", "Никита", "Эдуард", "Яков", "Ярослав", "Юлиан", "Савелий", "Святослав",
                                 "Прокопий", "Ефим", "Игнатий", "Руслан", "Ростислав", "Прохор", "Семен", "Ираклий",
                                 "Кузьма", "Лаврентий", "Лукьян"]
        first_name = first_name_collection[random.randint(0, len(first_name_collection) - 1)]
        return first_name

    def generate_add_name(self):
        add_name_collection = ["Андреевич", "Александрович", "Сергеевич", "Тимофеевич", "Антонович", "Петрович",
                               "Иванович", "Николаевич", "Константинович", "Анатольевич", "Дмитриевич", "Михайлович",
                               "Ильич", "Агафонович", "Авдеевич", "Альбертович", "Вадимович", "Витальевич",
                               "Вячеславович",
                               "Владимирович", "Всеволодович", "Геннадьевич", "Глебович", "Герасимович", "Германович",
                               "Григорьевич", "Даниилович", "Денисович", "Дорофеевич", "Демьянович", "Евгеньевич",
                               "Назарович", "Никитич", "Эдуардович", "Ярославович", "Юлианович", "Савельевич",
                               "Святославович", "Прокопьевич", "Ефимович", "Игнатьевич", "Русланович", "Ростиславович",
                               "Прохорович", "Семенович", "Ираклиевич", "Кузьмич", "Лаврентьевич", "Лукьянович"]
        add_name = add_name_collection[random.randint(0, len(add_name_collection) - 1)]
        return add_name

    def generate_date_of_birth(self):
        date_of_birth = f'19{str(random.randint(10, 99))}-02-02'
        return date_of_birth

    def generate_telephone_number(self):
        cypher_collection = [str(random.randint(0, 9)) for i in range(10)]
        tel_number = "8-{0[0]}{0[1]}{0[2]}-{0[3]}{0[4]}{0[5]}-{0[6]}{0[7]}-{0[8]}{0[9]}".format(cypher_collection)
        return tel_number

    def generate_inn(self):
        cypher_collection = [str(random.randint(0, 9)) for i in range(11)]
        inn = "{0[0]}{0[1]}{0[2]}-{0[3]}{0[4]}{0[5]}-{0[6]}{0[7]}{0[8]} {0[9]}{0[10]}".format(cypher_collection)
        return inn

    def generate_passport_number(self):
        cypher_collection = [str(random.randint(0, 9)) for i in range(6)]
        passport_number = "{0[0]}{0[1]}{0[2]}{0[3]}{0[4]}{0[]5}".format(cypher_collection)
        return passport_number

    def generate_passport_series(self):
        cypher_collection = [str(random.randint(0, 9)) for i in range(4]
        passport_series = "{0[0]}{0[1]} {0[2]}{0[3]}".format(cypher_collection)
        return passport_series


# user = User()
# params = user.__dict__.keys()
# print(user)
#
# print(params)
#
# for i in params:
#     print(getattr(user, i))
#     # print(getattr(user, i))
#     #user.i == 123



