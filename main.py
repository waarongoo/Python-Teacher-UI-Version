from tkinter import messagebox
from tkinter import *
import tkinter.messagebox as tm
import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk()
class App(tk):
  def startlesson1():
    answer1 = simpledialog.askstring("Lesson 1",
        'Now lets learn how to print stuff in the console. What is the console? The console is the black box that tells you stuff. \nHow do I print stuff? Well to do that use this print("Hello World")\n. Here try it yourself.'
    )
    if answer1 == 'print("Hello World")':
      tm.showinfo("Good Job!","Good Job!")

        


  tm.showinfo("Hello!", "I am Robert your python teacher!")
  answer = simpledialog.askstring("Input", "What is your first name?",
                                parent=application_window)
  if answer is not None:
    print("Your first name is ", answer)
    tm.showinfo("Hello!","Nice to meet you "  + answer)
    tm.showinfo("Start","Lets start shall we?")
    startlesson1()

window = App()
#window.protocol("WM_DELETE_WINDOW", window.check_quit)
window.resizable(False, False)
window.title("Python Teacher")

