from helpers.rest_helper import RestHelper
import random
from model.user import User


class UserHelper:
    def __init__(self):
        self.rest = RestHelper()


    def create_user(self, user):
        url = "http://10.201.48.186:8080/inrights/api/user/card/new"
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"id": "users.NewUser-1"}

        json = user.return_user_data_as_json()

        response = self.rest.call_request(request_type="PUT", url=url, json=json, headers=headers, params=params)

        created_user = User()


        self.fill_user_data_with_response(created_user, response)

        # for i in items:
        #     if i['name'] == 'lastName':
        #         created_user.lastName = i['value']
        #
        # for i in items:
        #     if i['name'] == 'firstName':
        #         created_user.firstName = i['value']
        #
        # for i in items:
        #     if i['name'] == 'additionalName':
        #         created_user.addName = i['value']
        #
        # for i in items:
        #     if i['name'] == 'dateOfBirth':
        #         created_user.dateOfBirth = i['value']
        #
        # for i in items:
        #     if i['name'] == 'type':
        #         created_user.type = i['value']
        #
        # for i in items:
        #     if i['name'] == 'contractNumber':
        #         created_user.contractNumber = i['value']
        #
        # for i in items:
        #     if i['name'] == 'dateFrom':
        #         created_user.dateFrom = i['value']
        #
        # for i in items:
        #     if i['name'] == 'workend':
        #         created_user.workend = i['value']
        #
        # for i in items:
        #     if i['name'] == 'locale':
        #         created_user.locale = i['value']
        #
        # for i in items:
        #     if i['name'] == 'telephoneNumber':
        #         created_user.telephoneNumber = i['value']

        # created_user.oid = json_response['oid']
        # user.oid = json_response['oid']

        # print(f'Created user OID: {str(new_user_oid)}')
        # print(f'Created user lastName: {str(new_user_last_name)}')
        # print(f'Created user firstName: {str(new_user_first_name)}')
        # print(f'Created user addName: {str(new_user_add_name)}')
        # print(created_user)
        # print("*************")
        # print(user)

        assert user.__eq__(created_user)

    def fill_user_data_with_response(self, user_object, response):
        json_response = response.json()
        items = json_response['items']

        param_list = user_object.__dict__.keys()

        for param in list(param_list):
            print(param)
            for item in items:
                if i['name'] == param:
                    setattr(user_object, param, item['value'])

        return user_object


    def get_user_data_by_oid(self, oid):
        url = f"http://10.201.48.186:8080/inrights/api/user/card/{oid}"
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = None
        json = None

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)

        user_data = User()
        self.fill_user_data_with_response(user_data, response)

        print(user_data)


a = UserHelper()
a.get_user_data_by_oid("1ae49411-38db-4beb-8172-5f9c4969c8de")







