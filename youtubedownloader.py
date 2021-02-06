from pytube import YouTube
from pytube import Playlist
import tkinter as tk
from tkinter import *

class mywindow:
    def __init__(self, win):
        self.l1 = Label(win, text="Enter Your Link Here", font=('arial', 15, 'bold'))
        self.l1.place(x=350, y=200)
        self.e1 = Entry(font=('arial', 13, 'bold'))
        self.e1.place(x=350, y=240)
        self.btn = Button(win, text="Download", fg="black", bg="white", font=('arial', 15, 'bold'), command=self.Downloader)
        self.btn.place(x=400, y=270)
        self.l2 = Label(win, text="Enter The Link Of Your Playlist", font=('arial', 15, 'bold'))
        self.l2.place(x=300, y=350)
        self.e2 = Entry(font=('arial', 15, 'bold'))
        self.e2.place(x=350, y=390)
        self.plbtn = Button(win, text="Download", fg="black", bg="white", font=('arial', 15, 'bold'), command=self.PlaylistDownload)
        self.plbtn.place(x=400, y=430)
        self.l3 = Label(win, text="Audio Only Download", font=('arial', 15, 'bold'))
        self.l3.place(x=350, y=510)
        self.e3 = Entry(font=('arial', 15, 'bold'))
        self.e3.place(x=350, y=550)
        self.aubtn = Button(win, text="Download", fg='black', bg='white', font=('arial', 15, 'bold'), command=self.AudioDownload)
        self.aubtn.place(x=400, y=590)

    def Downloader(self):
        url = YouTube(str(self.e1.get()))
        """You Can Change the get_by_itag option to your own choice to change the video quality"""
        video = url.streams.get_by_itag(136)
        video.download()
        window.destroy()

    def PlaylistDownload(self):
        pl = Playlist(str(self.e2.get()))
        for video in pl.videos:
            video.streams.first().download()
        window.destroy()

    def AudioDownload(self):
        au = YouTube(str(self.e3.get()))
        audio = au.streams.get_by_itag(251)
        audio.download()
        window.destroy()

window = tk.Tk()
mywin = mywindow(window)
window.geometry("1000x1000")
window.title("Youtube Video Downloader")
img = PhotoImage(file='youtube.png')
l1 = tk.Label(window, image=img).pack(side="top")
window.mainloop()

