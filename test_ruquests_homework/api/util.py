import requests


class Util:
    def token(self):
        """
        获取token
        :return:
        """
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww597387adfe2e828e&corpsecret=1aojVo4P_97XeQN0189B8zKr2CilKm2jFsxyESf28rI")
        # print(r.json()["access_token"])
        return r.json()["access_token"]
