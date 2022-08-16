import os
from textwrap import fill
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer

window = Tk()
window.title("MP3 Music Player")
window.geometry("406x255")
window.configure(background="black")
window.resizable(0, 0)

left_frame = Frame(window, width=155, height=150, bg="white")
left_frame.grid(row=0, column=0)

right_frame = Frame(window, width=250, height=150, bg="black")
right_frame.grid(row=0, column=1, padx=1)

bottom_frame = Frame(window, width=405, height=100, bg="black")
bottom_frame.grid(row=1, column=0, columnspan=2, pady=1)

listbox = Listbox(right_frame, selectmode = SINGLE, font = "Arial 10 bold", bg="black", fg="white", width = 22, height = 7)
listbox.grid(row = 0, column = 0)

w = Scrollbar(right_frame, orient=HORIZONTAL)
w.grid(row = 1, column = 0)

listbox.config(xscrollcommand=w.set)
w.config(command=listbox.xview)

def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = (index + 1)
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    
    listbox.select_set(new_index)
    running_song['text'] = playing

def prev_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = (index - 1)
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    
    listbox.select_set(new_index)
    running_song['text'] = playing

def stop_music():
    mixer.music.stop()

image1 = Image.open("D://UNIcompiler - Python Engineer Internship//MP3 Music Player//Icons//music.png")
image1 = image1.resize((150, 150))
image1 = ImageTk.PhotoImage(image1)
appimage = Label(left_frame, image = image1, bg = "white")
appimage.place(x = 0, y = 0)

image2 = Image.open("D://UNIcompiler - Python Engineer Internship//MP3 Music Player//Icons//prev.png")
image2 = image2.resize((30, 30))
image2 = ImageTk.PhotoImage(image2)
rewind_button = Button(bottom_frame, height = 40, width = 40, image = image2, bg = "black", command = prev_music)
rewind_button.place(x = 50, y = 45)

image3 = Image.open("D://UNIcompiler - Python Engineer Internship//MP3 Music Player//Icons//play.png")
image3 = image3.resize((30, 30))
image3 = ImageTk.PhotoImage(image3)
play_button = Button(bottom_frame, height = 40, width = 40, image = image3, bg = "black", command = play_music)
play_button.place(x = 100, y = 45)

image4 = Image.open("D://UNIcompiler - Python Engineer Internship//MP3 Music Player//Icons//next.png")
image4 = image4.resize((30, 30))
image4 = ImageTk.PhotoImage(image4)
next_button = Button(bottom_frame, height = 40, width = 40, image = image4, bg = "black", command=next_music)
next_button.place(x = 150, y = 45)

image5 = Image.open("D://UNIcompiler - Python Engineer Internship//MP3 Music Player//Icons//pause.png")
image5 = image5.resize((30, 30))
image5 = ImageTk.PhotoImage(image5)
pause_button = Button(bottom_frame, height = 40, width = 40, image = image5, bg = "black", command=pause_music)
pause_button.place(x = 200, y = 45)

image6 = Image.open("D://UNIcompiler - Python Engineer Internship//MP3 Music Player//Icons//resume.png")
image6 = image6.resize((30, 30))
image6 = ImageTk.PhotoImage(image6)
resume_button = Button(bottom_frame, height = 40, width = 40, image = image6, bg = "black", command=resume_music)
resume_button.place(x = 250, y = 45)

image7 = Image.open("D://UNIcompiler - Python Engineer Internship//MP3 Music Player//Icons//stop.png")
image7 = image7.resize((30, 30))
image7 = ImageTk.PhotoImage(image7)
stop_button = Button(bottom_frame, height = 40, width = 40, image = image7, bg = "black", command=stop_music)
stop_button.place(x = 300, y = 45)

running_song = Label(bottom_frame, text = "Choose a Song", width = 44, font = ("Comic Sans MS", 11), padx = 5, height = 1, bg = "black", fg = "white", anchor = NW)
running_song.place(x = 0, y=1)

os.chdir(r'D://UNIcompiler - Python Engineer Internship//MP3 Music Player//music')
songs = os.listdir()

def show():
    for item in songs:
        listbox.insert(END, item)

show()

mixer.init()
music_State = StringVar()
music_State.set("Choose one!")

window.mainloop()