from tkinter import *
import main as m
import random

class Main_window():
    def __init__(self,master):
        self.master = master
        self.master.configure(bg="slate gray")
        self.master.title("Public/ Private Key Share")
        self.master.option_add("*Font","Courier 12")
        self.master.option_add("*background","slate gray")
        self.master.geometry("625x450+100+100")
        self.master.resizable(width=False, height=True)
        self.master.iconbitmap('key-icon2.ico')
        self.encrypt = IntVar()
        self.img_index = 0
        self.lizard_show = False
        self.lizard = IntVar()
        
        main_frame = Frame(self.master)
        main_frame.grid()
        gif_frame = Frame(self.master)
        gif_frame.grid()
        
        lbl_encrypt = Label(main_frame)
        lbl_encrypt.config(text = "Encrypt",font=("Courier", 18), fg = "white smoke")
        lbl_encrypt.grid(row=0, column=0, columnspan = 3, sticky = 'w', padx = 10)
        
        lbl_decrypt=Label(main_frame)
        lbl_decrypt.config(text = "Decrypt",font=("Courier", 18), fg = "white smoke")
        lbl_decrypt.grid(row=0, column=4, columnspan = 3, sticky = 'e', padx = 10)

        self.txt_box_encrypt = Text(main_frame)
        self.txt_box_encrypt.config( width = 20, height = 15, bg = "light slate gray", fg = "mint cream")
        self.txt_box_encrypt.grid(row = 1, column = 0, columnspan = 2, sticky = 'w', padx = 10)

        btn_enter = Button(main_frame)
        btn_enter.config(text = "Encrypt/Decrypt", borderwidth = 2,fg = "white smoke", height = 5)
        btn_enter.grid(row = 1, column = 3, columnspan = 2, sticky = 'n', padx = 5)
        btn_enter.bind("<Button-1>",self.enter_button)

        btn_lizard = Button(main_frame)
        btn_lizard.config(text = "Lizard?", borderwidth = 2,fg = "white smoke", height = 2)
        btn_lizard.grid(row = 1, column = 3, columnspan = 2, sticky = 's', padx = 5)
        btn_lizard.bind("<Button-1>",self.release_lizard)

        self.txt_box_decrypt = Text(main_frame)
        self.txt_box_decrypt.config( width = 20, height = 15, bg = "light slate gray", fg = "mint cream")
        self.txt_box_decrypt.grid(row = 1, column = 5, columnspan = 2, sticky = 'e', padx = 10)

        self.radio_encrypt = Radiobutton(main_frame)
        self.radio_encrypt.config(fg = "black", variable = self.encrypt, value = 1)
        self.radio_encrypt.grid(row = 2, column = 0, sticky = 'w')
        self.radio_encrypt.deselect()

        lbl_radio_encrypt = Label(main_frame)
        lbl_radio_encrypt.config(text = "Encrypt",font=("Courier", 13), fg = "white smoke")
        lbl_radio_encrypt.grid(row = 2, column = 0, padx = 20)

        lbl_new_machine = Label(main_frame)
        lbl_new_machine.config(text = "Make New Machine\nName:",font=("Courier", 13), fg = "white smoke")
        lbl_new_machine.grid(row = 2, column=3, columnspan = 2, sticky = 'n')

        self.radio_decrypt = Radiobutton(main_frame)
        self.radio_decrypt.config(fg = "black", variable = self.encrypt, value = 0)
        self.radio_decrypt.grid(row = 2, column = 6, sticky = 'e')
        self.radio_decrypt.deselect()

        lbl_radio_decrypt = Label(main_frame)
        lbl_radio_decrypt.config(text = "Decrypt",font=("Courier", 13), fg = "white smoke")
        lbl_radio_decrypt.grid(row = 2, column = 6, sticky = 'w', padx = 15)
        
        lbl_from_machine = Label(main_frame)
        lbl_from_machine.config(text = "From machine:",font=("Courier", 12), fg = "white smoke")
        lbl_from_machine.grid(row = 3, column = 0, columnspan = 2, sticky = 'w')

        self.txt_box_generate_machine = Entry(main_frame)
        self.txt_box_generate_machine.config(width = 10, bg = "light slate gray", fg = "mint cream")
        self.txt_box_generate_machine.grid(row = 3, column = 3, columnspan = 2 , sticky = 'e'+'w', pady = 10)

        lbl_to_machine = Label(main_frame)
        lbl_to_machine.config(text = "To machine:",font=("Courier", 12), fg = "white smoke")
        lbl_to_machine.grid(row = 3, column = 5, columnspan = 2 , sticky = 'w', padx = 20)

        lbl_name_1 = Label(main_frame)
        lbl_name_1.config(text = "Name:",font=("Courier", 10), fg = "white smoke")
        lbl_name_1.grid(row = 4, column = 0 , sticky = 'w')

        self.txt_box_to_machine = Entry(main_frame)
        self.txt_box_to_machine.config(width = 10, bg = "light slate gray", fg = "mint cream")
        self.txt_box_to_machine.grid(row = 4, column = 1, sticky = 'w')

        btn_generate = Button(main_frame)
        btn_generate.config(text = "Generate", borderwidth = 2,fg = "white smoke")
        btn_generate.grid(row = 4, column = 2, columnspan = 2, sticky ='e', padx = 35, pady = 10)
        btn_generate.bind("<Button-1>",self.get_new_name)

        lbl_name_2 = Label(main_frame)
        lbl_name_2.config(text = "Name:",font=("Courier", 10), fg = "white smoke")
        lbl_name_2.grid(row = 4, column = 5 , sticky = 'w', padx = 20)

        self.txt_box_from_machine = Entry(main_frame)
        self.txt_box_from_machine.config(width = 10, bg = "light slate gray", fg = "mint cream")
        self.txt_box_from_machine.grid(row = 4, column = 6, sticky = 'w')

        self.btn_rave = Button(main_frame)
        self.btn_rave.config(text = "Rave!",fg = "#%06x" % random.randint(0, 0xFFFFFF), font = ("Comic Sans MS bold", 12),activeforeground = "white", activebackground= "#%06x" % random.randint(0, 0xFFFFFF), width = 10, height = 2)
        self.btn_rave.grid(row = 5, column = 2, columnspan = 2, sticky ='e', padx = 35, pady = 10)
        self.btn_rave.bind("<Button-1>",self.rave)

        self.img_gif = PhotoImage(file = "lizard.gif", format = "gif -index 0")
        self.img_lbl = Label(gif_frame)
        self.img_lbl.config(image = self.img_gif)

    def release_lizard(self,event):
        self.lizard = 1   
        

    def animate_gif(self,master):
            try:
                self.img_gif = PhotoImage(file = "lizard.gif", format = "gif -index {}".format(self.img_index))
                self.img_lbl.config(image = self.img_gif)
                self.img_lbl.grid(row = 0, column = 0, sticky ='s')
                self.img_index +=1
            except:
                self.img_index = 0
            master.after(10,self.animate_gif, master)

    def rave(self,event):        
        self.btn_rave.config(activebackground= "#%06x" % random.randint(0, 0xFFFFFF), fg = "#%06x" % random.randint(0, 0xFFFFFF))               
                              
    def enter_button(self,event):
        plaintext = self.txt_box_encrypt.get("1.0","end-1c")
        ciphertext = self.txt_box_decrypt.get("1.0","end-1c")
        machine_1 = self.txt_box_to_machine.get()
        machine_2 = self.txt_box_from_machine.get()
        self.txt_box_encrypt.delete("1.0","end")
        self.txt_box_decrypt.delete("1.0","end")
        self.txt_box_to_machine.delete("0","end")
        self.txt_box_from_machine.delete("0","end")
        self.encrypt.get()
        
    def get_new_name(self,event):
        txt_box_get = self.txt_box_generate_machine.get()
        self.txt_box_generate_machine.delete("0","end")
        print(m.generate_machine(txt_box_get).return_public_key())   
        

def main():
    root = Tk()
    encryption_app = Main_window(root)
    encryption_app.animate_gif(root)
    root.mainloop()
main()