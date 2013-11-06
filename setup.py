"""
Flask-Devices
----------

A Flask extension for switching template folder automatically by User Agent.

"""
from setuptools import setup


setup(
    name='Flask-Devices',
    version='0.0.1',
    url='https://github.com/yasunori/flask-devices',
    license='BSD',
    author='Yasunori Gotoh',
    author_email='yasunori@gotoh.me',
    maintainer='Yasunori Gotoh',
    maintainer_email='yasunori@gotoh.me',
    description='Flask extension for switching template folder automatically by User Agent',
    long_description=__doc__,
    py_modules=[
        'flask_devices'
    ],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    tests_require=[
        'nose',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
