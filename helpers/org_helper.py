from helpers.rest_helper import RestHelper


class OrgHelper:

    def create_companyType(self):
        url = "http://10.201.48.186:8080/inrights/api/companies/new"
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"sort": ""}

        rest_helper = RestHelper()
        json = {"fullName": "Api test", "shortName": "Api test"}

        response = rest_helper.call_request(request_type="POST", url=url, json=json, headers=headers, params=params)

        print(response)




