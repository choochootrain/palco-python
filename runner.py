#!/usr/bin/env python

from utils import camera, bash
import time
import os
import readline

cam = camera.Camera()
shell = bash.Bash()

while True:
  cmd = raw_input()

  if cmd == 'cam':
    cam.step()
    print cam.save()
  elif cmd == 'programs':
    print shell.run(os.getcwd() + '/utils/./times.sh')
