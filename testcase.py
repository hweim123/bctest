# coding:utf-8
"""
基本的自动化测试脚本
"""
__author__ = 'huang'

import unittest
import random

class IndexPageTest(TestCase):
    '''测试index登录首页'''

    def test_root_url_resolves_to_index_page(self):
        '''测试根url是否解析到登录页'''
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_correct_html(self):
        '''调试调用index函数返回的页与模板加载的index2.html是否相等'''
        request = HttpRequest()
        response = index(request)
        excepted_html = render_to_string('index2.html', request=request)
        self.assertEqual(response.content.decode(), excepted_html)
        # print('response.content.decode():\n', response.content.decode())
        # print('excepted_html\n', excepted_html)


class LoginActionTest(TestCase):
    '''测试登录动作'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_login_action_username_password_null(self):
        '''用户名密码为空'''
        c = Client()
        response = c.post('/login_action/', {'useername': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password null!", response.content)

    def test_login_action_username_password_error(self):
        '''用户密码错误'''
        test_data = {'username': 'abc', 'password': '123'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_success(self):
        '''登录成功'''
        test_data = {'username': 'admin', 'password': 'admin123456'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)


class EventManageTest(TestCase):
    # 发布会管理

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(name='xiaomi5', limit=2000, address='beijing',
                             status=1, start_time='2017-8-10 12:30:00')
        self.login_user = {'username': 'admin', 'password': 'admin123456'}

    def test_event_manage_success(self):
        response1 = self.client.post('/login_action/', data=self.login_user)
        response2 = self.client.post('/event_manage/')
        self.assertEqual(response1.status_code, 302)
        self.assertIn(b"xiaomi5", response2.content)
        self.assertIn(b"beijing", response2.content)

    def test_event_manage_search_success(self):
        ''' 测试发布会搜索 '''
        response1 = self.client.post('/login_action/', data=self.login_user)
        response2 = self.client.post('/search_name/', {'name': 'xiaomi5'})
        self.assertEqual(response1.status_code, 302)
        self.assertIn(b"xiaomi5", response2.content)
        self.assertIn(b"beijing", response2.content)


class GuestManageTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=15, name='xiaomi5', limit=2000, address='beijing',
                             status=1, start_time='2017-8-10 12:30:00')
        Guest.objects.create(realname='allen', phone=18611001100, email='allen@mail.com', sign=0,
                             event_id=15)
        self.login_user = {'username': 'admin', 'password': 'admin123456'}

    def test_guest_manage_success(self):
        '''测试嘉宾信息：allen'''
        response1 = self.client.post('/login_action/', data=self.login_user)
        response2 = self.client.post('/guest_manage/')
        self.assertEqual(response1.status_code, 302)
        self.assertIn(b"allen", response2.content)
        self.assertIn(b"18611001100", response2.content)

    def test_guest_manage_search_success(self):
        response1 = self.client.post('/login_action/', data=self.login_user)
        response2 = self.client.post('/search_phone/', {'phone': '18611001100'})
        self.assertEqual(response1.status_code, 302)
        self.assertIn(b"allen", response2.content)
        self.assertIn(b"18611001100", response2.content)
class IndexPageTest(unittest.TestCase):
    def setUp(self):
        print('start to testing...')

    def test_login_action_username_password_null(self):
        """
        用户密码为空
        :return:
        """
    c = Client()


    def tearDown(self):
        print('testing end.')


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def runTest(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


if __name__ == '__main__':
    unittest.main()

