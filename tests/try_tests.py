import requests
import random

# Через pytest удобнее запускать следующим образом: pytest -v -s api_tests.py
session = requests.session()


def test_open_login_page():
    # url = "http://10.201.48.70:8080/inrights/app/"
    url = "http://10.201.48.88:8080/inrights/app/"
    response = session.get(url)
    # response = requests.request("GET", url)
    print(response)

    if response.status_code == 200:
        print("Login page opened successfully" + "\nRequest's status code = " + str(
            response.status_code) + " \n***************")
        assert True
    else:
        print("FAILED: Requests's status = " + str(response.status_code))
        assert False


def test_login_with_administrator_credentials():
    # url = "http://10.201.48.70:8080/inrights/api/auth/login"
    url = "http://10.201.48.88:8080/inrights/api/auth/login"
    payload = {"login": "Administrator", "password": "5ecr3t"}

    response = session.post(url, params=payload)

    if response.status_code == 200 and response.headers.get('authenticationLevel') == "FULLY_AUTHENTICATED":
        print("Login with admin credentials successful" + "\nRequest's status code = " + str(response.status_code)
              + " \n***************")
        assert True
    else:
        print("FAILED: Requests's status = " + str(response.status_code))
        assert False


def test_creating_user():
    # url = "http://10.201.48.70:8080/inrights/api/user/card/new"
    url = "http://10.201.48.88:8080/inrights/api/user/card/new"

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
                           "Ильич", "Агафонович", "Авдеевич", "Альбертович", "Вадимович", "Витальевич", "Вячеславович",
                           "Владимирович", "Всеволодович", "Геннадьевич", "Глебович", "Герасимович", "Германович",
                           "Григорьевич", "Даниилович", "Денисович", "Дорофеевич", "Демьянович", "Евгеньевич",
                           "Назарович", "Никитич", "Эдуардович", "Ярославович", "Юлианович", "Савельевич",
                           "Святославович", "Прокопьевич", "Ефимович", "Игнатьевич", "Русланович", "Ростиславович",
                           "Прохорович", "Семенович", "Ираклиевич", "Кузьмич", "Лаврентьевич", "Лукьянович"]
    add_name = add_name_collection[random.randint(0, len(add_name_collection) - 1)]

    year_of_birth = random.randint(10, 99)
    date_of_birth = "19" + str(year_of_birth) + "-02-02"

    # payload = '{{"position":["d4c9a3b4-0bb9-4d13-a03b-72e46ad69698"], "manager": "null", "lastName": {lastName}, ' \
    #           '"firstName": {firstName}, "additionalName": {addName}, "dateOfBirth": {dateOfBirth}, ' \
    #           '"type": "штатный", "contractNumber": "777-999-111",' \
    #           ' "dateFrom": "1999-12-31T21:00:00.000Z", "workend": "2030-12-30T21:00:00.000Z", ' \
    #           '"locale": "null", "telephoneNumber": "8-800-555-35-35"}}' \
    #     .format(lastName=last_name, firstName=first_name, addName=add_name, dateOfBirth=date_of_birth)

    json_data = {"position": ["ab2ee738-243d-446c-b371-138478bcd528"],
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
                 "telephoneNumber": "8-800-555-35-35"}
    # ab2ee738-243d-446c-b371-138478bcd528
    # d4c9a3b4-0bb9-4d13-a03b-72e46ad69698

    headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}

    params = {"id": "users.NewUser-1"}

    response = session.put(url, json=json_data, params=params, headers=headers)

    json_response = response.json()
    print(json_data)
    print(response.status_code)

    print("Creating user - successful" + "\nRequest's status code = " + str(response.status_code))
    print("New user with name: " + str(last_name) + " " + str(first_name) + " "
          + str(add_name) + " and oid: " + json_response['oid'] + " successfully created" + "\n***************")

    # if response.status_code == 200 and json_response['oid'] is not None:
    #      print("Creating user - successful" + "\nRequest's status code = " + str(response.status_code))
    #      print("New user with name: " + str(last_name) + " " + str(first_name) + " "
    #            + str(add_name) + " and oid: " + json_response['oid'] + " successfully created" + "\n***************")
    #      assert True
    # else:
    #      print("FAILED: Requests's status = " + str(response.status_code))
    #      assert False
