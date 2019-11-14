from tkinter import *
import tkinter.font
from PIL import ImageTk, Image
import matplotlib



def createWidgets():
    font = tkinter.font.Font(family="Verdana", size="15")

    # clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # set the title
    root.winfo_toplevel().title("Classifier")

    # set new widgets
    root.About_btn = Button(root,  height=2, width=20,text="About application",font=font,command = aboutWindow)
    root.About_btn.place(x=260, y=100)

    root.Start_btn = Button(root,  height=2, width=20,text="Start acquisition",font=font,command = calibrationWindow)
    root.Start_btn.place(x=260, y=250)

    root.Quit_btn = Button(root,  height=2, width=20,text="Quit application",font=font,command = root.quit)
    root.Quit_btn.place(x=260, y=400)


def aboutWindow():
    font = tkinter.font.Font(family="Verdana", size="15")
    # clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # set new widgets

    root.About_txt = Label(root, wraplength=400, text="This application will provide resources for classification of gestures. It works in real time. First, you will be asked to calibrate the system by doing specific gestures. Next, go to the acquisition part and start the acquisition!", font=font)
    root.About_txt.place(x=220, y=200)

    root.Back_btn = Button(root,  height=1, width=15,text="Back",font=font,command = createWidgets)
    root.Back_btn.place(x=500, y=500)


def calibrationWindow():

    #create font
    titleFont = tkinter.font.Font(family="Verdana", size="16", weight="bold" )
    font = tkinter.font.Font(family="Verdana", size="15")

    # clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # set new widgets

    root.Title_txt = Label(root, text="Calibration", font=titleFont)
    root.Title_txt.place(x=310, y=30)

    root.Explanation_txt = Label(root, text="You are asked to do all of the gestures below", font=font)
    root.Explanation_txt.place(x=170, y=70)

    img1 = Image.open("testt1.png")
    photo1 = ImageTk.PhotoImage(img1)
    root.Photo_1 = Label(image=photo1)
    root.Photo_1.image = photo1
    root.Photo_1.place(x=0, y=120)

    root.Acquisition_btn = Button(root,  height=1, width=15,text="Start",font=font,command = acquisitionWindow)
    root.Acquisition_btn.place(x=500, y=500)

def acquisitionWindow():

    #create font
    font = tkinter.font.Font(family="Verdana", size="15")
    resultFont = tkinter.font.Font(family="Verdana", size="16", weight="bold")

    # clear widgets
    for widget in root.winfo_children():
        widget.destroy()

    # create widgets

    root.Stop_btn = Button(root,  height=1, width=15,text="Quit application",font=font,command = root.quit)
    root.Stop_btn.place(x=70, y=50)

    root.Result_txt = Label(root, text="Key grip", font=resultFont)
    root.Result_txt.place(x=580, y=270)

    img2 = Image.open("Classification_result.png")
    img2 = img2.resize((450,315), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(img2)
    root.Photo_2 = Label(image=photo2)
    root.Photo_2.image = photo2
    root.Photo_2.place(x=50, y=160)


root = Tk()
root.geometry('800x600')
createWidgets()
root.mainloop()
root.destroy()
