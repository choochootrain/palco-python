#!/usr/bin/env python

from utils import camera, bash, events
import time
import os
import sys
import readline
import random

import serial

cam = camera.Camera()
shell = bash.Bash()
events = events.Events()

if len(sys.argv) == 1:
  while True:
    cmd = raw_input()
    if cmd == 'quit':
      exit()
    elif cmd == 'cam':
      cam.step(False)
      print cam.save()
    elif cmd == 'programs':
      print shell.run(os.getcwd() + '/utils/./times.sh')
    elif cmd == 'event':
      evts = events.fast()
      print evts[random.randint(0,len(evts)-1)]
    elif 'say' in cmd:
      cmds = cmd.split(' ')
      print shell.run(os.getcwd() + '/utils/./say.sh ' + cmds[1])
else:
  while True:
    cam.step(True)
