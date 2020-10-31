import cv2
import numpy as np
import random
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

path = ""
def getperm(d):
    l = d.copy()
    l = l.flatten()
    seed = sum(l)
    random.seed(seed)
    perm = list(range(len(d)))
    random.shuffle(perm)
    random.seed() 
    return perm

def shuffle(l): 
    perm = getperm(l) 
    l[:] = [l[j] for j in perm] 

def unshuffle(l):  
    perm = getperm(l)  
    res = [None] * len(l) 
    for i, j in enumerate(perm):
        res[j] = l[i]
    l[:] = res  


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


class Root(Tk):
    img = None
    imgflat = None
    sh0 = 0
    sh1 = 0
    def __init__(self):
        super(Root, self).__init__()
        self.title("Image Bit Shuffle Encoder By Boat")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.button()
        self.labelFrame2 = ttk.LabelFrame(self, text = "Encode")
        self.labelFrame2.grid(column = 0, row = 2, padx = 20, pady = 20)
        self.Encodebutton()

        self.labelFrame3 = ttk.LabelFrame(self, text = "Decode")
        self.labelFrame3.grid(column = 0, row = 3, padx = 20, pady = 20)
        self.Decodebutton()

        self.label2 = Label()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def Encodebutton(self):
        self.button = ttk.Button(self.labelFrame2, text = "Encode",command = self.shuffleEncode)
        self.button.grid(column = 1, row = 1)

    def Decodebutton(self):
        self.button = ttk.Button(self.labelFrame3, text = "Decode",command = self.shuffleDecode)
        self.button.grid(column = 1, row = 1)

    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)

        img = Image.open(self.filename)
        photo = ImageTk.PhotoImage(img)
        self.label2.destroy()
        self.label2 = Label(image=photo)
        self.label2.image = photo 
        self.label2.grid(column=3, row=4)
        self.img = self.filename
        imgflat = None

    def shuffleEncode(self):
        if self.img is not None:
            path =os.path.normpath(self.img)
            img = cv2.imread(path)
            imgflat = img.flatten()
            shuffle(imgflat)
            imgflat = np.reshape(imgflat, (img.shape[0],img.shape[1],3))
            photo = ImageTk.PhotoImage(Image.fromarray(imgflat))
            self.label2.destroy()
            self.label2 = Label(image=photo)
            self.label2.image = photo
            self.label2.grid(column=3, row=4)
            self.imgflat = imgflat
            self.sh0 = img.shape[0]
            self.sh1 = img.shape[1]

    def shuffleDecode(self):
        if self.imgflat is not None:
            imgflat = self.imgflat.flatten()
            unshuffle(imgflat)
            imgflat = np.reshape(imgflat, (self.sh0,self.sh1,3))[:,:,::-1]
            photo = ImageTk.PhotoImage(Image.fromarray(imgflat))
            self.label2.destroy()
            self.label2 = Label(image=photo)
            self.label2.image = photo
            self.label2.grid(column=3, row=4)
            self.imgflat = None

root = Root()
root.mainloop()