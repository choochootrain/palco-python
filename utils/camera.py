#!/usr/bin/env python

import cv
import datetime
import os
import math
from random import Random

class Camera:
  HAAR_CASCADE_PATH = "/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml"
  CAMERA_INDEX = 1
  LINE_TYPE = cv.CV_AA
  FONT = cv.InitFont(0, 1, 1, 0, 3, LINE_TYPE)
  WHITE = cv.Scalar(55, 255, 55)

  def __init__(self):
    cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)

    self.capture = cv.CaptureFromCAM(Camera.CAMERA_INDEX)
    self.storage = cv.CreateMemStorage()
    self.cascade = cv.Load(Camera.HAAR_CASCADE_PATH)
    self.image = cv.QueryFrame(self.capture)
    self.faces = []

  def detect_faces(self):
    self.faces = []
    detected = cv.HaarDetectObjects(self.image, self.cascade, self.storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
      for (x,y,w,h),n in detected:
        self.faces.append((x,y,w,h))

  def step(self):
    self.image = cv.QueryFrame(self.capture)

    self.detect_faces()
    print self.faces

    for (x,y,w,h) in self.faces:
      cv.PutText(self.image, "THIS IDIOT IS STILL ON THE COMPUTER", (0, 30), Camera.FONT, Camera.WHITE)
      arrow(self.image, (70, 40), (x, y), Camera.WHITE)

    cv.ShowImage("w1", self.image)
    cv.WaitKey(1)

    return self.image

  def save(self):
    name = os.getcwd() + '/images/' + str(datetime.datetime.now()) + '.jpg'
    cv.SaveImage(name, self.image)
    return name

def arrow(img, p1, p2, color):
  angle = math.atan(float(p2[1]-p1[1])/(p2[0]-p1[0]))
  p2a = (p2[0]-int(10*math.cos(angle+math.pi/4)),
         p2[1]-int(10*math.sin(angle+math.pi/4)))
  p2b = (p2[0]-int(10*math.cos(angle-math.pi/4)),
         p2[1]-int(10*math.sin(angle-math.pi/4)))

  cv.Line(img, p1, p2,  color, 2)
  cv.Line(img, p2a, p2, color, 2)
  cv.Line(img, p2b, p2, color, 2)
