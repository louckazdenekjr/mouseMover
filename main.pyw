import pyautogui
import sys
import threading
import time
import tkinter

#----------------------------------------

movingBool = False
movingBoolLock = threading.Lock()

#----------------------------------------

def moveThreadFunc():
    global movingBool
    
    moveInterval = 10
    xDistance = 10
    yDistance = 0
    
    while True:
        with movingBoolLock:
            if movingBool:
                pyautogui.moveRel (
                    xDistance, 
                    yDistance
                )
                
                pyautogui.moveRel (
                    -xDistance,
                    yDistance
                )
            
        # sleep between movements, doubles as rate limiting and poll for changes
        time.sleep(moveInterval)

def exitApp():
    sys.exit(0)

def runApp():
    # define app function to switch states
    def switchMove():
        global movingBool

        # switch moving bool
        with movingBoolLock:
            if movingBool:
                movingBool = False
            else:
                movingBool = True
            
        # update label
        if movingBool:
            label1.config(text = "On")
        else:
            label1.config(text = "Off")
            
    # define app
    window = tkinter.Tk()
    background_color = "#1e1e1e"
    font_color = "#c8c8c8"
    window.geometry("600x100")
    window.resizable(False, False)
    window.configure(background = background_color)
    window.title("mouseMover")
    
    # define widgets
    label1 = tkinter.Label (
        window,
        text                = "Off",
        height              = 2, 
        background          = background_color,
        foreground          = font_color
    )
    
    button1 = tkinter.Button (
        text                = "On/Off", 
        height              = 1, 
        width               = 10, 
        background          = background_color, 
        foreground          = font_color,
        activebackground    = background_color, 
        activeforeground    = font_color,
        command             = switchMove
    )
    
    button2 = tkinter.Button (
        text                = "Exit", 
        height              = 1, 
        width               = 10, 
        background          = background_color, 
        foreground          = font_color,
        activebackground    = background_color, 
        activeforeground    = font_color,
        command             = exitApp
    )
    
    # place widgets
    label1.place (
        relx        = 0.5, 
        rely        = 0.5, 
        anchor      = tkinter.CENTER
    )
    
    button1.place(
        relx        = 0.2, 
        rely        = 0.5, 
        anchor      = tkinter.CENTER
    )
    
    button2.place (
        relx        = 0.8, 
        rely        = 0.5, 
        anchor      = tkinter.CENTER
    )
    
    # define and dispatch threads
    moveThread = threading.Thread (
        target      = moveThreadFunc, 
        daemon      = True
    )
    
    moveThread.start()
    
    # start event loop
    tkinter.mainloop()
    
#----------------------------------------

if __name__ == "__main__":
    runApp()
