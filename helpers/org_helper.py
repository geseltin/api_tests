import random

from helpers.rest_helper import RestHelper
from model.company import Company
from helpers.config import appUrl
from model.division import Division
from model.position import Position
from helpers.config import parentCompanyOid
from random import choice

class OrgHelper:

    def __init__(self):
        self.rest = RestHelper()
        self.appUrl = appUrl

    def create_company_type(self, initial_company, parent_company_oid=parentCompanyOid):
        url = f"{appUrl}/idm/api/companies/card/new"
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"sort": ""}

        json = initial_company.return_company_data_as_json()
        # parent_company_value = self._generate_company_parent_value(parent_company_oid=parentCompanyOid)
        json.update({'parentCompanyRef': parent_company_oid})

        response = self.rest.call_request(request_type="POST", url=url, json=json, headers=headers, params=params)
        json_response = response.json()
        #
        self.fill_company_data_from_response(initial_company, json_response)
        #
        setattr(initial_company, 'oid', initial_company.oid)
        print(initial_company)
        #
        return initial_company

    def get_company_by_oid(self, company_oid):
        url=f'{appUrl}/idm/api/companies/card/{company_oid}'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"sort": ""}
        json=None
        company_got_by_oid = Company()

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
        json_response = response.json()

        self.fill_company_data_from_response(company_object=company_got_by_oid, json_response=json_response)
        # print(company_got_by_oid)
        return company_got_by_oid

    def fill_company_data_from_response(self, company_object, json_response):
        items = json_response['attributes']
        param_list = company_object.__dict__.keys()

        for param in list(param_list):
            for item in items:
                if item['name'] == param:
                    setattr(company_object, param, item['value'])

        company_oid = json_response['oid']
        setattr(company_object, 'oid', company_oid)
        return company_object

    def _generate_company_parent_value(self, parent_company_oid):
        parent_company = self.get_company_by_oid(company_oid=parent_company_oid)
        parent_company_value = {}
        parent_company_value.update({'id': parent_company.oid, 'name': parent_company.shortName, 'userId': None})
        print(parent_company_value)

    def compare_company_data(self, created_company, company_get_by_oid):
        if created_company.__eq__(company_get_by_oid) == True:
            assert True
            print(f'[INFO] Created company with oid: {created_company.oid} and fullname: {created_company.fullName}')
        else:
            print(f'[ERROR] EXPECTED: {created_company}, BUT GOT: {company_get_by_oid}')
            assert False

    def create_division(self, initial_division, parent_id):
        url = f'{appUrl}/idm/api/division/card/new'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"sort": ""}
        json = None

        initial_division_object = initial_division.return_division_data_as_json()
        # division_json = initial_division_object.return_division_data_as_json()
        parent_orgs_object = self.generate_parent_org_object(parentId=parent_id)
        initial_division_object.update({'parentOrgs': parent_orgs_object})
        # print(division_json)
        json = initial_division_object

        response = self.rest.call_request(request_type="POST", url=url, json=json, headers=headers, params=params)
        json_response = response.json()
        # initial_division_object = self.fill_division_data_from_response(division_object=initial_division_object, json_response=json_response)
        created_division = Division()
        self.fill_division_data_from_response(created_division, json_response)
        setattr(initial_division, 'oid', created_division.oid)
        assert initial_division.__eq__(created_division)

        #print(initial_division)
        print(created_division)

        return created_division


    def fill_division_data_from_response(self, division_object, json_response):
        items = json_response['attributes']
        param_list = division_object.__dict__.keys()

        for param in list(param_list):
            for item in items:
                if item['name'] == param:
                    setattr(division_object, param, item['value'])

        division_oid = json_response['oid']
        setattr(division_object, 'oid', division_oid)
        return division_object

    def get_division_by_oid(self, division_oid):
        url = f'{appUrl}/idm/api/division/card/{division_oid}'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"sort": ""}
        json = None
        division_got_by_oid = Division()

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
        json_response = response.json()

        self.fill_division_data_from_response(division_object=division_got_by_oid, json_response=json_response)
        # print(division_got_by_oid)
        return division_got_by_oid

    def compare_division_data(self, created_division, division_get_by_oid):
        if created_division.__eq__(division_get_by_oid) == True:
            assert True
            print(f'[INFO] Created division with oid: {created_division.oid} and fullname: {created_division.fullName}')
        else:
            print(f'[ERROR] EXPECTED: {created_division}, BUT GOT: {division_get_by_oid}')
            assert False


    def generate_parent_org_object(self, parentId):
        parent_orgs_object = {}
        url = f'{appUrl}/idm/api/division/card/{parentId}'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"sort": ""}
        json = None

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
        json_reponse = response.json()
        if response.status_code == 200:
            division_object = Division()
            parent_division_object_filled = self.fill_division_data_from_response(division_object=division_object,
                                                                           json_response=json_reponse)
            parent_orgs = parent_division_object_filled.parentOrgs
            parent_orgs_object.update({'id': parentId, 'ids': parent_orgs['ids'] + [parent_division_object_filled.oid],
                                       'name': parent_orgs['name'] + [parent_division_object_filled.shortName],
                                       'paths': parent_orgs['name'] + [parent_division_object_filled.shortName],
                                       'type': 'org'})
            # print(parent_orgs_object)
            return parent_orgs_object

        elif response.status_code == 500:
            parent_company_filled = self.get_company_by_oid(company_oid=parentId)
            # print(parent_company_filled)
            parent_orgs = parent_company_filled.parentCompanyRef
            parent_orgs_object.update({'id': parentId, 'ids': [parent_orgs['id']] + [parent_company_filled.oid],
                                'name': [parent_orgs['name']] + [parent_company_filled.shortName],
                                'paths': [parent_orgs['name']] + [parent_company_filled.shortName] ,'type': 'org'})
            # print(parent_orgs_object)
            return parent_orgs_object
        else:
            print(f'Что то пошло не так, код ответа: {response.status_code}')

    def make_position_path(self, parentId):
        clientId = 'root/'
        parent_division = self.get_division_by_oid(division_oid=parentId)
        parent_orgs_division = parent_division.parentOrgs
        parent_ids = parent_orgs_division['ids']

        for id in parent_ids:
            clientId += f'{id}/'

        clientId += f'{parentId}/'

        return clientId

    def create_position(self, parent_division_oid):
        url = f'{appUrl}/idm/api/catalog/entry/'
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {'search':'', 'countType': 'all', "sort": ""}

        initial_position_object = Position()
        position_json = initial_position_object.return_position_data_as_json()
        clientId = self.make_position_path(parentId=parent_division_oid)
        position_json.update({'clientId': clientId, 'parentId': parent_division_oid})
        print(position_json)

        response = self.rest.call_request(request_type="POST", url=url, json=position_json, headers=headers, params=params)
        json_response = response.json()
        print(json_response)
        created_position = Position()
        self.fill_position_data_from_response(created_position, json_response)
        setattr(initial_position_object, 'id', created_position.id)
        assert initial_position_object.__eq__(created_position)

        return created_position

    def delete_position(self, position_id):
        url = f'{appUrl}/idm/api/catalog/entry/{position_id}'
        headers = {'WWW-Operation-Context': 'orgStruct', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'ru'}
        params = {}
        json = {'id': position_id, 'parentId': None, 'type': 'position'}

        response = self.rest.call_request(request_type="DELETE", url=url, json=json, headers=headers, params=params)

        if response.status_code == 500:
            json_response = response.json()
            print(json_response)
            assert False
        else:
            print(response.status_code)
            assert True

    def get_children_by_parent_node_oid(self, parent_oid=None, child_oid=None):
        url = f'{appUrl}/idm/api/catalog/entry/{parent_oid}'
        headers = {'WWW-Operation-Context': 'orgStruct', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'ru'}
        params = {'search': None, 'countType': 'all', 'sort': None, 'node': f'root/{parent_oid}'}
        json = None

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
        json_response = response.json()
        print(json_response)

        children_object = None
        for children in json_response['children']:
            if children['id'] == child_oid:
                children_object = children

                break
        if children_object == None:
            print(f'[ERROR] Cant get children with oid {child_oid} in node with oid {parent_oid}')

        children_got_by_oid = Position()
        self.fill_position_data_from_response(position_object=children_got_by_oid, json_response=children_object)
        print(children_got_by_oid)
        return children_got_by_oid

    def fill_position_data_from_response(self, position_object, json_response):

        param_list = position_object.__dict__.keys()
        for param in list(param_list):
            for json_key in json_response.keys():

                if json_key == param:
                    setattr(position_object, param, json_response[json_key])

        position_oid = json_response['id']
        setattr(position_object, 'oid', position_oid)
        return position_object

    def compare_position_data(self, created_position=None, position_get_by_oid=None):
        if created_position.__eq__(position_get_by_oid) == True:
            assert True
            print(f'[INFO] Created position with oid: {created_position.id} and fullname: {created_position.name}')
        else:
            print(f'[ERROR] Expected: {created_position}, but got: {position_get_by_oid}')
            assert False

    def _get_all_children_for_node(self, node_oid=parentCompanyOid):
        url = f'{appUrl}/idm/api/catalog/entry/{node_oid}'
        headers = {'WWW-Operation-Context': 'orgStruct', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'ru'}
        params = {'search': None, 'countType': 'all', 'sort': None, 'node': f'root/{node_oid}'}
        json = None

        response = self.rest.call_request(request_type="GET", url=url, json=json, headers=headers, params=params)
        children_list = response.json()
        #print(children_list['children'])
        return children_list['children']

    def _find_positions_in_org_node(self, node_oid, position_list=[]):

        node_objects = self._get_all_children_for_node(node_oid=node_oid)

        for node_object in node_objects:
            if node_object['type'] == 'position':
                position_list.append(node_object['id'])
                # print(position_list)
            else:
                self._find_positions_in_org_node(node_oid=node_object['id'])

        return position_list

    def _find_random_position_in_org_structure(self):
        # Проблема: если в орге нет ни одной должности random падает в ошибку
        # Решено обработкой исключения, если должностей нет возвращает False
        position_list = []
        node_objects = self._get_all_children_for_node(node_oid=parentCompanyOid)

        for node_object in node_objects:
            if node_object['type'] == 'position':
                position_list.append(node_object['id'])
            else:
                self._find_position_in_org_node(node_oid=node_object['id'], position_list=position_list)
        try:
            return random.choice(position_list)
        except IndexError:
            return False

    def _create_position_object_for_user(self, parent_division_oid, position_oid):
        position = {}
        path = 'root/'
        paths = []
        name = []
        ids = []
        parent_division = self.get_division_by_oid(division_oid=parent_division_oid)
        parent_orgs_division = parent_division.parentOrgs
        parent_ids = parent_orgs_division[0]['ids']
        parent_names = parent_orgs_division[0]['name']

        for id in parent_ids:
            path += f'{id}/'
            ids.append(id)

        path += f'{parent_division_oid}/{position_oid}'
        ids.append(parent_division_oid)
        ids.append(position_oid)

        for item in parent_names:
            name.append(item)
            paths.append(item)

        name.append(parent_division.shortName)
        paths.append(parent_division.shortName)

        parent_divison_children = self._get_all_children_for_node(node_oid=parent_division_oid)

        for child in parent_divison_children:
            if child['id'] == position_oid:
                name.append(child['name'])
                paths.append(child['name'])

        position.update({'id': position_oid, 'ids': ids , 'name': name, 'path': path, 'paths': paths, 'type': 'position'})

        # print(position)
        return position

    def _find_parent_for_position(self, position_oid, parent_oid = parentCompanyOid):
        # Проблема: отрабатывает 3 минуты на 186 стенде

        node_objects = self._get_all_children_for_node(node_oid=parent_oid)

        for node_object in node_objects:
            parent_oid = None
            parent_oid = node_object['id']
            #print(parent_oid)
            children_list = self._get_all_children_for_node(node_oid=parent_oid)
            for child in children_list:
                # print(child)
                if child['id'] == position_oid:
                    print(parent_oid)
                    return parent_oid
                    break
                else:
                    self._find_parent_for_position(position_oid=position_oid, parent_oid=parent_oid)














