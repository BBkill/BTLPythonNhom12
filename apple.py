from tkinter import *
from time import sleep
from PIL import ImageTk, Image
from random import randint

class Apple:
  def __init__(self,img,speed,canvas):
    self.img=img
    self.speed=speed
    self.canvas=canvas

  def new(self):
    self.speed=0

  def falling(self):
    canvas.move(img,0,speed)

