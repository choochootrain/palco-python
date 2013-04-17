from utils import camera, bash
import time

cam = camera.Camera()
shell = bash.Bash()

while True:
  cam.step()
