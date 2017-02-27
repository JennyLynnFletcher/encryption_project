from tkinter import *
import machine_class as mc

class Sub_window():
    def __init__(self,master,text):
        self.master = master
        self.master.configure(bg="slate gray")
        self.master.title("Machine List")
        self.master.option_add("*Font","Courier 12")
        self.master.option_add("*background","slate gray")
        self.master.geometry("625x437+50+50")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("key-icon2.ico")
        self.machine_list = text
        self.name_list = []
        self.list = ""

        main_frame = Frame(self.master)
        main_frame.grid()

        self.txt_box_list = Text(main_frame)
        self.txt_box_list.config(state = "normal", width = 60, height = 24, bg = "light slate gray", fg = "mint cream", wrap = "word")
        self.txt_box_list.grid(row = 0, column = 0)

        self.scroll_bar_list = Scrollbar(main_frame)
        self.scroll_bar_list.config(command = self.txt_box_list.yview)
        self.scroll_bar_list.grid(row = 0, column = 1, sticky = 'ns')
        self.txt_box_list['yscrollcommand'] = self.scroll_bar_list.set

        self.name_list = list(self.machine_list.keys())

        for i in range(len(self.machine_list)):
            print(self.name_list[i])
            self.list += self.name_list[i]
            self.list += " "
            self.list += str(self.machine_list[self.name_list[i]].return_public_key())
            self.list += "\n"
          
        self.txt_box_list.insert(0.0,self.list)
        self.txt_box_list.config(state = "disabled")

            
        
