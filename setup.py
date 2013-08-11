#!/usr/bin/env python
from distutils.core import setup

setup(name='Dota-notify',
      version='0.1',
      description='Display a notification when a dota tournament match begins.',
      author='Louis Taylor',
      author_email='kragniz@gmail.com',
      url='https://github.com/kragniz/dota-notifier',
      packages=['dotanotify'],
      scripts=['dota-notify']
     )
