from tkinter import *
from tkinter.messagebox import showwarning
import os
from datetime import datetime
import ctypes, sys

Version = "1.0.1"

Main = Tk()
Main.geometry("400x50")
Main.title("AMFW github@" + Version)

def UACElevationCheck():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

ReArmInstructions = Label(text="Select from the list of options below to manage activation.")
ReArmFireButton = Button(text="Run SbMgr Rearm Utility (may break Real Activation)", command=lambda: SbmgrRearmActivation())

def Log(status: str):
    Now = datetime.now()
    Time = Now.strftime("%H:%M:%S")
    print("[STATUS " + Time + "] " + status)

def SbmgrRearmActivation():
    Log("Please wait... checking/requesting elevated permissions.")
    if UACElevationCheck():
        Log("System-Command: slmgr /rearm")
        os.system("slmgr /rearm")
    else:
        showwarning("UAC Elevation Required", message="This program needs User Account Control Elevation (administrator permissions) to run. Will now call UAC Elevation request.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

ReArmInstructions.pack()
ReArmFireButton.pack()

Main.mainloop()