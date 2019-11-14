
from tkinter import *
import tkinter.font
from PIL import ImageTk, Image

img = Image.open("gest1img.jpg")
img = img.rotate(-90)
img.show()