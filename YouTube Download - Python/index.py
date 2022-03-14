from tkinter import *
from tkinter import ttk
from pytube import YouTube

root = Tk()
root.title("ACESSO")
root.geometry("500x130")
root.attributes('-alpha', 0.9)
root.resizable(width=False, height=False)
root.iconbitmap(default='icon/youtube.ico')

frame = Frame(root, width=500, height=300, bg='black', relief="raise")
frame.pack(side=TOP)

textLabel = Label(root, text='Download de vídeos do YouTube', bg='black', font=('Calibri', 12), fg='white')
textLabel.place(x=135, y=10)

usuarioLabel = Label(root, text='URL:', bg='black', font=('Calibri', 12), fg='white')
usuarioLabel.place(x=15, y=40)
usuarioEntry = ttk.Entry(root, width=68)
usuarioEntry.place(x=60, y=43)

def baixar():    
    url = usuarioEntry.get()
    youtube = YouTube(url)

    youtube.streams.get_highest_resolution().download()

    sinalLabel = Label(root, text='Complete...', bg='black', font=('Calibri', 12), fg='white')
    sinalLabel.place(x=2, y=105)

enviaButton = ttk.Button(root, text='BAIXAR', command=baixar)
enviaButton.place(x=210, y=80)

root.mainloop()