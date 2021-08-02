from tkinter import *
win1 = Tk()
win1.title('Schedule') #title
win1.geometry('800x800') #size
win1.resizable(False,False) #win1 -> not resizable

#win2 = Tk()
#win2.title('test')
#win2.geometry('400x400')
#win2.resizable(True, False) #win2 -> resizable

t1 = Text(win1, height = 10)
t1.insert(CURRENT, 'Arrange your schedule')
t1.pack()
t1.configure(font=('Times New Roman', 16, 'italic'))
t2 = Text(win1, height = 5)
t2.insert(CURRENT, 'Please input your schedule')
t2.pack()
t2.configure(font=('Arial', 14))

sv1 = StringVar()
sitemlabel = Label(win1, font = ('Arial',14),width = 5, height = 5, fg = 'green', relief = 'groove')
vitemlabel = Label(win1, textvariable=sv1, font = ('Arial',12),width = 5, height = 5, fg = 'green', relief = 'solid')
sitemlabel['text'] = 'Item'
sv1.set('Molly')
stimelabel = Label(win1, text = 'Time', font = ('Arial',14),width = 5, height = 5, fg = 'green', relief = 'groove')

sitemlabel.pack()
vitemlabel.pack()
stimelabel.pack()

win1.mainloop() # to prevent closing the windows without any input