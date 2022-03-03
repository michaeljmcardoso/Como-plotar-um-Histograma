from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("<Youtube_Video_Downloader>")

Label(root,text = 'Baixador de Vídeos do Youtube', font ='arial 20 bold').pack()

##enter link
link =  StringVar()

Label(root, text = 'Cole o Link Aqui:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 55,textvariable = link).place(x = 32, y = 90)

#function to download video

def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'ARQUIVO BAIXADO', font = 'arial 15').place(x= 180 , y = 210)

Button(root,text = 'BAIXAR', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=200 ,y = 150)

root.mainloop()
