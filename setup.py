from setuptools import setup, find_packages

setup(
    name='q3ron-py',
    version='v1.0.0',
    url='https://github.com/hellyet/q3rcon-py',
    license='MIT',
    author='hellyet',
    description='A tiny library for using Quake 3\'s RCON protocol feature for some game servers like FiveM or Quake.',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    zip_safe=False
)