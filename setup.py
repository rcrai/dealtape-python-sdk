import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(name='dealtape',
      version="0.0.8",
      description='DealTape SDK for Python',
      long_description=readme,
      author='Yutao Zhang',
      author_email='yutao@recurrent.ai',
      packages=['dealtape'],
      license='MIT',
      platforms=['any'],
      install_requires=['requests>=2.20.0',],
      url='https://github.com/rcrai/dealtape-python-sdk'
)

