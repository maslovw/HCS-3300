from setuptools import setup
import re


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('hcs_3300/bin/hcs3300.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name='hcs_3300',
    version=version,
    packages=['hcs_3300', 'hcs_3300.bin'],
    entry_points={"console_scripts": ['hcs3300 = hcs_3300.bin.hcs3300:main', 'hcs_3300 = hcs_3300.bin.hcs3300:main']},
    install_requires=['pyserial>=3.3'],
    python_requires='>3.5',
    url='https://github.com/maslovw/HCS-3300',
    author='maslovw',
    author_email='maslovw@gmail.com',
    license='MIT',
    keywords='HCS-3300 REMOTE PROGRAMMABLE Power Supply',
    description='Handles HCS-3300 (Remote Programmable Power Supply with DC wave form generator) '
                'command usage: hcs3300 --help'
)
