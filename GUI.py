<<<<<<< Updated upstream
import database
import main
import Tkinter.tk
=======
#import database
#import main
import tkinter as tk
from tkinter import *
import os







def fil_fjernet():
    print("Filen er fjernet")




def matcher_ikke():
    global screen4
    screen4 = Toplevel(screen1)
    screen4.title("Mismatch")
    screen4.geometry("200x50")
    Label(screen4, text="Fornavn og efternavn matcher ikke").pack()
    Button(screen4, text="OK", command=screen4.destroy).pack()






def fjern_vertify():
    fornavn1 = fornavn_vertify.get()
    efternavn1 = efternavn_vertify.get()
    fornavn_entry2.delete(0, END)
    efternavn_entry2.delete(0, END)

    list_of_files = os.listdir()
    if fornavn1 in list_of_files:
        file1 = open(fornavn1, "r")
        vertify = file1.read().splitlines()
        if efternavn1 in vertify:
            fil_fjernet()
        else:
            matcher_ikke()
    else:
        matcher_ikke()






def fjern_tid():
    global screen3
    screen3 = Toplevel(screen1)
    screen3.title("Fjern tid")
    screen3.geometry("350x300")
    Label(screen3, text="Fjern existerende tid", bg="grey", fg="white", width="30", height="2", font=("Calibri", 13)).pack()
    Label(screen3, text="Hvem skal fjernes?", width="30", height="2").pack()

    global fornavn_vertify
    global efternavn_vertify

    fornavn_vertify = StringVar()
    efternavn_vertify = StringVar()

    global fornavn_entry2
    global efternavn_entry2

    Label(screen3, text="Navn * ").pack()
    fornavn_entry2 = Entry(screen3, textvariable=fornavn_vertify)
    fornavn_entry2.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Efternavn * ").pack()
    efternavn_entry2 = Entry(screen3, textvariable=efternavn_vertify)
    efternavn_entry2.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Fjern", width="10", height="1", command=fjern_vertify).pack()

def register_booktid():
    fornavn_info = fornavn.get()
    efternavn_info = efternavn.get()
    tid_info = tid.get()

    file = open(fornavn_info, "w")
    file.write(fornavn_info + "\n")
    file.write(efternavn_info + "\n")
    file.write(tid_info)
    file.close()

    fornavn_entry1.delete(0, END)
    efternavn_entry1.delete(0, END)
    tid_entry1.delete(0, END)

    Label(screen2, screen6, text="Booking sucessful", fg="green", font=("calibri", 11)).pack()

def rediger_åbent():
    global screen6
    screen6 = Toplevel(screen1)
    screen6.geometry("350x300")

    global fornavn
    global efternavn
    global tid
    global fornavn_entry1
    global efternavn_entry1
    global tid_entry1
    fornavn = StringVar()
    efternavn = StringVar()
    tid = StringVar()

    Label(screen6, text="Rediger din tid", bg="grey", fg="white", width="30", height="2", font=("Calibri", 13)).pack()
    Label(screen6, text="Udfyld information, for at redigere din tid", width="30", height="2").pack()
    Label(screen6, text="").pack()

    Label(screen6, text="Nyt Fornavn * ").pack()
    fornavn_entry1 = Entry(screen6, textvariable=fornavn)
    fornavn_entry1.pack()

    Label(screen6, text="Nyt Efternavn * ").pack()
    efternavn_entry1 = Entry(screen6, textvariable=efternavn)
    efternavn_entry1.pack()

    Label(screen6, text="Nyt Tidspunkt * ").pack()
    Label(screen6, text="Fx. 13/1/2020/12:30").pack()
    tid_entry1 = Entry(screen6, textvariable=tid)
    tid_entry1.pack()

    Button(screen6, text="Book tid", width="10", height="1", command=register_booktid).pack()





def rediger_vertify():
    fornavn1 = fornavn_vertify.get()
    efternavn1 = efternavn_vertify.get()
    fornavn_entry2.delete(0, END)
    efternavn_entry2.delete(0, END)

    list_of_files = os.listdir()
    if fornavn1 in list_of_files:
        file1 = open(fornavn1, "r")
        vertify = file1.read().splitlines()
        if efternavn1 in vertify:
            rediger_åbent(), fil_fjernet()
        else:
            matcher_ikke()
    else:
        matcher_ikke()






def redigere_booking():
    global screen5
    screen5 = Toplevel(screen1)
    screen5.geometry("350x300")
    Label(screen5, text="Rediger existerende tid", bg="grey", fg="white", width="30", height="2", font=("Calibri", 13)).pack()
    Label(screen5, text="Hvem skal redigeres?", width="30", height="2").pack()


    global fornavn_vertify
    global efternavn_vertify

    fornavn_vertify = StringVar()
    efternavn_vertify = StringVar()

    global fornavn_entry2
    global efternavn_entry2

    Label(screen5, text="Navn * ").pack()
    fornavn_entry2 = Entry(screen5, textvariable=fornavn_vertify)
    fornavn_entry2.pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Efternavn * ").pack()
    efternavn_entry2 = Entry(screen5, textvariable=efternavn_vertify)
    efternavn_entry2.pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Rediger", width="10", height="1", command=rediger_vertify).pack()






def BookTid():
    global screen2
    screen2 = Toplevel(screen1)
    screen2.title=("Book en Tid")
    screen2.geometry("350x300")

    global fornavn
    global efternavn
    global tid
    global fornavn_entry1
    global efternavn_entry1
    global tid_entry1
    fornavn = StringVar()
    efternavn = StringVar()
    tid = StringVar()

    Label(screen2, text="Book din tid", bg="grey", fg="white", width="30", height="2", font=("Calibri", 13)).pack()
    Label(screen2, text="Udfyld information, for at book din tid", width="30", height="2").pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Fornavn * ").pack()
    fornavn_entry1 = Entry(screen2, textvariable=fornavn)
    fornavn_entry1.pack()

    Label(screen2, text="Efternavn * ").pack()
    efternavn_entry1 = Entry(screen2, textvariable=efternavn)
    efternavn_entry1.pack()

    Label(screen2, text="Tidspunkt * ").pack()
    Label(screen2, text="Fx. 13/1/2020/12:30").pack()
    tid_entry1 = Entry(screen2, textvariable=tid)
    tid_entry1.pack()

    Button(screen2, text="Book tid", width="10", height="1", command=register_booktid).pack()





def main_screen():
    global screen1
    screen1 = Tk()
    screen1.title("Booking System")
    screen1.geometry("350x300")
    Label(text="Booking System", bg="grey", fg="white", width="30", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Book en tid", height="2", width="30", command=BookTid).pack()
    Label(text="").pack()
    Button(text="Rediger en tid", height="2", width=30, command=redigere_booking).pack()
    Label(text="").pack()
    Button(text="Fjern en tid", height="2", width=30, command=fjern_tid).pack()
    Label(text="").pack()

    screen1.mainloop()

main_screen()







>>>>>>> Stashed changes
