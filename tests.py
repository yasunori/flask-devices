# -*- coding: utf-8 -*-
from nose.tools import ok_, eq_
import flask
from jinja2 import FileSystemLoader
from flask_devices import Devices


app = None
devices = None


class ClientProxy(object):
    def __init__(self, app, user_agent):
        self.app = app
        self.user_agent = user_agent

    def __call__(self, environ, start_response):
        environ['REMOTE_ADDR'] = environ.get('REMOTE_ADDR', '127.0.0.1')
        environ['HTTP_USER_AGENT'] = environ.get('HTTP_USER_AGENT', self.user_agent)
        return self.app(environ, start_response)


def setup():
    global app
    global devices
    app = flask.Flask(__name__)
    devices = Devices(app)


def teardown(self):
    pass


def mobile_test():
    devices.add_pattern('mobile', 'iphone', 'templates/mobile')
    devices.add_pattern('pc', '.*', 'templates/pc')
    app.wsgi_app = ClientProxy(app.wsgi_app, 'iphone')
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.user_agent.string, 'iphone')
        eq_(flask.request.DEVICE, 'mobile')
        eq_(app.jinja_loader.searchpath[0], 'templates/mobile')


def pc_test():
    devices.add_pattern('mobile', 'iphone', 'templates/mobile')
    devices.add_pattern('pc', '.*', 'templates/pc')
    app.wsgi_app = ClientProxy(app.wsgi_app, 'Chrome')
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.user_agent.string, 'Chrome')
        eq_(flask.request.DEVICE, 'pc')
        eq_(app.jinja_loader.searchpath[0], 'templates/pc')
