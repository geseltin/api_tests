import requests
import random



class RestHelper:



    def call_request(self, request_type=None, url=None, json=None,
                     headers=None, params=None, login="Administrator", password="5ecr3t"):

        auth_url = "http://10.201.48.186:8080/idm/api/auth/login"
        payload = {"login": login, "password": password}

        current_session = requests.session()

        response = current_session.post(auth_url, params=payload)
        if response.status_code == 200 and response.headers.get('authenticationLevel') == "FULLY_AUTHENTICATED":
            assert True
        else:
            print(f'FAILED: Requests status = {response.status_code}')
            assert False

        if request_type == "GET":
            return current_session.get(url, json=json, headers=headers, params=params)
        elif request_type == "POST":
            return current_session.post(url, json=json, headers=headers, params=params)
        elif request_type == "PUT":
            return current_session.put(url, json=json, headers=headers, params=params)
        elif request_type == "DELETE":
            return current_session.delete(url, json=json, headers=headers, params=params)


