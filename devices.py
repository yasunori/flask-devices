# -*- coding: utf-8 -*-

import re
from flask import _request_ctx_stack as stack
from jinja2 import FileSystemLoader
from collections import OrderedDict


class Devices(object):
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        self.patterns = app.config.get('DEVICES', OrderedDict())

        @app.before_request
        def _template_changer():
            ctx = stack.top
            if ctx is not None and hasattr(ctx, 'request'):
                self.process_request(ctx.request)

    def process_request(self, request):
        user_agent = request.user_agent.string
        for key, val in self.patterns.items():
            if val[0].search(user_agent):
                self.app.jinja_loader = FileSystemLoader(val[1])
                request.DEVICE = key
                break

    def set_patterns(self, patterns=None):
        self.patterns = patterns

    def add_pattern(self, name, pattern, template_folder):
        pattern_complied = re.compile(pattern)
        self.patterns[name] = (pattern_complied, template_folder)

