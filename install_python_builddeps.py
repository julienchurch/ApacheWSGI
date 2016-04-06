#!/usr/bin/env python
from subprocess import STDOUT, check_call
import os

def install(package):
  params = ['sudo', 'apt-get', 'install', '-y', package]
  check_call(params, stdout=None, stderr=None)

packages_to_install = [
                       'make'
                      ,'build-essential'
                      ,'libssl-dev'
                      ,'zlib1g-dev'
                      ,'libbz2-dev'
                      ,'libreadline-dev'
                      ,'libsqlite3-dev'
                      ,'wget'
                      ,'curl'
                      ,'llvm'
                      ,'libncurses5-dev'
                      ]

for package in packages_to_install:
  install(package)