a = OrgHelper()
# # # a.get_company_by_oid(company_oid='876412c3-4fab-4c12-b42f-7a40a1b38267')
division = Division()
# company = Company()
# position = Position()
# new_pos = Position()
# # a.generate_parent_org_object(parentId='efb6f40a-c391-44e2-aeb0-6675cb321151')
# #a.generate_parent_org_object(parentId='58fe98de-27cd-4205-8df8-d1071c4eb2bf')
#a.create_division(division, parent_id='3252e137-98db-47a5-bae7-6cf947ddfdaf')
# # a.make_position_path(parentId='b5a1f64f-d75c-4230-bd51-672bfc01c489')
# # a.create_position(parentId='b5a1f64f-d75c-4230-bd51-672bfc01c489')
# a.delete_position(positionId='f1b823ec-4442-4d56-baa9-c39152e5c404')
#a.create_company_type(initial_company=company, parent_company_oid='876412c3-4fab-4c12-b42f-7a40a1b38267')
#a._generate_company_parent_value(parent_company_oid='876412c3-4fab-4c12-b42f-7a40a1b38267')
# json_response = a.get_children_by_parent_node_oid(parent_oid='3252e137-98db-47a5-bae7-6cf947ddfdaf', child_oid='585060c4-267f-40cd-99bc-f0b7f8668c0b')
# position_object = a.fill_position_data_from_response(position_object=position, json_response=json_response)
# print(position_object)
# a.compare_position_data(created_position=position_object, position_get_by_oid=position_object)
# print(a._get_all_children_for_node(node_oid='876412c3-4fab-4c12-b42f-7a40a1b38267'))
# b = a._find_positions_in_org_node(node_oid='876412c3-4fab-4c12-b42f-7a40a1b38267')
# print(b)
#print(a._find_random_position_in_org_structure())
# position = a._create_position_object_for_user(parent_division_oid='61c5664b-b27a-4ed1-958f-3db08c1e62e2', position_oid='9afd1807-d2c0-4ae9-a3cb-eb333a25f404')
# print(position)
# a._find_random_position_and_parent_in_org_structure()
#a._find_parent_for_position(position_oid='568649f6-f4ab-4e9f-be7f-a502693f1dd7')


