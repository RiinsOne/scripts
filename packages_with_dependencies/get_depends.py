#/usr/bin/python3
from sys import argv as _argv
from subprocess import run as _run
from os import path as _path
from os import getcwd as _getcwd
from time import sleep as _sleep


args = _argv[1:]
pwd = _getcwd()

for arg in args:
    if not _path.exists(arg):
        _run('mkdir {dir_name}'.format(dir_name=arg), shell=True)

    _run('apt-get download $(apt-cache depends --recurse --no-recommends --no-suggests \
      --no-conflicts --no-breaks --no-replaces --no-enhances \
      --no-pre-depends {arg} | grep "^\w")'.format(arg=arg), shell=True)
    _run('mv *.deb {pwd}/{dir_name}'.format(pwd=pwd, dir_name=arg), shell=True)
    _sleep(0.1)
    
