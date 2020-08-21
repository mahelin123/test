import yaml

from test_requests.api.util import Util
from test_ruquests_homework.api.baseapi import BaseApi


class Wework(BaseApi):
    def __init__(self):
        self.token = Util().token()
        self.params["token"] = self.token

        with open("../api/wework.yaml", encoding="utf-8") as f:
            self.data = yaml.load(f)

    def creat(self, tagname, tagid):
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        return self.send(self.data["creat"])

    def get(self, tagid):
        self.params["tagid"] = tagid
        return self.send(self.data["get"])

    def update(self, tagid, tagname):
        self.params["tagid"] = tagid
        self.params["tagname"] = tagname
        return self.send(self.data["update"])

    def delete(self, tagid):
        self.params["tagid"] = tagid
        return self.send(self.data["delete"])
