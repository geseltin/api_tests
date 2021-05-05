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
                 dateFrom="1998-12-31T21:00:00.000Z",
                 workend="2050-12-30T21:00:00.000Z",
                 locale=None,
                 positionOid=["4ff0f334-66d3-42fe-beb6-2965ba3ed830"],
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
                 funcManager='Должен быть реальный юзер',
                 gender=None,
                 hrCategory='20',
                 hrGroup='1',
                 hrStatus='active',
                 hrSubstitute=None,
                 inn=None,
                 interNumber=None,
                 isCandidate=None,
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
        self.dateFrom = dateFrom
        self.workend = workend
        self.locale = locale
        self.positionOid = positionOid
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
        self.locationCode = locationCode #TODO генератор кода локации
        self.main = main
        self.officeMobilePhoneNumber = officeMobilePhoneNumber or self.generate_telephone_number()
        self.org = org
        self.passportIssueDate = passportIssueDate
        self.passportIssueDiv = passportIssueDiv
        self.passportIssueDivCode = passportIssueDivCode
        self.passportNumber = passportNumber
        self.passportSeries = passportSeries
        self.placeOfBirth = placeOfBirth
        self.regionOfBirth = regionOfBirth
        self.roomNumber = roomNumber
        self.substitute = substitute
        self.uniqEmployeeId = uniqEmployeeId
        self.vipUser = vipUser
        self.workplaceNumber = workplaceNumber

    def __repr__(self):
        return f'User with atributes --- oid: {self.oid}, ' \
               f'last_name: {self.lastName}, ' \
               f'first_name: {self.firstName}, ' \
               f'add_name: {self.additionalName}, ' \
               f'dateOfBirth: {self.dateOfBirth}, ' \
               f'telephoneNumber: {self.telephoneNumber}, ' \
               f'type: {self.type}, ' \
               f'dateFrom: {self.dateFrom}, ' \
               f'workend: {self.workend}, ' \
               f'locale: {self.locale}, ' \
               f'positionOid: {self.positionOid}, ' \
               f'contractNumber: {self.contractNumber}'

    def __eq__(self, other):
        return (self.lastName,
                self.firstName,
                self.additionalName,
                self.dateOfBirth,
                self.telephoneNumber,
                self.dateFrom,
                self.workend,
                self.locale,
                self.positionOid,
                self.contractNumber) == (other.lastName,
                                           other.firstName,
                                           other.additionalName,
                                           other.dateOfBirth,
                                           other.telephoneNumber,
                                           other.dateFrom,
                                           other.workend,
                                           other.locale,
                                           other.positionOid,
                                           other.contractNumber)



    def return_user_data_as_json(self):
        json_data = {"position": self.positionOid,
                     "manager": self.manager,
                     "lastName": self.lastName,
                     "firstName": self.firstName,
                     "additionalName": self.additionalName,
                     "dateOfBirth": self.dateOfBirth,
                     "type": self.type,
                     "contractNumber": self.contractNumber,
                     "dateFrom": self.dateFrom,
                     "workend": self.workend,
                     "locale": self.locale,
                     "telephoneNumber": self.telephoneNumber}
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


# user = User()
# params = user.__dict__.keys()
#
# print(params)
#
# for i in params:
#     print(getattr(user, i))
#     # print(getattr(user, i))
#     #user.i == 123



additionalName: "Отечество"
candContactEmployee: null
candOwrp: null
candPC: null
candPhone: null
candPlanStartDate: null
candRnst: null
candWorkPlace1: null
candWorkPlace2: null
category: "А"
citizenship: "RU"
costPlace: null
countyOfBirth: null
dateOfBirth: "1994-12-31T21:00:00.000Z"
empNumber: null
employeeType: null
firstName: "Имене"
floorNumber: null
funcManager: "1ae49411-38db-4beb-8172-5f9c4969c8de"
gender: null
hrCategory: "20"
hrGroup: "1"
hrStatus: "active"
hrSubstitute: null
inn: null
interNumber: null
isCandidate: null
lastName: "Фалафилия"
locality: "Никитски"
locationCode: "007"
main: null
officeMobilePhoneNumber: null
org: null
passportIssueDate: null
passportIssueDiv: null
passportIssueDivCode: null
passportNumber: null
passportSeries: null
placeOfBirth: null
position: {id: "9afd1807-d2c0-4ae9-a3cb-eb333a25f404",…}
regionOfBirth: null
roomNumber: null
substitute: null
telephoneNumber: null
uniqEmployeeId: null
vipUser: null
workend: null
workplaceNumber: null
workstart: "1998-12-31T21:00:00.000Z"

{"lastName":"Фалафилия","firstName":"Имене","additionalName":"Отечество","dateOfBirth":"1994-12-31T21:00:00.000Z","gender":null,"citizenship":"RU","uniqEmployeeId":null,"inn":null,"passportSeries":null,"passportNumber":null,"passportIssueDiv":null,"passportIssueDivCode":null,"passportIssueDate":null,"countyOfBirth":null,"regionOfBirth":null,"placeOfBirth":null,"empNumber":null,"category":"А","position":{"id":"9afd1807-d2c0-4ae9-a3cb-eb333a25f404","ids":["-id-company-gk-ra","895c3447-f048-499a-8424-6d7f7180467d","61c5664b-b27a-4ed1-958f-3db08c1e62e2","9afd1807-d2c0-4ae9-a3cb-eb333a25f404"],"name":["Госкорпорация \"Росатом\"","ГК \"Росатом\"","Нейтрон","ГлавРеакт"],"path":"/root/-id-company-gk-ra/895c3447-f048-499a-8424-6d7f7180467d/61c5664b-b27a-4ed1-958f-3db08c1e62e2/9afd1807-d2c0-4ae9-a3cb-eb333a25f404","paths":["Госкорпорация \"Росатом\"","ГК \"Росатом\"","Нейтрон","ГлавРеакт"],"type":"position"},"org":null,"hrStatus":"active","workstart":"1998-12-31T21:00:00.000Z","workend":null,"funcManager":"1ae49411-38db-4beb-8172-5f9c4969c8de","substitute":null,"hrSubstitute":null,"hrGroup":"1","hrCategory":"20","employeeType":null,"costPlace":null,"vipUser":null,"telephoneNumber":null,"officeMobilePhoneNumber":null,"interNumber":null,"locality":"Никитски","locationCode":"007","workplaceNumber":null,"floorNumber":null,"roomNumber":null,"candWorkPlace1":null,"candWorkPlace2":null,"candPlanStartDate":null,"candContactEmployee":null,"candPC":null,"candPhone":null,"candOwrp":null,"candRnst":null,"main":null,"isCandidate":null}


