import requests
import random


class RestHelper:

    def __init__(self):
        RestHelper.self = self

    def call_request(self, request_type=None, url=None, json=None,
                     headers=None, params=None, login="Administrator", password="5ecr3t"):

        auth_url = "http://10.201.48.88:8080/inrights/api/auth/login"
        payload = {"login": login, "password": password}
        print(auth_url)

        current_session = requests.session()

        response = current_session.post(auth_url, params=payload)
        if response.status_code == 200 and response.headers.get('authenticationLevel') == "FULLY_AUTHENTICATED":
            print("Login with admin credentials successful" + "\nRequest's status code = " + str(response.status_code)
                  + " \n***************")
            assert True
        else:
            print("FAILED: Requests's status = " + str(response.status_code))
            assert False

        if request_type == "GET":
            return current_session.get(url, json=json, headers=headers, params=params)
        elif request_type == "POST":
            return current_session.post(url, json=json, headers=headers, params=params)
        elif request_type == "PUT":
            return current_session.put(url, json=json, headers=headers, params=params)
        elif request_type == "DELETE":
            return current_session.delete(url, json=json, headers=headers, params=params)


class ObjectGenerators:

    def user_data(self, position="ab2ee738-243d-446c-b371-138478bcd528"):
        last_name_collection = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Биткоинов", "Картошкин", "Болконский",
                                "Хренов", "Приколов", "Онегин", "Пушкин", "Ленин", "Сталин", "Брежнев", "Силуанов",
                                "Путин", "Медведев", "Зайцев", "Коровин", "Птицев", "Собакин", "Кошкин", "Пельмешкин",
                                "Дураков", "Огурцов", "Водкин", "Ивкин", "Тимофеев", "Андреев", "Соловьев", "Тараканов",
                                "Муравьев", "Абдулкахова", "Титов", "Васильев"]
        last_name = last_name_collection[random.randint(0, len(last_name_collection) - 1)]

        first_name_collection = ["Андрей", "Александр", "Сергей", "Тимофей", "Антон", "Петр", "Иван", "Николай",
                                 "Константин", "Анатолий", "Дмитрий", "Михаил", "Илья", "Джон", "Агафон", "Авдей",
                                 "Альберт", "Вадим", "Виталий", "Вячеслав", "Владимир", "Всеволод", "Геннадий", "Глеб",
                                 "Герасим", "Герман", "Григорий", "Даниил", "Денис", "Дорофей", "Демьян", "Евгений",
                                 "Назар", "Никита", "Эдуард", "Яков", "Ярослав", "Юлиан", "Савелий", "Святослав",
                                 "Прокопий", "Ефим", "Игнатий", "Руслан", "Ростислав", "Прохор", "Семен", "Ираклий",
                                 "Кузьма", "Лаврентий", "Лукьян"]
        first_name = first_name_collection[random.randint(0, len(first_name_collection) - 1)]

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

        date_of_birth = "19{0}-02-02".format(str(random.randint(10, 99)))

        json_data = {"position": [position],
                     "manager": None,
                     "lastName": last_name,
                     "firstName": first_name,
                     "additionalName": add_name,
                     "dateOfBirth": date_of_birth,
                     "type": "штатный",
                     "contractNumber": "777-999-111",
                     "dateFrom": "1999-12-31T21:00:00.000Z",
                     "workend": "2030-12-30T21:00:00.000Z",
                     "locale": None,
                     "telephoneNumber": self.tel_number()}
        print(json_data)
        return json_data

    def tel_number(self):
        cypher_collection = [str(random.randint(0, 9)) for i in range(10)]
        tel_number = "8-{0[0]}{0[1]}{0[2]}-{0[3]}{0[4]}{0[5]}-{0[6]}{0[7]}-{0[8]}{0[9]}".format(cypher_collection)
        return tel_number


a = ObjectGenerators()
a.user_data()
