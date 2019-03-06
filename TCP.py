
import requests
import unittest


class MyTest(unittest.TestCase):
    def test_login(self):
        payload = {'user.username': 'admin', 'user.password': '123456'}
        r = requests.post("http://123.57.50.28/SC/login!login.action", data=payload)
        print(r.status_code)
        print(r.text)


class AddEventTest(unittest.TestCase)
    def setUp(self):
        self.base_url = "http://demo.yinmei.me/sys/printbill"


if __name__ == '__main__':
    unittest.main()


