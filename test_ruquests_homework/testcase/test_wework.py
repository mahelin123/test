from test_ruquests_homework.api.wework import Wework


class TestWework:

    def test_create(self):
        print(Wework().creat("活动部门", "001"))

    def test_get(self):
        print(Wework().get("001"))

    def test_update(self):
        print(Wework().update("001", "哈哈部门"))

    def test_delete(self):
        print(Wework().delete("001"))
