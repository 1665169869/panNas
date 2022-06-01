import json
import sys
import requests
import os
import time


class QrcodeSign:
    imgurl = ""
    errno = 0
    sign = ""
    prompt = ""
    response = requests.Response


class BaiDuPan:
    qrcode = {
        "url": "https://passport.baidu.com/v2/api/getqrcode?lp=pc",
        "method": "GET",
    }
    qrlogin = "https://wappass.baidu.com/wp/?qrlogin"
    unicast = {
        "url": "https://passport.baidu.com/channel/unicast",
        "method": "GET"
    }
    qrbdusslogin = {
        "url": "https://passport.baidu.com/v3/login/main/qrbdusslogin",
        "method": "GET"
    }

    def __init__(self):
        self.bduss = ""

    def login(self, r: QrcodeSign):
        data = {
            "cookies": {},
            "Response": requests.Response
        }
        if 200 == r.response.status_code and 0 == r.errno:
            for i in range(10):
                result = self.is_login(r.sign)
                if result:
                    break
            if result is not None and True:
                params = {
                    "v": int(round(time.time() * 1000)),
                    "bduss": self.bduss,
                    "loginVersion": "v4",
                    "qrcode": 1,
                    "tpl": "netdisk",
                    "apiver": "v3",
                    "tt": int(round(time.time() * 1000))
                }
                res = requests.request(self.qrbdusslogin['method'], self.qrbdusslogin['url'], params=params)
                if res.status_code == 200:
                    data['cookies'] = res.cookies
                    data['Response'] = res
        return data

    def logout(self):
        ...

    def getSign(self):
        r = requests.request(self.qrcode['method'], self.qrcode['url'])
        result = QrcodeSign
        result.response = r
        if 200 == r.status_code:
            res = r.json()
            result.imgurl = "https://" + res['imgurl']
            result.errno = res['errno']
            result.sign = res['sign']
            result.prompt = res['prompt']
        return result

    def is_login(self, sign: str, result=False):
        """
        该接口每次请求会很慢很慢
        """
        params = {
            "channel_id": sign,
            "tpl": "netdisk",
            "apiver": "v3",
            "tt": int(round(time.time() * 1000)),
            "_": int(round(time.time() * 1000))
        }
        r = requests.request(self.unicast['method'], self.unicast['url'], params=params)
        if 200 == r.status_code and result == True:
            return r.json()
        if 200 == r.status_code and 0 == r.json()['errno'] and 0 == json.dumps(r.json()['channel_v'])['status']:
            self.bduss = json.dumps(r.json()['channel_v'])['v']
            return True
        return False

    def getQrcode(self, sign):
        qrcode = bytes
        r = requests.get(f"https://passport.baidu.com/v2/api/qrcode?sign={sign}&lp=pc")
        if r.status_code == 200:
            qrcode = r.content
            return qrcode


class PanNas:
    def __init__(self):
        self.path = os.path.split(os.path.realpath(__file__))[0] + "/panNasFile/"
        self.mkdir(self.path)

    @staticmethod
    def mkdir(path) -> None:
        os.makedirs(path, mode=777, exist_ok=True)


if __name__ == "__main__":
    ...
