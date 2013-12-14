try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

kargs = {}

kargs['name'] = 'PLoSPy'
kargs['version'] = ''
kargs['author'] = 'Georg R Walther'
kargs['author_email'] = 'contact@georg.io'
kargs['packages'] = ['plospy']
kargs['package_dir'] = {'plospy': 'plospy'}
kargs['url'] = 'http://georg.io'
kargs['license'] = 'BSD'
kargs['description'] = 'A library for handling PLoS data'
kargs['long_description'] = ''
kargs['test_suite'] = 'plospy.tests'
kargs['install_requires'] = ['BeautifulSoup']

setup(**kargs)
