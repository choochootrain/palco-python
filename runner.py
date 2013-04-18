#!/usr/bin/env python

from utils import camera, bash
import time
import os
import sys
import readline

cam = camera.Camera()
shell = bash.Bash()

if len(sys.argv) == 1:
  while True:
    cmd = raw_input()

    if cmd == 'cam':
      cam.step()
      print cam.save()
    elif cmd == 'programs':
      print shell.run(os.getcwd() + '/utils/./times.sh')
else:
  while True:
    cam.step()
