import requests
import random
from rest_helper import RestHelper
from rest_helper import ObjectGenerators

# Через pytest удобнее запускать следующим образом: pytest -v -s api_tests.py
session = requests.session()


def test_open_login_page():
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
    url = "http://10.201.48.88:8080/inrights/api/user/card/new"
    headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
    params = {"id": "users.NewUser-1"}
    json = ObjectGenerators.user_data

    response = self.RestHelper.call_request(request_type="PUT", url=url, json=json, headers=headers, params=params)

    json_response = response.json()
    print(json_response)
    print(response.status_code)
    new_user_oid = response(['oid'][0])
    new_user_last_name = response(['additionalName'][0])
    new_user_first_name = response(['firstName'][0])
    new_user_add_name = response(['lastName'][0])

    print(str(new_user_oid))
    print(str(new_user_last_name))
    print(str(new_user_first_name))
    print(str(new_user_add_name))

    print("Creating user - successful" + "\nRequest's status code = " + str(response.status_code))
    print("New user with name: " + str(new_user_last_name) + " " + str(new_user_first_name) + " "
          + str(new_user_add_name) + " and oid: " + json_response[
              'oid'] + " successfully created" + "\n***************")

    # if response.status_code == 200 and json_response['oid'] is not None:
    #      print("Creating user - successful" + "\nRequest's status code = " + str(response.status_code))
    #      print("New user with name: " + str(last_name) + " " + str(first_name) + " "
    #            + str(add_name) + " and oid: " + json_response['oid'] + " successfully created" + "\n***************")
    #      assert True
    # else:
    #      print("FAILED: Requests's status = " + str(response.status_code))
    #      assert False
