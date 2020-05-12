import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
import time

import tkinter.scrolledtext as scrolledtext

deviceList=[]
flag=1


def refresh():
    deviceList=[]
    list_dev()

def checkdata():
    flag=1
    if(txt2.get()==""):
        lblch.configure(text="Choose a device name",fg="black",bg="#006064",font=('ubuntu',10,"bold"))
        lblch.place(x=250, y=220)
        flag=0
    if(form.get()==""):
            formatch.configure(text="Choose a format",fg="black",bg="#006064",font=('ubuntu',10,"bold"))
            formatch.place(x=250, y=300)
            flag=0
    if(myCombo.get()==""):
                devch.configure(text="Choose a Device",fg="black",bg="#006064",font=('ubuntu',10,"bold"))
                devch.place(x=250, y=150)
                flag=0
    #if flag==1:
    redirect2()







def redirect2():
    MsgBox = tk.messagebox.askquestion('Format', 'Are you sure you want to format \n Formatting will erase all data',
                                       icon='warning')
    if MsgBox == 'yes':
        f()
    else:
        tk.messagebox.showinfo('Aborting...', 'Format has been aborted')



def list_dev():

    stream = os.popen('lsblk | grep /media | grep -oP "sd[a-z][0-9]?" | awk \'{print "/dev/"$1}\'')
    res = stream.read()
    #txt.insert('insert', res + "")


    stream = os.popen('lsblk | grep /media | grep -oP "[A-z]*[0-9]*?$"')
    res = stream.read()
    #txt.insert('insert', "Volume Label \t\t:\t" + res + "")
    deviceList.append(res)

    stream = os.popen('lsblk | grep /media | grep -oP "[0-9]*[.]*[0-9]*?G"')
    res = stream.read()
    #txt.insert('insert', "Usable Size \t\t: \t" + res + "")

    stream = os.popen('lsblk | grep /media | grep -oP "/[A-z]*/[A-z]*/[A-z]*[0- 9]*?$"')
    res = stream.read()
    #txt.insert('insert', "Mount Point \t\t: \t" + res + "\n")



list_dev()

window = tk.Tk()
window.title("USB Format")
window.geometry('500x500')
C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file="blackk.png")
background_label = Label(window, bg="#006064")
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
# window.attributes('-fullscreen', True)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


photo=PhotoImage(file="mult.png")
window.iconphoto(False,photo)

s=ttk.Style()
s.configure('Kim.TButton',foregroud="white",background="white",font=('Ubuntu', 10))
s.configure('X.TLabel',foreground="white",background="#006064",font=('Ubuntu',12))
s.configure('C.TEntry')
s.configure('Warn.TLabel',foregroud="red",backgroud="#212121")

img1=PhotoImage(file="disk.png")

message1 = tk.Label(window, text="Disk Format",image=img1,height=35,width=180)
message1.place(x=150, y=23)


img2=PhotoImage(file="drive.png")
lbl = tk.Label(window, text="Drive",image=img2,width=39,height=20)
lbl.place(x=120, y=130)

chdev=tk.StringVar()
chdev.set(deviceList)

devopt=tk.OptionMenu(window,chdev, *deviceList)
devopt.config(width=25, font=('Helvetica', 12), bg="#212121", )
#devopt.place(x=250,y=130)
chdev.set("Choose Drive")

myCombo=ttk.Combobox(window,value=deviceList,font = ('courier', 11, 'bold'))
myCombo.current(0)
myCombo.place(x=250,y=130)

devch=tk.Label(window)


img3=PhotoImage(file="label.png")
lbl2 = tk.Label(window, text="New Volume Label", width=190,height=36,fg="white",bg="#006064",image=img3)
lbl2.place(x=45, y=192)

refr=PhotoImage(file="refresh.png")
ref=tk.Button(window,image=refr,command=refresh)
ref.place(x=450,y=127)

txt2 = ttk.Entry(window, width=21, justify = CENTER,font = ('mincho', 11, 'bold'))
txt2.place(x=250, y=200)

lblch=tk.Label(window)

img4=PhotoImage(file="format.png")

lb2 = tk.Label(window, text="  File System Format", width=150, height=25, fg="white", bg="#006064",image=img4)
lb2.place(x=60, y=270)

OptionList = ["","FAT32", "NTFS" ]
variable = tk.StringVar(window)
variable.set(OptionList[0])

opt = tk.OptionMenu(window, variable, *OptionList)
opt.config(width=25, font=('Helvetica', 12), bg="white", )
#opt.place(x=250, y=270)


form=ttk.Combobox(window,value=OptionList,font = ('courier', 11, 'bold'))
form.current(0)
form.place(x=250,y=270)


formatch=tk.Label(window)



def f():
    dev = (chdev.get())
    dev_name = (txt2.get())
    file_sys = (variable.get())
    '''
    if file_sys == 'FAT32':
        fs = 'vfat'
    else:
        fs = 'ntfs'
    req_string = 'sudo umount ' + dev
    stream = os.popen(req_string)
    res = stream.read()
    txt.insert('insert', res + "\n")
    req_string2 = 'sudo mkfs.' + fs + ' -n ' + dev_name + ' ' + dev
    stream = os.popen(req_string2)
    res = stream.read()
    txt.insert('insert', res + "\n")
    '''

    progress.place(x=10, y=470)
    bar()
    time.sleep(2)
    tk.messagebox.showinfo('Formatted', 'Device Format Complete')


def quit():
    dialog_title = 'QUIT'
    dialog_text = 'Are you sure?'
    answer = messagebox.askyesno(dialog_title, dialog_text)
    if answer == TRUE:
        window.destroy()

txt = scrolledtext.ScrolledText(window, undo=True, bg="#212121", fg="white", width=60, height=8,
                                    font=('Monospaced', 12, ' '))
#txt.place(x=10, y=285)




listbutton = tk.Button(window, text="List Devices", command=list_dev)
#listbutton.place(x=150, y=420)

img5=PhotoImage(file="formatf.png")
formatbutton = tk.Button(window, text="Format", command=checkdata,bg="#263238",image=img5)
formatbutton.place(x=130, y=360)


progress = ttk.Progressbar(window,length=480,mode='determinate')



def bar():

    progress['value'] = 20
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    window.update_idletasks()
    time.sleep(1)
    progress['value'] = 100




q=PhotoImage(file="quit.png")
quit=tk.Button(window,image=q,command=quit,bg="red")
quit.place(x=330,y=360)

window.mainloop()

