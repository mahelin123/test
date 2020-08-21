import yaml

from test_requests.api.baseapi import BaseApi
from test_requests.api.util import Util


class Wework(BaseApi):
    def __init__(self):
        self.token = Util().token()
        self.params["token"] = self.token

        with open("../api/wework.yaml", encoding="utf-8") as f:
            self.data = yaml.load(f)

    def test_creat(self, userid, mobile, name="柯南", department=None):
        if department is None:
            department = "1"
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department
        return self.send(self.data["creat"])

    def test_get(self, userid):
        self.params["userid"] = userid
        return self.send(self.data["get"])

    def test_update(self, userid, name):
        self.params["userid"] = userid
        self.params["name"] = name
        return self.send(self.data["update"])

    def test_delete(self, userid):
        self.params["userid"] = userid
        return self.send(self.data["delete"])
