from helpers.rest_helper import RestHelper
import random
from model.user import User
from helpers.config import appUrl
from model.employment import Employment
from model.account import Account
from datetime import date
from datetime import timedelta


class UserHelper:
    def __init__(self):
        self.rest = RestHelper()
        self.appUrl = appUrl


    def create_user(self, user):
        url = f'{appUrl}/idm/api/user/card/new'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"id": "users.NewUser-1"}

        json = user.return_user_data_as_json()

        response = self.rest.call_request(request_type="PUT", url=url, json=json, headers=headers, params=params)
        json_response = response.json()

        created_user = User()

        self.fill_user_data_from_response(created_user, json_response)
        # print(created_user)
        # print(user)

        assert user.__eq__(created_user)
        setattr(user, 'oid', created_user.oid)
        #print(created_user)
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
        url = f'{appUrl}/idm/api/user/card/{oid}'
        # url = f'http://10.201.48.186:8080/idm/api/user/card/{oid}'
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
        if created_user.__eq__(user_get_by_oid) == True:
            assert True
            print(f'Created user with oid: {created_user.oid} and fullname: {created_user.lastName} '
                  f'{created_user.firstName} {created_user.additionalName}')
        else:
            print(f'EXPECTED: {created_user}, BUT GOT: {user_get_by_oid}')
            assert False


    def get_employment_by_user_oid(self, oid):
        url=f'{appUrl}/idm/api/user/{oid}/employments'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"sort": None}
        json = None

        employment_object = Employment()

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
        json_response = response.json()

        self.fill_employment_from_response(employment_object=employment_object, json_response=json_response)
        return employment_object


    def fill_employment_from_response(self, employment_object, json_response):

        param_list = employment_object.__dict__.keys()
        attributes_list = json_response['items'][0]['card']['attributes']
        # print(attributes_list)

        for param in list(param_list):
            for attribute in attributes_list:
                if attribute['name'] == param:
                    setattr(employment_object, param, attribute['value'])

        setattr(employment_object, 'id', json_response['items'][0]['card']['oid'])


        return employment_object

    def get_accounts_by_user_oid(self, user_oid):
        url = f'{appUrl}/idm/api/user/{user_oid}/accounts'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = None
        json = None

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
        json_response = response.json()

        account = Account()
        param_list = account.__dict__.keys()
        print(param_list)
        items_list = json_response['items']
        for item in items_list:
            print(item)
            if item.get('resourceName') == 'AD - gk.rosatom.local':
                for param in list(param_list):
                    setattr(account, param, item.get(param))


        return account

    def check_account_entitlements(self, account):
        if "Test_S" in account.entitlements:
            print("Успех")
        else:
            assert False

    def change_user_hr_status(self, user_oid, target_hr_status):
        url = f"{appUrl}/idm/api/user/{user_oid}/employment"
        headers = {"Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "ru",
                   "WWW-Operation-Context": "users.card:employments",
                   "Accept": "application/json;charset=UTF-8"}
        params = None
        employment = self.get_employment_by_user_oid(user_oid)

        if target_hr_status == 'active':
            today = date.today()
            dateInThePast = (today - timedelta(days=-1)).isoformat()
            futureDate = (today + timedelta(days=365)).isoformat()

            employment_data_json = employment.return_employment_data_as_json()
            employment_data_json.update(
                {"vacationType": None, "vacstart": None, "vacend": None, "worstart": dateInThePast,
                 "workend": futureDate})

            response = self.rest.call_request(request_type="POST", url=url, json=employment_data_json, headers=headers,
                                              params=params)
            print(response)

        elif target_hr_status == 'vacation':
            today_date = date.today()
            today = today_date.isoformat()
            tomorrow = (today_date + timedelta(days=2)).isoformat()

            employment_data_json = employment.return_employment_data_as_json()
            position_object = employment.position
            position_object.update({'path': position_object['name'], 'type': 'position'})
            employment_data_json.update(
                {"position": position_object, 'vacstart': today, 'vacend': tomorrow, 'vacationType': 'vacation'})

            response = self.rest.call_request(request_type="POST", url=url, json=employment_data_json, headers=headers,
                                              params=params)
            print(response)

        elif target_hr_status == 'maternityleave':
            today_date = date.today()
            today = today_date.isoformat()
            tomorrow = (today_date + timedelta(days=2)).isoformat()

            employment_data_json = employment.return_employment_data_as_json()
            position_object = employment.position
            position_object.update({'path': position_object['name'], 'type': 'position'})
            employment_data_json.update(
                {"position": position_object, 'vacstart': today, 'vacend': tomorrow, 'vacationType': 'leave'})

            response = self.rest.call_request(request_type="POST", url=url, json=employment_data_json, headers=headers,
                                              params=params)
            print(response)
        elif target_hr_status == 'fired':
            today_date = date.today()
            today = today_date.isoformat()

            employment_data_json = employment.return_employment_data_as_json()
            position_object = employment.position
            position_object.update({'path': position_object['name'], 'type': 'position'})
            employment_data_json.update(
                {"position": position_object, 'workend': today})

            response = self.rest.call_request(request_type="POST", url=url, json=employment_data_json, headers=headers,
                                              params=params)
            print(response)
        else:
            print('hr_status is incorrect')
            assert False

        self.check_user_hr_status(user_oid=user_oid, status=target_hr_status)


    def send_user_on_vacation(self, user_oid):
        url=f"{appUrl}/idm/api/user/{user_oid}/employment"
        headers = {"Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "ru",
                   "WWW-Operation-Context": "users.card:employments",
                   "Accept": "application/json;charset=UTF-8"}
        params = None
        today_date = date.today()
        today = today_date.isoformat()
        tomorrow = (today_date + timedelta(days=2)).isoformat()

        employment = self.get_employment_by_user_oid(user_oid)

        employment_data_json = employment.return_employment_data_as_json()
        position_object = employment.position
        position_object.update({'path': position_object['name'], 'type': 'position'})
        employment_data_json.update({"position":position_object, 'vacstart': today, 'vacend': tomorrow, 'vacationType': 'vacation'})

        #print(employment_data_json)

        response = self.rest.call_request(request_type="POST", url=url, json=employment_data_json, headers=headers,
                                           params=params)
        print(response)
        self.check_user_hr_status(user_oid=user_oid, status ='vacation')


    def make_user_hrstatus_active(self, user_oid):
        url = f"{appUrl}/idm/api/user/{user_oid}/employment"
        headers = {"Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "ru",
                   "WWW-Operation-Context": "users.card:employments"}
        params = None

        today = date.today()
        dateInThePast = (today - timedelta(days=-1)).isoformat()
        futureDate = (today + timedelta(days=365)).isoformat()

        employment = self.get_employment_by_user_oid(user_oid)
        employment_data_json = employment.return_employment_data_as_json()
        employment_data_json.update({"vacationType":None,"vacstart":None,"vacend":None, "worstart": dateInThePast, "workend": futureDate})


        response = self.rest.call_request(request_type="POST", url=url, json=employment_data_json, headers=headers,
                                          params=params)
        print(response)
        self.check_user_hr_status(user_oid=user_oid, status='active')

    def fire_user(self, user_oid):
        url = f"{appUrl}/idm/api/user/{user_oid}/employment"
        headers = {"Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "ru",
                   "WWW-Operation-Context": "users.card:employments"}
        params = None

        today_date = date.today()
        today = today_date.isoformat()

    def check_user_hr_status(self, user_oid, status):
        employment = self.get_employment_by_user_oid(user_oid)
        employment_data_json = employment.return_employment_data_as_json()
        if employment_data_json['hrStatus'] == status:
            assert True
        else:
            print(f'User current hrStatus is: {employment_data_json["hrStatus"]}')
            assert False





