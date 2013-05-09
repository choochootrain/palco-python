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
present = False
responded = False

welcomes = ['lazybones', 'alive', 'buddy']
insults = ['event', 'facebook', 'homework', 'notpopular']

def rand(arry):
  return arry[int(random.random()*len(arry))]

def say(msg):
  return shell.run(os.getcwd() + '/utils/./say.sh ' + msg)

if len(sys.argv) == 1:
  while True:
    cmd = raw_input()
    cam.step(False)
    if cmd == 'quit':
      exit()
    elif cmd == 'cam':
      print cam.save()
    elif cmd == 'programs':
      print shell.run(os.getcwd() + '/utils/./times.sh')
    elif cmd == 'event':
      evts = events.fast()
      print evts[random.randint(0,len(evts)-1)]
    elif 'say' in cmd:
      cmds = cmd.split(' ')
      say(cmds[1])
else:
  while True:
    cam.step(True)
    present = len(cam.face()) > 0

    print present
    if present and not responded:
      say(rand(welcomes))
      responded = True

    if not present:
      responded = False

    if present:
      if int(time.time()) % 8 == 0:
        progs = shell.run(os.getcwd() + '/utils/./times.sh')

        if 'chrome' in progs and random.random() > 0.95:
          say(rand(insults))
