flask-devices
=============

Switch Flask's template folder automatically by request's user-agent(iPhone, iPad, Android, PC, and so on)

## Usage
```
devices = Devices(app)
devices.add_pattern('mobile', 'android|fennec|iemobile|iphone|opera (?:mini|mobi)', 'webapp/templates/mobile')
devices.add_pattern('chrome', 'Chrome', webapp/templates/chrome)
devices.add_pattern('pc', '.*', 'webapp/templates/pc')
```

## Other
```view.py
@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.DEVICE) # mobile, pc,
    if(request.DEVICE == 'pc'):
        # pc
```

```example.html
{% if request.DEVICE == 'mobile' %}<strong>I'm mobile</strong>{% endif %}
```
