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
                 manager=None):
        self.oid = oid
        self.lastName = lastName or self.generate_last_name()
        self.firstName = firstName or self.generate_first_name()
        self.addName = addName or self.generate_add_name()
        self.dateOfBirth = dateOfBirth or self.generate_date_of_birth()
        self.telephoneNumber = telephoneNumber or self.generate_telephone_number()
        self.type = type
        self.dateFrom = dateFrom
        self.workend = workend
        self.locale = locale
        self.positionOid = positionOid
        self.contractNumber = contractNumber
        self.manager = manager

    def __repr__(self):
        return f'User with atributes --- oid: {self.oid}, ' \
               f'last_name: {self.lastName}, ' \
               f'first_name: {self.firstName}, ' \
               f'add_name: {self.addName}, ' \
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
                self.addName,
                self.dateOfBirth,
                self.telephoneNumber,
                self.dateFrom,
                self.workend,
                self.locale,
                self.positionOid,
                self.contractNumber) == (other.lastName,
                                           other.firstName,
                                           other.addName,
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
                     "additionalName": self.addName,
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


# user = User()
# params = user.__dict__.keys()
#
# print(params)
#
# for i in params:
#     print(getattr(user, i))
#     # print(getattr(user, i))
#     #user.i == 123






