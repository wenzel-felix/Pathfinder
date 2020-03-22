from tkinter import *


class Collector:

    submit_allowed = False
    start_x = 0
    start_y = 0
    end_x = 10
    end_y = 8

    master = Tk()

    def submit(self):
        if int(self.start_x_entry.get()) > 99:
            self.start_x = 99
        else:
            self.start_x = int(self.start_x_entry.get())
        if int(self.start_y_entry.get()) > 79:
            self.start_y = 79
        else:
            self.start_y = int(self.start_y_entry.get())
        if int(self.end_x_entry.get()) > 99:
            self.end_x = 99
        else:
            self.end_x = int(self.end_x_entry.get())
        if int(self.end_y_entry.get()) > 79:
            self.end_y = 79
        else:
            self.end_y = int(self.end_y_entry.get())
        self.master.destroy()


    def __init__(self):
        # labels for start
        start_main_label = Label(master=self.master, text="Set your starting point")
        start_main_label.place(x=0, y=0)

        start_x_label = Label(master=self.master, text="X:")
        start_x_label.place(x=0, y=20)
        self.start_x_entry = Entry(master=self.master, width=8)
        self.start_x_entry.place(x=25, y=20)

        start_y_label = Label(master=self.master, text="Y:")
        start_y_label.place(x=75, y=20)
        self.start_y_entry = Entry(master=self.master, width=8)
        self.start_y_entry.place(x=100, y=20)

        # labels for end
        end_main_label = Label(master=self.master, text="Set your target point")
        end_main_label.place(x=0, y=40)

        end_x_label = Label(master=self.master, text="X:")
        end_x_label.place(x=0, y=60)
        self.end_x_entry = Entry(master=self.master, width=8)
        self.end_x_entry.place(x=25, y=60)

        end_y_label = Label(master=self.master, text="Y:")
        end_y_label.place(x=75, y=60)
        self.end_y_entry = Entry(master=self.master, width=8)
        self.end_y_entry.place(x=100, y=60)

        submit_button = Button(master=self.master, text="Submit", command=self.submit)
        submit_button.place(x=20, y=80)

        self.master.mainloop()
