#!/usr/bin/env python

import cv
import datetime
import os
from random import Random

class Camera:
  HAAR_CASCADE_PATH = "/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml"
  CAMERA_INDEX = 0
  RANDOM = Random()
  PT1 =  (RANDOM.randrange(-50, 2 * 50),
      RANDOM.randrange(-50, 2 * 50))
  line_type = cv.CV_AA
  FONT = cv.InitFont(RANDOM.randrange(0, 8),
    RANDOM.randrange(0, 100) * 0.05 + 0.01,
    RANDOM.randrange(0, 100) * 0.05 + 0.01,
    RANDOM.randrange(0, 5) * 0.1,
    RANDOM.randrange(0, 10),
    line_type)

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
      cv.Rectangle(self.image, (x,y), (x+w,y+h), 255)
      cv.PutText(self.image, "THIS IDIOT IS STILL ON THE COMPUTER", Camera.PT1, Camera.FONT, self.random_color(Camera.RANDOM))

    cv.ShowImage("w1", self.image)
    cv.WaitKey(1)

    return self.image

  def save(self):
    name = os.getcwd() + '/images/' + str(datetime.datetime.now()) + '.jpg'
    cv.SaveImage(name, self.image)
    return name

  def random_color(self, random):
    icolor = random.randint(0, 0xFFFFFF)
    return cv.Scalar(icolor & 0xff, (icolor >> 8) & 0xff, (icolor >> 16) & 0xff)
