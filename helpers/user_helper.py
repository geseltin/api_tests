from helpers.rest_helper import RestHelper
import random


class UserHelper:

    def create_user(self):
        url = "http://10.201.48.88:8080/inrights/api/user/card/new"
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"id": "users.NewUser-1"}

        rest_helper = RestHelper()
        json = self.user_data(position="ab2ee738-243d-446c-b371-138478bcd528")
        print(json)

        response = rest_helper.call_request(request_type="PUT", url=url, json=json, headers=headers, params=params)

        json_response = response.json()

        items = json_response['items']
        for i in items:
            if i['name'] == 'lastName':
                new_user_last_name = i['value']

        for i in items:
            if i['name'] == 'firstName':
                new_user_first_name = i['value']

        for i in items:
            if i['name'] == 'additionalName':
                new_user_add_name = i['value']

        new_user_oid = json_response['oid']

        print(f'Created user OID: {str(new_user_oid)}')
        print(f'Created user lastName: {str(new_user_last_name)}')
        print(f'Created user firstName: {str(new_user_first_name)}')
        print(f'Created user addName: {str(new_user_add_name)}')

        return json_response

    def get_user_data_by_oid(self, json_response):
        print(json_response)

    # def user_data(self, position="ab2ee738-243d-446c-b371-138478bcd528"):
    #     last_name_collection = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Биткоинов", "Картошкин", "Болконский",
    #                             "Хренов", "Приколов", "Онегин", "Пушкин", "Ленин", "Сталин", "Брежнев", "Силуанов",
    #                             "Путин", "Медведев", "Зайцев", "Коровин", "Птицев", "Собакин", "Кошкин", "Пельмешкин",
    #                             "Дураков", "Огурцов", "Водкин", "Ивкин", "Тимофеев", "Андреев", "Соловьев", "Тараканов",
    #                             "Муравьев", "Абдулкахова", "Титов", "Васильев"]
    #     last_name = last_name_collection[random.randint(0, len(last_name_collection) - 1)]
    #
    #     first_name_collection = ["Андрей", "Александр", "Сергей", "Тимофей", "Антон", "Петр", "Иван", "Николай",
    #                              "Константин", "Анатолий", "Дмитрий", "Михаил", "Илья", "Джон", "Агафон", "Авдей",
    #                              "Альберт", "Вадим", "Виталий", "Вячеслав", "Владимир", "Всеволод", "Геннадий", "Глеб",
    #                              "Герасим", "Герман", "Григорий", "Даниил", "Денис", "Дорофей", "Демьян", "Евгений",
    #                              "Назар", "Никита", "Эдуард", "Яков", "Ярослав", "Юлиан", "Савелий", "Святослав",
    #                              "Прокопий", "Ефим", "Игнатий", "Руслан", "Ростислав", "Прохор", "Семен", "Ираклий",
    #                              "Кузьма", "Лаврентий", "Лукьян"]
    #     first_name = first_name_collection[random.randint(0, len(first_name_collection) - 1)]
    #
    #     add_name_collection = ["Андреевич", "Александрович", "Сергеевич", "Тимофеевич", "Антонович", "Петрович",
    #                            "Иванович", "Николаевич", "Константинович", "Анатольевич", "Дмитриевич", "Михайлович",
    #                            "Ильич", "Агафонович", "Авдеевич", "Альбертович", "Вадимович", "Витальевич",
    #                            "Вячеславович",
    #                            "Владимирович", "Всеволодович", "Геннадьевич", "Глебович", "Герасимович", "Германович",
    #                            "Григорьевич", "Даниилович", "Денисович", "Дорофеевич", "Демьянович", "Евгеньевич",
    #                            "Назарович", "Никитич", "Эдуардович", "Ярославович", "Юлианович", "Савельевич",
    #                            "Святославович", "Прокопьевич", "Ефимович", "Игнатьевич", "Русланович", "Ростиславович",
    #                            "Прохорович", "Семенович", "Ираклиевич", "Кузьмич", "Лаврентьевич", "Лукьянович"]
    #     add_name = add_name_collection[random.randint(0, len(add_name_collection) - 1)]
    #
    #     date_of_birth = "19{0}-02-02".format(str(random.randint(10, 99)))
    #
    #     json_data = {"position": [position],
    #                  "manager": None,
    #                  "lastName": last_name,
    #                  "firstName": first_name,
    #                  "additionalName": add_name,
    #                  "dateOfBirth": date_of_birth,
    #                  "type": "штатный",
    #                  "contractNumber": "777-999-111",
    #                  "dateFrom": "1999-12-31T21:00:00.000Z",
    #                  "workend": "2030-12-30T21:00:00.000Z",
    #                  "locale": None,
    #                  "telephoneNumber": self.tel_number()}
    #     return json_data
    #
    # def tel_number(self):
    #     cypher_collection = [str(random.randint(0, 9)) for i in range(10)]
    #     tel_number = "8-{0[0]}{0[1]}{0[2]}-{0[3]}{0[4]}{0[5]}-{0[6]}{0[7]}-{0[8]}{0[9]}".format(cypher_collection)
    #     return tel_number



