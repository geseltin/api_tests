# import requests
# import random
#
# import RestHelper
#
# # Через pytest удобнее запускать следующим образом: pytest -v -s old_tests.py
# session = requests.session()
#
#
# def test_open_login_page():
#     url = "http://10.201.48.186:8080/inrights/app/"
#     response = session.get(url)
#     # response = requests.request("GET", url)
#     print(response)
#
#
#     if response.status_code == 200:
#         print("Login page opened successfully" + "\nRequest's status code = " + str(
#             response.status_code) + " \n***************")
#         assert True
#     else:
#         print("FAILED: Requests's status = " + str(response.status_code))
#         assert False
#
#
# # test_open_login_page()
#
#
# def test_login_with_administrator_credentials():
#     url = "http://10.201.48.186:8080/inrights/api/auth/login"
#     payload = {"login": "Administrator", "password": "5ecr3t"}
#
#     response = session.post(url, params=payload)
#
#     if response.status_code == 200 and response.headers.get('authenticationLevel') == "FULLY_AUTHENTICATED":
#         print("Login with admin credentials successful" + "\nRequest's status code = " + str(response.status_code)
#               + " \n***************")
#         assert True
#     else:
#         print("FAILED: Requests's status = " + str(response.status_code))
#         assert False
#
#     # print(response.headers)
#     # print(response.headers.get('authenticationLevel'))
#
#
# # test_login_with_administrator_credentials()
#
# def test_creating_user():
#     url = "http://10.199.30.136:8080/inrights/api/user/card/new"
#
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
#                            "Ильич", "Агафонович", "Авдеевич", "Альбертович", "Вадимович", "Витальевич", "Вячеславович",
#                            "Владимирович", "Всеволодович", "Геннадьевич", "Глебович", "Герасимович", "Германович",
#                            "Григорьевич", "Даниилович", "Денисович", "Дорофеевич", "Демьянович", "Евгеньевич",
#                            "Назарович", "Никитич", "Эдуардович", "Ярославович", "Юлианович", "Савельевич",
#                            "Святославович", "Прокопьевич", "Ефимович", "Игнатьевич", "Русланович", "Ростиславович",
#                            "Прохорович", "Семенович", "Ираклиевич", "Кузьмич", "Лаврентьевич", "Лукьянович"]
#     add_name = add_name_collection[random.randint(0, len(add_name_collection) - 1)]
#
#     year_of_birth = random.randint(0, 99)
#     date_of_birth = "19" + str(year_of_birth) + "-12-31T21:00:00.000Z"
#
#     payload = {"position": "cdb615aa-813e-48ad-93b5-6b24f3542e31", "org": [], "manager": "", "last_name": last_name,
#                "firstName": first_name, "additionalName": add_name, "dateOfBirth": date_of_birth,
#                "type": "подрядчик", "contractNumber": "777-999-111", "dateFrom": "1999-12-31T21:00:00.000Z",
#                "workend": "2030-12-30T21:00:00.000Z", "locale": "", "telephoneNumber": "8-800-555-35-35"}
#
#     response = session.put(url, data=payload).json()
#     new_user_oid = response(['oid'][0])
#     new_user_last_name = response(['additionalName'][0])
#     new_user_first_name = response(['firstName'][0])
#     new_user_add_name = response(['lastName'][0])
#
#     print(str(new_user_oid))
#     print(str(new_user_last_name))
#     print(str(new_user_first_name))
#     print(str(new_user_add_name))
#
#     if response.status_code == 200 and new_user_oid is not None:
#         print("Creating user - successful" + "\nRequest's status code = " + str(response.status_code)
#               + " \n***************")
#         print("User with oid =" + str(new_user_oid) + " and name: " + str(last_name) + " " + str(first_name) + " "
#               + str(add_name) + "\n***************")
#         assert True
#     else:
#         print("FAILED: Requests's status = " + str(response.status_code))
#         assert False
#
# # def test_get_user_info_by_oid(oid):
# # url = "http://10.201.48.70:8080/inrights/api/user/card/"
# # response = session.get(url, data=payload).json()
#
#
# # def test_get_role_xml():
# #     url = "http://10.201.48.186:8080/inrights/api/roles/role/00000000-0000-0000-0000-000000000004/xml"
# #
# #     payload = {"_dc": 1614317739029}
# #     headers = {}
# #
# #     response = session.get(url, headers=headers, data=payload)
# #
# #     print(response.text)
# #     print(response.status_code)
# #     print(response.url)
# #
# #
# # def test_create_role_request():
# # pass
#
# # def test_create_org_unit():
# # pass
#
# # def test_create_position():
# # pass
#
# # Назначение роли/доступа??
# # Отзыв доступа??


