from helpers.rest_helper import RestHelper
from helpers.user_helper import UserHelper
from helpers.org_helper import OrgHelper
from helpers.request_helper import RequestHelper
from model.user import User
from model.division import Division
from model.company import Company
from model.position import Position



# Через pytest удобнее запускать следующим образом: pytest -v -s old_tests.py


# Авторизации в системе админом DONE
# def test_admin_autorization():
#     rh = RestHelper()
#     rh.call_request()


# Создание юзера DONE
# def test_creating_user():
#
#     initial_user = User()
#     uh = UserHelper()
#
#     created_user = uh.create_user(user=initial_user)
#
#     user_get_by_oid = uh.get_user_data_by_oid(oid=created_user.oid)
#
#     uh.compare_user_data(created_user, user_get_by_oid)


# Создание заявки/различных видов заявок
# def test_create_request():
#     initial_user = User()
#     requestHelper = RequestHelper()
#     userHelper = UserHelper()
#     created_user = userHelper.create_user(user=initial_user)
#     created_user_employment = userHelper.get_employment_by_user_oid(oid=created_user.oid)
#     requestHelper.check_and_publicate_applications_for_position(position_oid=created_user_employment.position['id'])
#     requestHelper.create_request(employment_oid=created_user_employment.id)

#
# # Создание компании DONE
# def test_create_company():
#     initial_company = Company()
#     orgHelper = orgHelper()
#
#     created_company = orgHelper.create_company_type(initial_company=initial_company)
#
#     company_get_by_oid = orgHelper.get_company_by_oid(company_oid=created_company.oid)
#
#     orgHelper.compare_company_data(created_company=created_company, company_get_by_oid=company_get_by_oid)
# # Создание подразделения DONE
# def test_create_division():
#     initial_division = Division()
#     orgHelper = OrgHelper()
#
#     created_division = orgHelper.create_division(initial_division=initial_division, parent_id='3252e137-98db-47a5-bae7-6cf947ddfdaf')
#
#     division_get_by_oid = orgHelper.get_division_by_oid(division_oid=created_division.oid)
#
#     orgHelper.compare_division_data(created_division=created_division, division_get_by_oid=division_get_by_oid)
# # Создание должности DONE
# def test_create_position():
#     initial_position = Position()
#     orgHelper = OrgHelper()
#
#     created_position = orgHelper.create_position(parent_division_oid='передать оид созданного ранее подразделения')
#
#     position_get_by_oid = orgHelper.get_children_by_parent_node_oid(parent_oid='передать оид ранее созданного подразделения', child_oid='передать оид созданной должности')
#
#     orgHelper.compare_position_data(created_position=None, position_get_by_oid=None)
# # Создание орг стурктуры DONE
# def test_create_org_structure():
#     orgHelper = OrgHelper()
#     initial_company = Company()
#     initial_division = Division()
#     initial_position = Position()
#
#     created_company = orgHelper.create_company_type(initial_company=initial_company)
#     company_get_by_oid = orgHelper.get_company_by_oid(company_oid=created_company.oid)
#     orgHelper.compare_company_data(created_company=created_company,
#                                    company_get_by_oid=company_get_by_oid)
#
#     created_division = orgHelper.create_division(initial_division=initial_division,
#                                                  parent_id=created_company.oid)
#     division_get_by_oid = orgHelper.get_division_by_oid(division_oid=created_division.oid)
#     orgHelper.compare_division_data(created_division=created_division,
#                                     division_get_by_oid=division_get_by_oid)
#
#     created_position = orgHelper.create_position(parent_division_oid=created_division.oid)
#     position_get_by_oid = orgHelper.get_children_by_parent_node_oid(parent_oid=created_division.oid,
#                                                                     child_oid=created_position.id)
#     orgHelper.compare_position_data(created_position=created_position,
#                                     position_get_by_oid=position_get_by_oid)






# Назначение/отзыв доступов (по заявке - невозможно, попробовать назначить базовыми и проверить наличие УЗ ГК + ящик??)

def test_find_parent():
    orgHelper = OrgHelper()
    orgHelper._find_parent_for_position(position_oid ='568649f6-f4ab-4e9f-be7f-a502693f1dd7')









# def test_open_login_page():
#     url = "http://10.201.48.186:8080/inrights/app/"
#     response = requests.get(url)
#     # response = requests.request("GET", url)
#     # print(response)
#
#     if response.status_code == 200:
#         print("Login page opened successfully" + "\nRequest's status code = " + str(
#             response.status_code) + " \n***************")
#         assert True
#     else:
#         print("FAILED: Requests's status = " + str(response.status_code))
#         assert False

# def test_create_company():
#     url = "http://10.201.48.186:8080/inrights/api/companies/new"
#     headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
#     params = {"sort": ""}
#
#     rest_helper = RestHelper()
#     json = {'fullName': "API Company Don't touch", 'shortName': "API Comp"}
#
#     response = rest_helper.call_request(request_type="POST", url=url, json=json, headers=headers, params=params)
#     json_response = response.json()['id']
#
#     print(json_response)

# def test_create_division():
#     url = "http://10.201.48.186:8080/inrights/api/division/card/new"
#     headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
#     params = {"sort": ""}
#
#     rest_helper = RestHelper()
#     json = {"fullName":"api division",
#             "shortName":"api div",
#             "parentOrgs":{"id":"876412c3-4fab-4c12-b42f-7a40a1b38267",
#                           "name":["Api company"],
#                           "ids":["876412c3-4fab-4c12-b42f-7a40a1b38267"],
#                           "paths":["Api test"],
#                           "type":"org"},"manager": None}
