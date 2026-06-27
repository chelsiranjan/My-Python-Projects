from tkinter import *
from tkinter import ttk
import yt_dlp
import os

root = Tk()
root.geometry('500x320')
root.title('YouTube Video Downloader')
root.resizable(False, False)

Label(root,text='YouTube Video Downloader',fg ="#13090D",font=('Arial', 19, 'bold')).pack(pady=15)

link = StringVar()

Label(root,text='Paste Link Here:',fg ="#70183D",font=('Arial', 14, 'bold')).pack()

Entry(root,width=60,textvariable=link).pack(pady=10)

Label(root,text='Select Quality:',fg ="#70183D",font=('Arial', 12, 'bold')).pack()

quality = StringVar()
quality.set('Best')

quality_menu = ttk.Combobox(root,textvariable=quality,values=['Best', '1080p', '720p', '480p', 'Audio Only'],state='readonly')
quality_menu.pack(pady=5)

status = Label(root,text='',font=('Arial', 10))
status.pack()


def download_video():
    try:
        downloads_folder = os.path.join(os.path.expanduser('~'),'Downloads')

        selected_quality = quality.get()

        if selected_quality == 'Best':
            fmt = 'best'

        elif selected_quality == '1080p':
            fmt = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
        # this is not working it is giving error for any video since i did not know how to fix it now bcos it is too advanced right now i feel for me to fix
        # but ill definately going to fix it whenever ill learn or study about that concept which im not getting right now

        
        elif selected_quality == '720p':
            fmt = 'bestvideo[height<=720]+bestaudio/best[height<=720]'

        elif selected_quality == '480p':
            fmt = 'bestvideo[height<=480]+bestaudio/best[height<=480]'

        elif selected_quality == 'Audio Only':
            fmt = 'bestaudio'

        ydl_opts = {'format': fmt,'outtmpl': os.path.join(downloads_folder,'%(title)s.%(ext)s'),}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link.get()])

        status.config(text='Downloaded Successfully!')

    except Exception as e:
        status.config(text=f'Error: {e}')


Button(root,text='DOWNLOAD',bg='pale violet red',font=('Arial', 15, 'bold'),command=download_video).pack(pady=20)

root.mainloop()