import pyautogui
import time
import threading
import tkinter
from tkinter import mainloop, Label, ttk

movingBool=False
stateString="Off"

def move_thread(window):
    global movingBool
    while True:
        try:
            if movingBool:
                pyautogui.moveRel(-10, 0)
                pyautogui.moveRel(10, 0)
                time.sleep(2)
            else:
                time.sleep(2)
        except:
            print("An exception occurred")
            time.sleep(2)

def switchMove():
    global movingBool
    global stateString

    if movingBool:
        movingBool=False
        stateString="Off"
    else:
        movingBool=True
        stateString="On"
    label1.config(text=stateString)

window = tkinter.Tk()
window.geometry("600x100")
window.resizable(0, 0)
window.configure(bg='gray20')
window.title("mouseMover")

button1 = tkinter.Button(text="On/Off", height=1, width=20, background = "gray20", activebackground = "gray20", foreground="white", activeforeground="white", command = switchMove)
button1.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

label1 = tkinter.Label(window, text=stateString, height=2, background = "gray20", foreground="white")
label1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button2 = tkinter.Button(text="Exit", height=1, width=20, background = "gray20", activebackground = "gray20", foreground="white", activeforeground="white", command = window.destroy)
button2.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

threading.Thread(target=move_thread, args=(window,), daemon=True).start()

mainloop()