# user = User()
# a = UserHelper()
# a.create_user(user=user)
# employment = a.get_employment_by_user_oid(oid ="f51c558d-2383-4d0d-bb11-645432c85b6c")
# print(employment)
#account = a.get_accounts_by_user_oid(user_oid="fb922968-39b7-4df1-8bc7-4dcb4a3c00cd")
#a.check_account_entitlements(account=account)
# a.send_user_on_vacation(user_oid="f51c558d-2383-4d0d-bb11-645432c85b6c")
# a.make_user_hrstatus_active(user_oid="f51c558d-2383-4d0d-bb11-645432c85b6c")
# a.change_user_hr_status(user_oid='f51c558d-2383-4d0d-bb11-645432c85b6c', target_hr_status='vacation')
# a.change_user_hr_status(user_oid='f51c558d-2383-4d0d-bb11-645432c85b6c', target_hr_status='active')
# a.change_user_hr_status(user_oid='f51c558d-2383-4d0d-bb11-645432c85b6c', target_hr_status='maternityleave')
# a.change_user_hr_status(user_oid='f51c558d-2383-4d0d-bb11-645432c85b6c', target_hr_status='active')
# a.change_user_hr_status(user_oid='f51c558d-2383-4d0d-bb11-645432c85b6c', target_hr_status='fired')
# c = {"first": 1, "second":2}
# print(c)
# c.update({"first": 999, "second":999})
# print(c)
#
# today = date.today()
# d1 = today.strftime("%d-%m-%Y")
# print(d1)
# print(today)
# d2 = today + timedelta(days=1)
# print(d2)









