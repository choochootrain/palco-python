#!/usr/bin/env python

from utils import camera, bash, events
import time
import os
import sys
import readline

cam = camera.Camera()
shell = bash.Bash()
events = events.Events()

if len(sys.argv) == 1:
  while True:
    cmd = raw_input()

    if cmd == 'cam':
      cam.step()
      print cam.save()
    elif cmd == 'programs':
      print shell.run(os.getcwd() + '/utils/./times.sh')
    elif cmd == 'events':
      print events.nearby()[0:10]
else:
  while True:
    cam.step()
