import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = ''

version = ''
with open('__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(name='dealtape-python-sdk',
      version=version,
      description='DealTape SDK for Python',
      long_description=readme,
      author='Yutao Zhang',
      author_email='yutao@recurrent.ai',
      packages=['dealtape-python-sdk'],
      license='MIT',
      platforms=['any'],
      install_requires=['requests!=2.9.0',],
      url='https://github.com/rcrai/dealtape-python-sdk'
)