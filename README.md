# Youtube-Video-Downloader

This is a Python Program to download Youtube videos with the link of that video.

FEATURES-:
1. Version 1 i.e youtubedownloader.py download videos at the highest quality available on youtube(not higher than 1080p) whereas Version 2 i.e youtubedownloader_V2.py can download videos at two qualities, 360p and 720p, you have to choose what you want.
2. This program can also download a whole playlist from youtube with just the link of the playlist, given the playlist should be public.
3. It can also perform AUDIO-ONLY DOWNLOAD at its highest quality on Version 1 and of your choice on Verion 2.

This program is created using a module called pytube which is a free library for downloading Youtube Videos.
You Can find more info about it here-:
https://pypi.org/project/pytube/.

HOW TO INSTALL THE PROGRAM

1. git clone https://github.com/NoisyBotDude/Youtube-Video-Downloader.git

Use the above command in a Linux Terminal or Windos Subsystem for Linux to download the directory of the program

Make sure you have git installed in your system before proceeding with the above step.
If not follow this link to instal git in your system-:
https://github.com/git-guides/install-git

2. After downloading, head to the directory, which should be named Youtube-Video-Downloader
3. After reaching the directory, you will find a python program named youtubedownloader.py and youtubedownloader_V2.py
4. Run the program with the command-: python3 youtubedownloader.py or python3 youtubedownloader_V2.py

SOME THINGS TO REMEMBER
1. This program may not work with every version of pytube, so install pytube from pip with this command-:  python -m pip install git+https://github.com/nficano/pytube
2. Also, this program also needs TKINTER installed to work.
3. If you try to download only the audio, it gets downloaded in mp4 format not in mp3.
4. Version 2 is having an error on some of the youtube videos where only video is downloaded and not audio. Even though this error is not common, it normally happens on older videos with low quality on youtube.
