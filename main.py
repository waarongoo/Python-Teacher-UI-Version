from tkinter import messagebox
from tkinter import *
import tkinter.messagebox as tm
import tkinter as tk
from tkinter import simpledialog
import turtle
from tkinter.ttk import *
application_window = tk.Tk()


def startlesson1():
    answer1 = simpledialog.askstring(
        "Lesson 1",
        'Now lets learn how to print stuff in the console. What is the console? The console is the black box that tells you stuff. \nHow do I print stuff? Well to do that use this print("Hello World")\n. Here try it yourself.'
    )
    if answer1 == 'print("Hello World")':
        tm.showinfo("Good Job!", "Good Job!")
        print("Hello World")

        def lesson2():
            tm.showinfo(
                "",
                "Ok so for this next lesson we are gonna use something called turtle. What is turtle? It is like the animal turtle you may ask? No, its a python package for drawing.\n\n"
            )
            tm.showinfo(
                "",
                "In this package, we can do many different things with the 'turtle'. Now choose what do you want to do with the turtle.\n\n"
            )

            go = True
            while go == True:
                choice = simpledialog.askstring(
                    "",
                    "                  Enter: \n 1. To move the turtle forward,\n 2. To move backwards,\n 3. To turn left,\n 4. To turn right,\n 5. To clear your drawing,\n 6. To stop drawing\n"
                )
                if choice == "1":
                    length = simpledialog.askstring(
                        "Turtle IDE", "How far do you want to move forward?")
                    turtle.forward(int(length))
                if choice == "2":
                    length = simpledialog.askstring(
                        "", "How far do you want to move backwards?")
                    turtle.backward(int(length))
                if choice == "3":
                    length = simpledialog.askstring(
                        "", "How many degrees do you want to turn left?")
                    turtle.left(int(length))
                if choice == "4":
                    length = simpledialog.askstring(
                        "", "How many degrees do you want to turn right?")
                    turtle.right(int(length))
                if choice == "5":
                    tm.showinfo("", "Your have cleared your drawing!")
                    turtle.clear()
                if choice == "6":
                    go = False
                    tm.showinfo("", "Did you have fun? If so great!")

        lesson2()


tm.showinfo("Hello!", "I am Robert your python teacher!")
answer = simpledialog.askstring("Input",
                                "What is your first name?",
                                parent=application_window)
if answer is not None:
    print("Your first name is ", answer)
    tm.showinfo("Hello!", "Nice to meet you " + answer)
    tm.showinfo("Start", "Lets start shall we?")
    startlesson1()

window = App()
window.protocol("WM_DELETE_WINDOW", window.check_quit)
window.resizable(True, True)
window.title("Python Teacher")
program = Tk()
photo = PhotoImage(file = "logo.png")
program.iconphoto(False, photo)