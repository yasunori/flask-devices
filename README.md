Flask-Devices
=============

Switch Flask's template folder automatically by request's User Agent(iPhone, iPad, Android, other mobile device, PC, and so on)

[![Build Status](https://travis-ci.org/yasunori/flask-devices.png?branch=master)](https://travis-ci.org/yasunori/flask-devices)


## Install
```
pip install Flask-Devices
```

## Usage
```
devices = Devices(app)
# device.add_pattern(device_group_name, pattern, template_folder)
devices.add_pattern('mobile', 'iPhone|iPod|Android.*Mobile|Windows.*Phone|dream|blackberry|CUPCAKE|webOS|incognito|webmate', 'templates/sp')
devices.add_pattern('tablet', 'iPad|Android', 'templates/pc')
devices.add_pattern('hoge', 'hoge', 'templates/hoge')
devices.add_pattern('pc', '.*', 'templates/pc')
```
Then, template folder is changed automatically by User Agent.

## Other
Get device group name of current request
```view.py
@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.DEVICE) # mobile, tablet, hoge, pc
    if request.DEVICE == 'pc':
        # pc
    elif request.DEVICE == 'tablet':
        # tablet
```

```example.html
{% if request.DEVICE == 'mobile' %}<strong>I'm a mobile phone!</strong>{% endif %}
```
