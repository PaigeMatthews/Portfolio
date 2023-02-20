from tkinter import *
import calendar

def showCalendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font="Latos 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()

if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calender")
    new.geometry("250x140")