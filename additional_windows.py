from tkinter import *


class Collector:

    submit_allowed = False
    start_x = 0
    start_y = 0
    end_x = 10
    end_y = 8
    different_start_end = True


    def submit(self):
        if not (self.start_x_entry.get() == "" or self.start_y_entry.get() == "" or self.end_x_entry.get() == "" or self.end_y_entry.get() == ""):
            if int(self.start_x_entry.get()) > 79:
                self.start_x = 79
            else:
                self.start_x = int(self.start_x_entry.get())
            if int(self.start_y_entry.get()) > 59:
                self.start_y = 59
            else:
                self.start_y = int(self.start_y_entry.get())
            if int(self.end_x_entry.get()) > 79:
                self.end_x = 79
            else:
                self.end_x = int(self.end_x_entry.get())
            if int(self.end_y_entry.get()) > 59:
                self.end_y = 59
            else:
                self.end_y = int(self.end_y_entry.get())
            if self.start_x != self.end_x or self.start_y != self.end_y:
                self.master.destroy()
            else:
                self.warning_label.config(text="start and end must be different", fg="red")
        else:
            self.warning_label.config(text="all four fields must be filled", fg="red")

    def __init__(self):

        self.master = Tk()
        self.master.maxsize(width=180, height=150)

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

        self.warning_label = Label(master=self.master, text="")
        self.warning_label.place(x=5, y=80)

        submit_button = Button(master=self.master, text="Submit", command=self.submit)
        submit_button.place(x=80, y=100)

        self.master.mainloop()


class InstanceManager:

    new_game = False

    def __init__(self):
        self.master = Tk()
        self.master.maxsize(width=150, height=60)

        new_map_button = Button(master=self.master, text="Create new Map", command=self.set_new_game_true)
        new_map_button.place(x=10, y=10)
        exit_button = Button(master=self.master, text="Exit", command=self.set_new_game_false)
        exit_button.place(x=110, y=10)

        self.master.mainloop()

    def set_new_game_true(self):
        self.new_game = True
        self.master.destroy()

    def set_new_game_false(self):
        self.new_game = False
        self.master.destroy()
