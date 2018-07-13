from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from shutil import copyfile
import os
from subprocess import Popen


def UploadFile():
	uploadedfilenames = askopenfilenames(multiple=True)
	if uploadedfilenames == '':
		tkMessageBox.showinfo(message="File Upload has been cancelled program will stop")
		return
	uploadedfiles = master.splitlist(uploadedfilenames)
	print type(uploadedfiles)
	filepath = str(uploadedfiles[0])
	f = open(filepath)
	s = f.read()
	copyfile(filepath,"story.txt")

def Ask():
	f = open("question.txt","w")
	f.write(e1.get())
	f.close()
	Process=Popen('sh %s' % (str("dist/Model1/run.sh"),), shell=True)
	Process.wait()
	f = open("answer.txt")
	s = f.read()
	tkMessageBox.showinfo("Answer",s)

def Ask2():
	f = open("question.txt","w")
	f.write(e1.get())
	f.close()
	Process=Popen('sh %s' % (str("dist/Model2/run.sh"),), shell=True)
	Process.wait()
	f = open("answer.txt")
	s = f.read()
	tkMessageBox.showinfo("Answer",s)

def viewGraph():
	Process=Popen('python %s' % (str("dist/Model1/graph.py"),), shell=True)
	Process.wait()
	
master = Tk()
master.title("Question Answering System")
Label(master, text="Question").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Upload File', command=UploadFile).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Model1', command=Ask).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Model2', command=Ask2).grid(row=3,column=3,sticky=W,pady=4)
Button(master, text='View Graph', command=viewGraph).grid(row=3,column=2,sticky=W,pady=4)

mainloop( )
