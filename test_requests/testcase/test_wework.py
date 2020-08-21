import requests

from test_requests.api.util import Util
from test_requests.api.wework import Wework


class TestWework:
    def test_get_token(self):
        # print(Wework().token())
        # print(Util().token())
        print(Wework().test_get(14000000012))

    def test_create(self):
        Wework().test_creat("maheheheh", "13370146365")

    def test_get(self):
        print(Wework().test_get("maheheheh"))

    def test_update(self):
        print(Wework().test_update("maheheheh", "13370146366"))

    def test_delete(self):
        Wework().test_delete("maheheheh")

    def test_session(self):
        s = requests.session()
        s.params = {"access_token": Util().token()}
        res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=maheheheh")
        print(res.json())
