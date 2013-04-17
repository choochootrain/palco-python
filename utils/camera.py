#!/usr/bin/env python

import cv

class Camera:
  HAAR_CASCADE_PATH = "/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml"
  CAMERA_INDEX = 0

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

    cv.ShowImage("w1", self.image)
    cv.WaitKey(1)
