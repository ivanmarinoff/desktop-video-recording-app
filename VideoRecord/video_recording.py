from multiprocessing import *
import cv2
import numpy as np
from time import sleep
import pyautogui
import platform
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile as save_as
from tkinter import simpledialog
import os
import webbrowser


# Main function to record screen
def record_screen():
    SCREEN_SIZE = tuple(pyautogui.size())
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # frames per second
    fps = 12.0
    # create the video write object
    out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))
    # the time you want to record in seconds
    record_seconds = 100000
    for i in range(int(record_seconds * fps)):
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # if the user clicks the button stop recording, it exits
        if (open("cache", "r").read() == "stop"):
            open("cache", "w").write("")
            break
    cv2.destroyAllWindows()
    out.release()


# This function start the recording
def start_record():
    if ("__cache__" in os.listdir()):
        open("__cache__", "w").write("")
    else:
        open("__cache__", "a").write("")
    while (0 < 1):
        y = open("__cache__", "r").read()
        if (y == "do"):
            record_screen()
        else:
            sleep(2)


# function for releasing recorded video
def main_releasing():
    def releasing():
        t = save_as()
        l = "output.avi"
        if (t != None):
            t = t.name + ".avi"
            shutil.copy(l, t)
            button_3.place(x=150, y=1000)
            messagebox.showinfo("File saved", "Your file has been saved")

    # checking the presence of cache file in file system
    if ("cache" in os.listdir()):
        open("cache", "w").write("")
    else:
        open("cache", "a").write("")

    ##export the video is random name in .avi format
    # filename = str(len(os.listdir("video")))+".avi"

    # For start recording, this function writes "" in cache file, due to which the main.py file starts recording the screen
    def play():
        open("__cache__", "w").write("do")
        open("cache", "w").write("")
        bitton_2.place(x=15, y=80)
        button_1.place(x=150, y=1000)

    # For stop recording, this function writes "stop" in cache file, due to which the main.py file stop recording the screen
    def stop():
        open("__cache__", "w").write("")
        open("cache", "w").write("stop")
        button_1.place(x=15, y=80)
        button_3.place(x=15, y=170)
        bitton_2.place(x=150, y=1000)

    # Function to open browser
    def github():
        try:
            webbrowser.open("https://github.com/ivanmarinoff")
        except Exception as ss:
            try:
                messagebox.showerror("Error", str(ss))
            except:
                messagebox.showerror("Error",
                                     "Not able to open your default browser, kindly examine your system's default browser!")

    t = Tk()
    t.title("Screen")
    t.geometry("280x320")
    t.resizable(0, 0)
    Label(t, background="#8E8E90", height=5, width=500, padx=5, pady=5).place(x=0, y=0)
    Label(t, background="#8E8E90", text="Screen recorder", foreground="black", font=('Comic sans MS', 19), padx=5,
          pady=5) \
        .place(x=10, y=0)
    Label(t, background="black", height=30, width=500, padx=5, pady=5).place(x=0, y=50)
    # photo = PhotoImage(file=r"C:\Users\Studio6\Documents\SoftUni\VideoRecord\record.png")
    button_1 = Button(t, text="Start recording", font=('Comic sans MS', 15), command=play, background="#BC0116",
                      foreground="black", activebackground="white", activeforeground="black")
    bitton_2 = Button(t, text="Stop recording", font=('Comic sans MS', 15), command=stop, background="#BC0116",
                foreground="black", activebackground="white", activeforeground="black")
    button_3 = Button(t, text="Release video", font=('Comic sans MS', 15), command=releasing, background="#BC0116",
                foreground="black", activebackground="white", activeforeground="black")
    Button(t, text="By IvanMarinoff", font=('Comic sans MS', 13), command=github, background="grey", foreground="white",
           activebackground="white", activeforeground="black", padx=5, pady=5).place(x=10, y=230)
    button_1.place(x=15, y=80)
    bitton_2.place(x=1500, y=1000)
    t.mainloop()


if __name__ == '__main__':
    t = Process(target=main_releasing)
    t2 = Process(target=start_record)
    t.start()
    t2.start()
    t.join()