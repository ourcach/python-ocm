try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Open Charge Map API wrapper',
    'author': 'Rui Silva',
    'url': 'https://github.com/ourcach/python-ocm',
    'download_url': 'https://github.com/ourcach/python-ocm',
    'author_email': 'rds.mcc@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ocm'],
    'scripts': [],
    'name': 'python-ocm'
}

setup(**config)
