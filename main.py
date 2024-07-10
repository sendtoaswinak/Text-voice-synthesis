from tkinter import *
from gtts import gTTS
import pygame

root = Tk()
root.geometry('500x300')
root.resizable(10,10)
root.config(bg = '#CAFF70')
root.title('T2VS')
root.iconbitmap("bitmap.ico")

Label(root, text = 'TEXT TO VOICE SYNTHESIS' , font='Verdana 20 bold' , bg ='white smoke').place(x=30,y=30)
Label(root, text ='GUI' , font ='Verdana 15 bold', bg = 'white smoke').place(x=200,y=230)
Label(root, text ='Enter Text', font ='Verdana 15 bold', bg ='white smoke').place(x=30,y=80)

Msg = StringVar()

entry_field = Entry(root, textvariable=Msg,width= 100)
entry_field.place(x=30, y=120)

pygame.mixer.init()
def Text_to_voice():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('Audio.mp3')
    pygame.mixer.music.load('Audio.mp3')
    pygame.mixer.music.play()
def Exit():
    root.destroy()
def Reset():
    Msg.set("")

Button(root, text = "PLAY", font = 'Verdana 15 bold', command = Text_to_voice, width = 4).place(x=30, y=150)
Button(root, text = "EXIT", font = 'Verdana 15 bold', command = Exit, bg = 'OrangeRed1').place(x=100, y=150)
Button(root, text = "RESET", font = 'Verdana 15 bold', command = Reset).place(x=189, y=150)

root.mainloop()

