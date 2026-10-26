from tkinter import *
import instaloader
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

def get_image():
    l = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(l.context, f"{username.get()}")
    a = urlopen(profile.get_profile_pic_url())
    deta = a.read()
    a.close
    img = Image.open(io.BytesIO(deta))
    pic = ImageTk.PhotoImage(img)
    Label.config(image=pic)
    Label.image = pic
    Label.pack()    
window = Tk()

window.title("instagram profile dwonloader")

window.geometry("600x600")

Label(window, text="enter insta username").pack()


username = Entry(window,width=50)
username.pack()

botton = Button(window,text="start download")
botton.pack()
botton.config(command=get_image)
Label = Label(window)

window.mainloop()