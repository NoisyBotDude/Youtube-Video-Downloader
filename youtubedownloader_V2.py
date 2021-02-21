from pytube import YouTube
from pytube import Playlist
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# noinspection DuplicatedCode
class mywindow:

    def __init__(self, win):
        self.l1 = Label(win, text="Enter Your Link Here", font=('arial', 15, 'bold'))
        self.l1.place(x=350, y=200)
        self.e1 = Entry(font=('arial', 13, 'bold'))
        self.e1.place(x=350, y=240)
        self.btn = Button(win, text="Download", fg="black", bg="white", font=('arial', 15, 'bold'),
                          command=self.Downloader)
        self.btn.place(x=400, y=270)
        self.qualitylabel = Label(win, text="Select Your Video Quality to Download", font=('arial', 15, 'bold'))
        self.qualitylabel.place(x=590, y=200)
        self.quality = ttk.Combobox(values=list(combobox_keys),
                                    font=('arial', 15, 'bold'), width=5)
        self.quality.place(x=680, y=240)
        self.l2 = Label(win, text="Enter The Link Of Your Playlist", font=('arial', 15, 'bold'))
        self.l2.place(x=280, y=350)
        self.e2 = Entry(font=('arial', 15, 'bold'))
        self.e2.place(x=350, y=390)
        self.plbtn = Button(win, text="Download", fg="black", bg="white", font=('arial', 15, 'bold'),
                            command=self.PlaylistDownload)
        self.plbtn.place(x=400, y=430)
        self.qualitypllabel = Label(win, text="Select Your Video Quality to Download", font=('arial', 15, 'bold'))
        self.qualitypllabel.place(x=590, y=350)
        self.qualitypl = ttk.Combobox(values=list(combobox_keys),
                                      font=('arial', 15, 'bold'), width=5)
        self.qualitypl.place(x=680, y=390)
        self.l3 = Label(win, text="Audio Only Download", font=('arial', 15, 'bold'))
        self.l3.place(x=350, y=510)
        self.e3 = Entry(font=('arial', 15, 'bold'))
        self.e3.place(x=350, y=550)
        self.aubtn = Button(win, text="Download", fg='black', bg='white', font=('arial', 15, 'bold'),
                            command=self.AudioDownload)
        # self.combo = Combobox(root, values=list(materialDict.keys()))
        # self.combo.bind('<<ComboboxSelected>>',
        #                     lambda event: label_selected.config(text=materialDict[var_material.get()]))
        self.aubtn.place(x=400, y=590)
        self.qualityaulabel = Label(win, text="Select Your Audio Quality to Download", font=('arial', 15, 'bold'))
        self.qualityaulabel.place(x=590, y=510)
        self.audio = ttk.Combobox(values=list(audicombobox_keys),
                                  font=('arial', 15, 'bold'), width=5)
        self.audio.place(x=680, y=550)

    def Downloader(self):
        url = YouTube(str(self.e1.get()))
        """You Can Change the get_by_itag option to your own choice to change the video quality"""
        videoget = self.quality.get()
        videotag = dictionary[videoget]
        video = url.streams.get_by_itag(videotag)
        video.download()
        window.destroy()

    def PlaylistDownload(self):
        pl = Playlist(str(self.e2.get()))
        videoget = self.qualitypl.get()
        videotag = dictionary[videoget]
        video = url.streams.get_by_itag(videotag)
        for video in pl.videos:
            video.download()
        window.destroy()

    def AudioDownload(self):
        au = YouTube(str(self.e3.get()))
        audioget = self.audio.get()
        audiotag = audiodictionary[audioget]
        audio = au.streams.get_by_itag(audiotag)
        audio.download()
        window.destroy()


dictionary = {'360p': 18,
              '720p': 22}
combobox_keys = dictionary.keys()
combobox_values = dictionary.values()

audiodictionary = {'50kbps': 249,
                   '70kbps': 250,
                   '128kbps': 140,
                   '160kbps': 251}
audicombobox_keys = audiodictionary.keys()

window = tk.Tk()
mywin = mywindow(window)
window.geometry("1000x1000")
window.title("Youtube Video Downloader")
# window.configure(background='white')
img = PhotoImage(file='youtube.png')
l1 = tk.Label(window, image=img).pack(side="top")
window.mainloop()
