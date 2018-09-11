# -*- coding: utf-8 -*-
from nose.tools import ok_, eq_, with_setup
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
        #environ['HTTP_USER_AGENT'] = environ.get('HTTP_USER_AGENT', self.user_agent)
        environ['HTTP_USER_AGENT'] = self.user_agent
        return self.app(environ, start_response)


def setup():
    pass


def teardown():
    pass


def f_setup():
    global app
    global devices
    app = flask.Flask(__name__)
    devices = Devices(app)


def f_setup_full():
    global app
    global devices
    app = flask.Flask(__name__)
    devices = Devices(app)
    devices.add_pattern('sp', 'iPhone|iPod|Android.*Mobile|Windows.*Phone|dream|blackberry|CUPCAKE|webOS|incognito|webmate', 'templates/sp')
    devices.add_pattern('pc', '.*', 'templates/pc')



@with_setup(f_setup)
def mobile_test():
    devices.add_pattern('mobile', 'iphone', 'templates/mobile')
    devices.add_pattern('pc', '.*', 'templates/pc')
    app.wsgi_app = ClientProxy(app.wsgi_app, 'iphone')
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.user_agent.string, 'iphone')
        eq_(flask.request.DEVICE, 'mobile')
        eq_(app.jinja_loader.searchpath[0], 'templates/mobile')


@with_setup(f_setup)
def pc_test():
    devices.add_pattern('mobile', 'iphone', 'templates/mobile')
    devices.add_pattern('pc', '.*', 'templates/pc')
    app.wsgi_app = ClientProxy(app.wsgi_app, 'Chrome')
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.user_agent.string, 'Chrome')
        eq_(flask.request.DEVICE, 'pc')
        eq_(app.jinja_loader.searchpath[0], 'templates/pc')


@with_setup(f_setup)
def order_test():
    devices.add_pattern('pc', '.*', 'templates/pc')
    devices.add_pattern('mobile', 'iphone', 'templates/mobile')
    app.wsgi_app = ClientProxy(app.wsgi_app, 'iphone')
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.user_agent.string, 'iphone')
        eq_(flask.request.DEVICE, 'pc')
        eq_(app.jinja_loader.searchpath[0], 'templates/pc')


@with_setup(f_setup_full)
def user_agent_1_test():
    user_agent = ('sp', 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25')
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_2_test():
    user_agent = ('sp', 'Mozilla/5.0 (iPod; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3')
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_3_test():
    user_agent = ('sp', 'Mozilla/5.0 (Linux; U; Android 4.1.1; ja-jp; HTL21 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_4_test():
    user_agent = ('pc', 'Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; SC-01D Build/MASTER) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13')  # tablet
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_5_test():
    user_agent = ('pc', 'Mozilla/5.0 (Linux; U; Android 4.1.2; ja-jp; dtab01 Build/HuaweiMediaPad) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30')  # tablet
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_6_test():
    user_agent = ('pc', 'Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25')  # ipad
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_7_test():
    user_agent = ('sp', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; FujitsuToshibaMobileCommun; IS12T; KDDI)')
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_8_test():
    user_agent = ('sp', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; ja) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.74 Mobile Safari/534.11+')
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_9_test():
    user_agent = ('sp', 'Opera/9.80 (BlackBerry; Opera Mini/6.1.25376/26.958; U; en) Presto/2.8.119 Version/10.54')
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])


@with_setup(f_setup_full)
def user_agent_10_test():
    user_agent = ('pc', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)')
    app.wsgi_app = ClientProxy(app.wsgi_app, user_agent[1])
    with app.test_client() as c:
        c.get('/')
        eq_(flask.request.DEVICE, user_agent[0])
        eq_(app.jinja_loader.searchpath[0], 'templates/' + user_agent[0])




