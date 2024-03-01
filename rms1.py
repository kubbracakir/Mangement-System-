from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from datetime import datetime
import os

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win = win
        #self.win.geometry("1350*750+0+0")
        self.win.title("Restaurant Management System")

        self.title_label= Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="black",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)

        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="black",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="black",font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=True)

        self.entus_lbl = Label(self.entry_frame,text="Enter Username: ",bg="black",font=('sans-serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)

    ##### Variables ######
        
        username = StringVar()
        password = StringVar()


        self.entus_ent  = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)

        self.entpass_lbl = Label(self.entry_frame,text="Enter Password: ",bg="black",font=('sans-serif',15))
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)


        self.entpass_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=password,show="*")
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)

        ########### Function ###########

        def check_login():
            ''' This Function Will Check Login ''' 
            if username.get() == "" and password.get() == "":
                self.billing_btn.config(state="normal")
            else:
                pass

        def reset():
            username.set("")
            password.set("")

        def billing_sect():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)


        self.button_frame = LabelFrame(self.entry_frame,text="Options",font=('Arial',15),bg="black",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)

        self.login_btn = Button(self.button_frame,text="Login",font=('Arial',15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn = Button(self.button_frame,text="Billing",font=('Arial',15),bd=5,width=15,command=billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)



class Window2:
    def __init__(self,win):
        self.win = win
        #self.win.geometry("1350*750+0+0")
        self.win.title("Restaurant Management System")

        self.title_label= Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="black",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        #self.win.resizable(0,0)

        ######### Variables ##########
        bill_no = random.randint(100,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        calc_var = StringVar()

        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cone = StringVar()

        date_pr.set(datetime.now())




        ##### Entry ########

        self.entry_frame = LabelFrame(self.win,text="Enter Details",background="black",font=('Arial',35),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)

        self.bill_no_lbl = Label(self.entry_frame,text="Bill Number",font=('Arial',15),bg="black")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent = Entry(self.entry_frame,bd=5,font=('Arial',15), textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")

        self.cust_nm_lbl = Label(self.entry_frame,text="Customer Name",font=('Arial',15),bg="black")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Arial',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_cot_lbl = Label(self.entry_frame,text="Customer Contact",font=('Arial',15),bg="black")
        self.cust_cot_lbl.grid(row=2,column=0,padx=2,pady=2)

        self.cust_cot_ent = Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=('Arial',15))
        self.cust_cot_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lbl = Label(self.entry_frame,text="Date",font=('Arial',15),bg="black")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)

        self.item_pur_lbl = Label(self.entry_frame,text="Item Purchased",font=('Arial',15),bg="black")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.item_pur_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Arial',15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qty_lbl = Label(self.entry_frame,text="Item Quantity",font=('Arial',15),bg="black")
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.item_qty_ent = Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Arial',15))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lbl = Label(self.entry_frame,text="Cost Of One",font=('Arial',15),bg="black")
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)

        self.cost_one_ent = Entry(self.entry_frame,bd=5,textvariable=cone,font=('Arial',15))
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)


        ########### Functions ##########

        def default_bill ():
            self.bill_txt.insert(END,"\t\t\t\tSwaad Restaurant")
            self.bill_txt.insert(END,"\n\t\t\t7 Street, Near Railway Lines, Badaun")
            self.bill_txt.insert(END,"\n\t\t\t   Contact - +91989076897")
            self.bill_txt.insert(END,"\n===============================================================================================")
            self.bill_txt.insert(END,f"Bill Number {bill_no_tk.get()}")

        def genbill():
            self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
            self.bill_txt.insert(END,f"\nCustomer Contact : {cust_cot.get()}")
            self.bill_txt.insert(END,f"\nDate : {date_pr.get()}")
            self.bill_txt.insert(END,"\n===============================================================================================")



        def add_pur():
            pass




        ####### Options #######

        self.button_frame = LabelFrame(self.entry_frame,bd=5, text="Options", bg="black",font=('Arial',15))
        self.button_frame.place(x=20,y=280,width=410,height=300)

        self.add_btn = Button(self.button_frame,bd=4,text="Add",font=('Arial',12),width=12,height=3)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.generate_btn = Button(self.button_frame,bd=4,text="Generate",font=('Arial',12),width=12,height=3, command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.clear_btn = Button(self.button_frame,bd=4,text="Clear",font=('Arial',12),width=12,height=3)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)

        self.total_btn = Button(self.button_frame,bd=4,text="Total",font=('Arial',12),width=12,height=3)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)

        self.reset_btn = Button(self.button_frame,bd=4,text="Reset",font=('Arial',12),width=12,height=3)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

        self.save_btn = Button(self.button_frame,bd=4,text="Save",font=('Arial',12),width=12,height=3)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)

        ##############################

        


        ###### Calculator Frame ########

        self.calc_frame = Frame(self.win, bd=8, background="black",relief=GROOVE)
        self.calc_frame.place(x=578,y=110,width=720,height=295)

        self.num_ent = Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=calc_var,font=('Arial',15),width=54, justify='right' )
        self.num_ent.grid(row=0,column=0,columnspan=11)


        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "C":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()


        self.btn7 = Button(self.calc_frame,bg="black",text=7,bd=8,width=12,height=1,font=('Arial',15))
        self.btn7.grid(row=1,column=0,padx=2,pady=2)
        self.btn7.bind("<Button-1>",press_btn)

        self.btn8 = Button(self.calc_frame,bg="black",text=8,bd=8,width=12,height=1,font=('Arial',15))
        self.btn8.grid(row=1,column=1,padx=2,pady=2)
        self.btn8.bind("<Button-1>",press_btn)
        

        self.btn9 = Button(self.calc_frame,bg="black",text=9,bd=8,width=12,height=1,font=('Arial',15))
        self.btn9.grid(row=1,column=2,padx=2,pady=2)
        self.btn9.bind("<Button-1>",press_btn)

        self.btnadd = Button(self.calc_frame,bg="black",text="+",bd=8,width=12,height=1,font=('Arial',15))
        self.btnadd.grid(row=1,column=3,padx=2,pady=1)
        self.btnadd.bind("<Button-1>",press_btn)

        self.btn4 = Button(self.calc_frame,bg="black",text=4,bd=8,width=12,height=1,font=('Arial',15))
        self.btn4.grid(row=2,column=0,padx=2,pady=2)
        self.btn4.bind("<Button-1>",press_btn)

        self.btn5 = Button(self.calc_frame,bg="black",text=5,bd=8,width=12,height=1,font=('Arial',15))
        self.btn5.grid(row=2,column=1,padx=2,pady=1)
        self.btn5.bind("<Button-1>",press_btn)

        self.btn6 = Button(self.calc_frame,bg="black",text=6,bd=8,width=12,height=1,font=('Arial',15))
        self.btn6.grid(row=2,column=2,padx=2,pady=2)
        self.btn6.bind("<Button-1>",press_btn)

        self.btnsubs = Button(self.calc_frame,bg="black",text="-",bd=8,width=12,height=1,font=('Arial',15))
        self.btnsubs.grid(row=2,column=3,padx=2,pady=2)
        self.btnsubs.bind("<Button-1>",press_btn)

        self.btn0 = Button(self.calc_frame,bg="black",text=0,bd=8,width=12,height=1,font=('Arial',15))
        self.btn0.grid(row=4,column=0,padx=2,pady=2)
        self.btn0.bind("<Button-1>",press_btn)

        self.btnpoint = Button(self.calc_frame,bg="black",text=".",bd=8,width=12,height=1,font=('Arial',15))
        self.btnpoint.grid(row=4,column=1,padx=2,pady=2)
        self.btnpoint.bind("<Button-1>",press_btn)

        self.btnclear = Button(self.calc_frame,bg="black",text="=",bd=8,width=12,height=1,font=('Arial',15))
        self.btnclear.grid(row=4,column=2,padx=2,pady=2)
        self.btnclear.bind("<Button-1>",press_btn)

        self.btndiv = Button(self.calc_frame,bg="black",text="/",bd=8,width=12,height=1,font=('Arial',15))
        self.btndiv.grid(row=4,column=3,padx=2,pady=2)
        self.btndiv.bind("<Button-1>",press_btn)

        self.btn1 = Button(self.calc_frame,bg="black",text=1,bd=8,width=12,height=1,font=('Arial',15))
        self.btn1.grid(row=3,column=0,padx=2,pady=2)
        self.btn1.bind("<Button-1>",press_btn)

        self.btn2 = Button(self.calc_frame,bg="black",text=2,bd=8,width=12,height=1,font=('Arial',15))
        self.btn2.grid(row=3,column=1,padx=2,pady=2)
        self.btn2.bind("<Button-1>",press_btn)

        self.btn3 = Button(self.calc_frame,bg="black",text=3,bd=8,width=12,height=1,font=('Arial',15))
        self.btn3.grid(row=3,column=2,padx=2,pady=2)
        self.btn3.bind("<Button-1>",press_btn)

        self.btnmult = Button(self.calc_frame,bg="black",text="*",bd=8,width=12,height=1,font=('Arial',15))
        self.btnmult.grid(row=3,column=3,padx=2,pady=2)
        self.btnmult.bind("<Button-1>",press_btn)


        ##### Bill Frame ########
        self.bill_frame = LabelFrame(self.win,text="Bill Area",font=("Arial",18),background="black",bd=8,relief=GROOVE)
        self.bill_frame.place(x=585,y=420,width=710,height=320)

        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame, bg="black",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=True)
        
        default_bill()
        


if __name__ == "__main__":
    main()