# Multimedia Project 2 Movie editor + Soundboard: Tyler, Daniel, Brandon

import subprocess
from tkinter import *
from moviepy.editor import *

# Gets the location of the sound files for playing on the Soundboard

sound1 = "‪C:/Project2/beep.mp3"
sound2 = "C:/Project2/Clang.mp3"
sound3 = "C:/Project2/Scream.mp3"
sound4 = "C:/Project2/Swoosh.mp3"
sound5 = "C:/Project2/Woosh.mp3"
sound6 = "C:/Project2/Punch.mp3"
sound7 = "C:/Project2/Hit.mp3"
sound8 = "C:/Project2/Cry.mp3"
sound9 = "C:/Project2/Laugh.mp3"
sound10 = "C:/Project2/Guts.mp3"


scene = VideoFileClip("C:/Project2/Killbill.mp4", audio=True).subclip(59, 200)
# Gets the movie file and clips it down to desired length
scene = scene.fx(vfx.blackwhite)
# Applies the Black and White filter to the movie
scene = scene.volumex(0.5)
# Reduces the volume of the clipped movie by 50%
scene.write_videofile("C:/Project2/Edited_clip.mp4", fps=24, codec='mpeg4')
# Writes the new file to your desired location


def open_window():
    num1.set("Open_window")
    subprocess.call('open C:/Project2/Edited_clip.mp4', shell=True)
    return


def sound_1():  # Defines a sound for the 1st button
    num1.set("****")
    subprocess.call(["afplay", sound1])
    return


def sound_2():  # Defines a sound for the 2nd button
    num1.set("Clang")
    subprocess.call(["afplay", sound2])
    return


def sound_3():  # Defines a sound for the 3rd button
    num1.set("Scream")
    subprocess.call(["afplay", sound3])
    return


def sound_4():  # Defines a sound for the 4th button
    num1.set("Swoosh")
    subprocess.call(["afplay", sound4])
    return


def sound_5():  # Defines a sound for the 5th button
    num1.set("Woosh")
    subprocess.call(["afplay", sound5])
    return


def sound_6():  # Defines a sound for the 6th button
    num1.set("Punch")
    subprocess.call(["afplay", sound6])
    return


def sound_7():  # Defines a sound for the 7th button
    num1.set("Hit")
    subprocess.call(["afplay", sound7])
    return


def sound_8():  # Defines a sound for the 8th button
    num1.set("Cry")
    subprocess.call(["afplay", sound8])
    return


def sound_9():  # Defines a sound for the 9th button
    num1.set("Laugh")
    subprocess.call(["afplay", sound9])
    return

root = Tk()  # Sets the box for the GUI
frame = Frame(root) # Sets the frame for the GUI

num1 = StringVar()  # Sets the names of the buttons in the GUI

# Below is the buttons and location of the buttons

topframe = Frame(root)
topframe.pack(side=TOP)
txtDisplay = Entry(frame, textvariable=num1, bd=20, insertwidth=1, font=30, justify='center', width=4)
txtDisplay.pack(side=TOP)

button0 = Button(topframe, padx=8, height=2, pady=2, bd=8, text="Open_Window ", bg="black", fg="white", command=open_window)
button0.pack(side=LEFT)

button1 = Button(topframe, padx=8, height=2, pady=2, bd=8, text="**** ", bg="black", fg="white", command=sound_1)
button1.pack(side=LEFT)

button2 = Button(topframe, padx=8, height=2, pady=2, bd=8, text="Clang ", bg="black", fg="white", command=sound_2)
button2.pack(side=LEFT)

button3 = Button(topframe, padx=8, height=2, pady=2, bd=8, text="Scream ", bg="black", fg="white", command=sound_3)
button3.pack(side=LEFT)

frame1 = Frame(root)
frame1.pack(side=TOP)

button4 = Button(frame1, padx=8, height=2, pady=2, bd=8, text="Swoosh ", bg="black", fg="white", command=sound_4)
button4.pack(side=LEFT)

button5 = Button(frame1, padx=8, height=2, pady=2, bd=8, text="Woosh ", bg="black", fg="white", command=sound_5)
button5.pack(side=LEFT)

button6 = Button(frame1, padx=8, height=2, pady=2, bd=8, text="Punch ", bg="black", fg="white", command=sound_6)
button6.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(side=TOP)

button7 = Button(frame2, padx=8, height=2, pady=2, bd=8, text="Hit ", bg="black", fg="white", command=sound_7)
button7.pack(side=LEFT)

button8 = Button(frame2, padx=8, height=2, pady=2, bd=8, text="Cry ", bg="black", fg="white", command=sound_8)
button8.pack(side=LEFT)


button9 = Button(frame2, padx=8, height=2, pady=2, bd=8, text="Laugh ", bg="black", fg="white", command=sound_9)
button9.pack(side=LEFT)


root.title('SoundBoard')    # Sets the name of the GUI @ the top
root.mainloop()  # Basically how tkinter ends the script
