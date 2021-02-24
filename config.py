import os

def echo(msg='',end='\n'):
    print(msg,end=end)

def startpython():
    os.system("python teacher.py")

def configHelp():
    print(
"""
== Help Manual ==
startpython Starts the Python Teacher
"""
)