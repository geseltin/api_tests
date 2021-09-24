from helpers.rest_helper import RestHelper
from helpers.config import appUrl
import random
from helpers.config import parentCompanyOid

class RequestHelper():

    def __init__(self):
        self.rest = RestHelper()
        self.appUrl = appUrl

    def create_request(self, employment_oid):
        url = f'{appUrl}/idm/api/request/submit'
        headers = {'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/json',
                   'WWW-Operation-Context': 'request.newRequest'}
        params = None
        access_oid = self._get_valid_access_for_request(employmentOid=employment_oid)

        json = {"comment":"Request created by API","separate":False,"employments":[employment_oid],
                "accesses":[{"id":access_oid,"type":"STANDARD","contexts":[],"accessType":None}]}

        # Ответ {"violations":null,"requestNumbers":["01.004.261"]}
        response = self.rest.call_request(request_type='POST', url=url, json=json, headers=headers, params=params)
        json_response = response.json()
        print(json_response)
        if 'message' in json_response:
            print(f'[ERROR] Something goes wrong')
            assert False
        else:
            if json_response['requestNumbers'] is not None:
                print('[INFO] Created request Id: ' + str(json_response['requestNumbers'][0]))
                assert True
            else:
                assert False


    def _get_random_access_id_for_employment(self, employmentOid):
        url = f'{appUrl}/idm/api/newrequest/accesses'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = None
        json = {'start': 0, 'limit': 200, 'sort': [{'property': 'name', 'direction': 'ASC'}],
                'filter': [{'value': [''], 'property': 'search'},
                           {'property': 'employmentOids', 'value': [employmentOid]},
                           {'property': 'applicationOids', 'value': []}, {'property': 'ownerCompanyOids', 'value': []},
                           {'property': 'ownerEmpOids', 'value': []}]}

        response = self.rest.call_request(request_type='POST', url=url, json=json, headers=headers, params=params)
        json_response = response.json()
        # print(json_response)

        access_item = json_response['items'][random.randint(0, len(json_response['items']) - 1)]
        # print(access_item['id'])
        # print(access_item)
        return access_item['id']

    def _validate_access(self, accessesOid, employmentOid):
        url = f'{appUrl}/idm/api/request/validate'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = None
        json = {'employments': [employmentOid], 'accesses': [{'id': accessesOid, 'accessType': None, 'contexts': [], 'type': 'STANDART'}]}

        response = self.rest.call_request(request_type='POST', url=url, params=params, headers=headers, json=json)
        json_response = response.json()
        # print(json_response)

        if  len(json_response['items']) == 0:
            print('Validate access - OK')
            return True
        else:
            print('Validate access - FAILED')
            return False

    def _get_valid_access_for_request(self, employmentOid):
        valid_access = None
        attempt_number = 0
        while attempt_number < 100:
            attempt_number += 1
            accessOid = self._get_random_access_id_for_employment(employmentOid=employmentOid)
            if self._validate_access(accessesOid=accessOid, employmentOid=employmentOid) == True:
                valid_access = accessOid
                break

        # print(valid_access)
        return valid_access

    def assign_user_in_request(self, userOid, requestOid):
        url = f'{appUrl}/idm/api/requests/assign-user'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = None
        json = {"requestId": requestOid,
                "requestItemId":0,"userId": userOid,"comment":"","requestType":"CREATE_ROLE_ASSIGNMENTS"}

        response = self.rest.call_request(request_type='POST', url=url, params=params, headers=headers, json=json)
        json_response = response.json()
        print(json_response)

    def get_application_list(self):
        url = f'{appUrl}/idm/api/applications/applications'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = None
        json = {"start":0,"limit":50,"sort":[{"property":"name","direction":"ASC"}],"filter":[{"value":[""],"property":"search"}]}

        response = self.rest.call_request(request_type='POST', url=url, params=params, headers=headers, json=json)
        application_list = response.json()
        #print(application_list['items'])

        return application_list['items']

    def _get_application_publications(self, application_oid):
        url = f'{appUrl}/idm/api/applications/card/{application_oid}/publications'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = {'sort': None}
        json = None

        response = self.rest.call_request(request_type='GET', url=url, params=params, headers=headers, json=json)
        publication_list = response.json()
        return publication_list


    def _publicate_application(self,application_oid, org_structure_oid):
        url = f'{appUrl}/idm/api/applications/card/{application_oid}/publications/create'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = None
        json = {"oids":[org_structure_oid]}

        response = self.rest.call_request(request_type='POST', url=url, params=params, headers=headers, json=json)
        json_response = response.json() # ответ [{"id":"04986cf1-7253-46a1-84c6-52b834c60ff6","path":["API Comp","Австралия","секретариата"],"error":false}]

    def publicate_applications_for_company(self):
        application_list = self.get_application_list()
        for application in application_list:
            publication_list = self._get_application_publications(application_oid=application['id'])
            print(publication_list)
            #todo

    def check_and_publicate_applications_for_position(self, position_oid):
        application_list = self.get_application_list()

        for application in application_list:
            id_list = []
            publication_list = self._get_application_publications(application_oid=application['id'])
            for publication_item in publication_list:
                id_list.append(publication_item['id'])
            if position_oid not in id_list:
                self._publicate_application(application_oid=application['id'], org_structure_oid=position_oid)


            #print(id_list)








a = RequestHelper()
# a._get_random_accesses_id_for_employment(employmentOid='3d9f2cfe-29e0-4fcf-aaec-76d3976b3a55')
# a._validate_accesses(accesses_oid='5ae1e436-db8f-45f6-bb24-9adb296e05f9', employment_oid='66c6ba63-6231-4bf9-80fd-2ea383bc1d6e')
# a._get_valid_access_for_request(employmentOid='3d9f2cfe-29e0-4fcf-aaec-76d3976b3a55')
# a.create_request(employmentOid='3d9f2cfe-29e0-4fcf-aaec-76d3976b3a55')
# a.assign_user_in_request(userOid='00000000-0000-0000-0000-000000000002', requestOid='40f44827-ddc8-4a41-b637-7920cb44b1af')
# a.get_application_list()
# a._get_application_publications(application_oid='c1d9fd17-6e0c-4154-8174-583e6e77bc1e')
# if not []:
#     print('YEAH')
#a.publicate_applications_for_company()
a.check_and_publicate_applications_for_position(position_oid='72c5ce25-543e-4e4a-bda3-56790e8b2c0a')
