from helpers.rest_helper import RestHelper
import random
from model.user import User
from  helpers.app_url import appUrl


class UserHelper:
    def __init__(self):
        self.rest = RestHelper()
        self.appUrl = appUrl


    def create_user(self, user):
        url = f'{appUrl}/inrights/api/user/card/new'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"id": "users.NewUser-1"}

        json = user.return_user_data_as_json()

        response = self.rest.call_request(request_type="PUT", url=url, json=json, headers=headers, params=params)
        json_response = response.json()

        created_user = User()
        print(f'initial user {user}')

        self.fill_user_data_from_response(created_user, json_response)
        print(f'created by rest {created_user}')

        assert user.__eq__(created_user)
        setattr(user, 'oid', created_user.oid)
        #print(user)
       # print(created_user)
        return created_user

    def fill_user_data_from_response(self, user_object, json_response):

        # print(f'This json from def_fill_user_data_with_response {json_response}')
        items = json_response['items']

        param_list = user_object.__dict__.keys()

        for param in list(param_list):
            for item in items:
                if item['name'] == param:
                    setattr(user_object, param, item['value'])

        user_oid = json_response['oid']
        setattr(user_object, 'oid', user_oid)


        return user_object


    def get_user_data_by_oid(self, oid):
        url = f'{appUrl}/inrights/api/user/card/{oid}'
        # url = f'http://10.201.48.186:8080/inrights/api/user/card/{oid}'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = None
        json = None

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
        json_response = response.json()

        user_get_by_oid = User()
        self.fill_user_data_from_response(user_get_by_oid, json_response)
        # print(f'Get by oid {user_get_by_oid}')

        return user_get_by_oid

    def compare_user_data(self, created_user, user_get_by_oid):
        assert created_user.__eq__(user_get_by_oid)


# a = UserHelper()
# a.get_user_data_by_oid("1ae49411-38db-4beb-8172-5f9c4969c8de")







