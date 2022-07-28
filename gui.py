from tkinter import *
window=Tk()
# add widgets here

btn = Button(window, text="This is Button", fg="blue", )
btn.place(x=80, y=100, )
window.title('Hello Python')
window.geometry("1000x1000+10+20")
window.mainloop()