import requests
from rest_helper import RestHelper
from rest_helper import ObjectGenerators
from org_helper import OrgHelper

# Через pytest удобнее запускать следующим образом: pytest -v -s api_tests.py
# session = requests.session()


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


# def test_creating_user():
#     url = "http://10.201.48.88:8080/inrights/api/user/card/new"
#     headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
#     params = {"id": "users.NewUser-1"}
#
#     rest_helper = RestHelper()
#     object_generator = ObjectGenerators()
#     json = object_generator.user_data()
#     # print(json)
#
#     response = rest_helper.call_request(request_type="PUT", url=url, json=json, headers=headers, params=params)
#
#     json_response = response.json()
#     print(json_response)




    # print(response.status_code)
#
#     items = json_response['items']
#     for i in items:
#         if i['name'] == 'lastName':
#             new_user_last_name = i['value']
#
#     for i in items:
#         if i['name'] == 'firstName':
#             new_user_first_name = i['value']
#
#     for i in items:
#         if i['name'] == 'additionalName':
#             new_user_add_name = i['value']
#
#     new_user_oid = json_response['oid']
#     # new_user_last_name = json_response['items'][0]['value']
#     # new_user_first_name = json_response['items'][2]['value']
#     # new_user_add_name = json_response['items'][4]['value']
#
#     print(str(new_user_oid))
#     print(str(new_user_last_name))
#     print(str(new_user_first_name))
#     print(str(new_user_add_name))
#
#     url = f"http://10.201.48.88:8080/inrights/api/user/card/{new_user_oid}"
#     params = None
#     headers = None
#     response = rest_helper.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
#     json_response_from_get_request = response.json()
#
#     json_items_from_get_request = json_response_from_get_request['items']
#
#     for i in json_items_from_get_request:
#         if i['name'] == 'lastName':
#             new_user_last_name_from_get_request = i['value']
#
#     for i in json_items_from_get_request:
#         if i['name'] == 'firstName':
#             new_user_first_name_from_get_request = i['value']
#
#     for i in json_items_from_get_request:
#         if i['name'] == 'additionalName':
#             new_user_add_name_from_get_request = i['value']
#
#     test_result = []
#
#     if new_user_add_name == new_user_add_name_from_get_request:
#         test_result.append('PASS')
#     else:
#         test_result.append('FAIL')
#
#     if new_user_first_name == new_user_first_name_from_get_request:
#         test_result.append('PASS')
#     else:
#         test_result.append('FAIL')
#
#     if new_user_last_name == new_user_last_name_from_get_request:
#         test_result.append('PASS')
#     else:
#         test_result.append('FAIL')
#
#     print(test_result)
#
#     if 'FAIL' in test_result:
#         assert False
#     else:
#         assert True

    # print(f"Creating user - successful" + "\nRequest's status code = {str(response.status_code)}")
    # print("New user with name: " + str(new_user_last_name) + " " + str(new_user_first_name) + " "
    #       + str(new_user_add_name) + " and oid: " + json_response[
    #           'oid'] + " successfully created" + "\n***************")

    # if response.status_code == 200 and json_response['oid'] is not None:
    #      print("Creating user - successful" + "\nRequest's status code = " + str(response.status_code))
    #      print("New user with name: " + str(last_name) + " " + str(first_name) + " "
    #            + str(add_name) + " and oid: " + json_response['oid'] + " successfully created" + "\n***************")
    #      assert True
    # else:
    #      print("FAILED: Requests's status = " + str(response.status_code))
    #      assert False

    # def test_create_company():
    #     org = OrgHelper()
    #     org.create_companyType()


