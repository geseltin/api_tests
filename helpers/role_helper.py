from helpers.rest_helper import RestHelper
from  helpers.config import appUrl


class RoleHelper:

    def __init__(self):
        self.appUrl = appUrl
        self.rest = RestHelper()

    def create_role(self):
        url = f"{appUrl}inrights/api/roles/card/new"
        headers = {"Accept-Encoding": "gzip, deflate", "Accept-Language": "ru"}
        params = {"id": "INRIGHTS.model.roles.NewRole-1"}

        response = self.rest.call_request(request_type="POST", url=url, json=json, headers=headers, params=params)

    def get_role_data_by_oid(self, oid):
        pass

    def delete_role(self):
        pass