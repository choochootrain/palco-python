#!/usr/bin/env python

from utils import camera, bash, events
from itertools import cycle
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
found = 0
lost = 0

welcomes = cycle(['lazybones', 'alive', 'buddy'])
insults = cycle(['facebook', 'homework', 'notpopular'])
events = cycle([
    'http://portugal2013sf-es2.eventbrite.com',
    'http://gatsbypremiere-es2.eventbrite.com',
    'http://cfadrinkupsf-es2.eventbrite.com',
    'http://tchotour-es2.eventbrite.com',
    'http://unreasonabledrinkssf-es2.eventbrite.com'
])

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
      if time.time() - found > 3:
        say(welcomes.next())
        responded = True

    if present:
      found = time.time()

      if int(time.time()) % 30 == 0:
        progs = shell.run(os.getcwd() + '/utils/./times.sh')
        if random.random() > 0.5:
          say('event')
          shell.run('google-chrome ' + events.next())
        else:
          say(insults.next())
