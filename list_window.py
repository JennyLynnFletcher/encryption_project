class Sub_window():
    def __init__(self,master):
        self.master = master
        self.master.configure(bg="slate gray")
        self.master.title("Machine List")
        self.master.option_add("*Font","Courier 12")
        self.master.option_add("*background","slate gray")
        self.master.geometry("625x450+50+50")
        self.master.resizable(width=False, height=False)
        self.master.iconbitmap("key-icon2.ico")
        
