#-*-coding:utf-8-*-

import tornado.httpserver
import tornado.web
import json
#http://localhost:8000/?greeting='wuchen'

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            print("call LoginHandler success!!!")
            name = self.get_argument('name', 'noname')
            password = self.get_argument('password','nopassword')
            self.write(name + ' login success!'+' pass word is: '+ password)
            print(name + ' login success!'+' pass word is: '+ password)
        except :
            print('get_argument exception...')
    get = post


