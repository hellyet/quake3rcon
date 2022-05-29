from setuptools import setup, find_packages

setup(
    name='q3rcon-py',
    version='1.0.1',
    url='https://github.com/hellyet/q3rcon-py',
    license='MIT',
    author='hellyet',
    author_email='leonid.tosterovski@gmail.com',
    description='A tiny library for using Quake 3\'s RCON protocol feature for some game servers like FiveM.',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False
)