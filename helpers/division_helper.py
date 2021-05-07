from helpers.rest_helper import RestHelper


class OrgHelper:

    def __init__(self):
        self.rest = RestHelper()

    def create_companyType(self):
        url = "http://10.201.48.186:8080/inrights/api/companies/new"
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"sort": ""}


        json = {"fullName": "Api test", "shortName": "Api test"}

        response = self.rest.call_request(request_type="POST", url=url, json=json, headers=headers, params=params)

        print(response)

    def get_division_by_oid(self, division, oid):




