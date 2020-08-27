from tkinter import *
import random
from tkinter import messagebox
import sqlite3
from tkinter import *
import random
from tkinter import messagebox


class Bill_App:


    def __init__(self, root):
        self.r = []
        self.conn = sqlite3.connect('project.db')
        self.c = self.conn.cursor()
        # self.c.execute(
        #     """CREATE TABLE data(billno VARCHAR(20),name VARCHAR(20),cphone VARCHAR(20),items VARCHAR(255),price VARCHAR(20))""")
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#4863A0"
        # variables

        # -----customer details variable-------#
        self.c_name = StringVar()
        self.c_ph = StringVar()
        self.bill_no = StringVar()
        x = random.randint(10000000, 99999999)
        self.bill_no.set(str(x))

        # -----Help in bill print------#
        self.total_price = IntVar()
        self.total_tax = IntVar()

        # -----Cosmetics----#

        self.bs = IntVar()
        self.fc = IntVar()
        self.hs = IntVar()
        self.fw = IntVar()
        self.bl = IntVar()
        self.hg = IntVar()

        # ------Groceries------#

        self.rc = IntVar()
        self.fo = IntVar()
        self.dl = IntVar()
        self.wt = IntVar()
        self.sg = IntVar()
        self.tea = IntVar()

        # ------cold drink--------#

        self.mz = IntVar()
        self.ck = IntVar()
        self.fr = IntVar()
        self.tu = IntVar()
        self.pep = IntVar()
        self.sp = IntVar()

        # -------Billing menu-------#

        self.cos = StringVar()
        self.gry = StringVar()
        self.cd = StringVar()
        self.cos_tax = StringVar()
        self.gry_tax = StringVar()
        self.cd_tax = StringVar()

        # --------Bill search-------#
        self.srch_bill = StringVar()



        #------for quanity---------#

        self.bathadmin = IntVar()
        self.facewashadmin = IntVar()
        self.faceadmin = IntVar()
        self.hairadmin = IntVar()
        self.bodyadmin = IntVar()
        self.hairgeladmin = IntVar()
        self.riceadmin =IntVar()
        self.foodoiladmin = IntVar()
        self.daaladmin = IntVar()
        self.wheatadmin = IntVar()
        self.sugaradmin = IntVar()
        self.teaadmin = IntVar()
        self.mazaadmin = IntVar()
        self.cokeadmin = IntVar()
        self.frootiadmin = IntVar()
        self.thumbsupadmin = IntVar()
        self.pepsiadmin = IntVar()
        self.spriteadmin = IntVar()
        #for admin pasnnel
        self.passadmin=StringVar()
        self.nameadmin=StringVar()


        # title of project
        title = Label(self.root, text="Billing Software", fg="gold", bg=bg_color, bd=12, relief=GROOVE,
                      font=("times new roman", 20, "bold"), pady=1).pack(fill=X)
        # Customer details frame
        F1 = LabelFrame(self.root, text="Customer Details", font=("time new roman", 15, "bold"), fg="gold", bg=bg_color,
                        bd=8, relief=GROOVE)
        F1.place(x=0, y=62, relwidth=1)

        # object of customer details frame
        cust_name_lb = Label(F1, text="Customer Name :", fg="white", bg=bg_color,
                             font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cust_name_txt = Entry(F1, width=20, textvariable=self.c_name, font=("arial", 13), bd=2, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=5)

        cust_cont_lb = Label(F1, text="Contact No :", fg="white", bg=bg_color,
                             font=("times new roman", 15, "bold")).grid(row=0, column=3, padx=20, pady=5)
        cust_cont_txt = Entry(F1, width=20, textvariable=self.c_ph, font=("arial", 13), bd=2, relief=SUNKEN).grid(row=0,
                                                                                                                  column=4,
                                                                                                                  padx=10,
                                                                                                                  pady=5)

        cust_billno_lb = Label(F1, text="Bill No :", fg="white", bg=bg_color,
                               font=("times new roman", 15, "bold")).grid(row=0, column=5, padx=20, pady=5)
        cust_bill_txt = Entry(F1, width=20, textvariable=self.srch_bill, font=("arial", 13), bd=2, relief=SUNKEN).grid(
            row=0, column=6, padx=20, pady=5)

        bill_search_btn = Button(F1, text="SEARCH", command=self.bill_search, fg="black", bg="white",
                                 font=("times new roman", 15, "bold"), bd=5, relief=GROOVE, width=10, height=1).grid(
            row=0, column=7, padx=30, pady=5)

        # Cosmetics details frame
        F2 = LabelFrame(self.root, text="Cosmetics", font=("time new roman", 15, "bold"), fg="gold", bg=bg_color, bd=8,
                        relief=GROOVE)
        F2.place(x=0, y=157, width=280, height=350)

        # object of cosmetics frame
        bs_lb = Label(F2, text="Bath Soap :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=6)
        bs_txt = Entry(F2, width=15, textvariable=self.bs, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        fc_lb = Label(F2, text="Face Cream :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(
            row=1, column=0, padx=12, pady=6)
        fc_txt = Entry(F2, width=15, textvariable=self.fc, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=1,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        hs_lb = Label(F2, text="Hair Spray :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(
            row=2, column=0, padx=10, pady=6)
        hs_txt = Entry(F2, width=15, textvariable=self.hs, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        fw_lb = Label(F2, text="Face Wash :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=6)
        fw_txt = Entry(F2, width=15, textvariable=self.fw, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=3,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        bl_lb = Label(F2, text="Body Loshan :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(
            row=4, column=0, padx=10, pady=6)
        bl_txt = Entry(F2, width=15, textvariable=self.bl, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=4,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        hg_lb = Label(F2, text="Hair Gel :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=5,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=6)
        hg_txt = Entry(F2, width=15, textvariable=self.hg, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        # Groceries details frame
        F3 = LabelFrame(self.root, text="Groceries", font=("time new roman", 15, "bold"), fg="gold", bg=bg_color, bd=8,
                        relief=GROOVE)
        F3.place(x=285, y=157, width=280, height=350)

        # object of Groceries frame
        rc_lb = Label(F3, text="Rice :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=6)
        rc_txt = Entry(F3, width=15, textvariable=self.rc, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        fo_lb = Label(F3, text="Food Oil :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=1,
                                                                                                                 column=0,
                                                                                                                 padx=12,
                                                                                                                 pady=6)
        fo_txt = Entry(F3, width=15, textvariable=self.fo, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=1,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        dl_lb = Label(F3, text="Daal :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=2,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=6)
        dl_txt = Entry(F3, width=15, textvariable=self.dl, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        wt_lb = Label(F3, text="Wheat :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=3,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=6)
        wt_txt = Entry(F3, width=15, textvariable=self.wt, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=3,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        sg_lb = Label(F3, text="Sugar :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=4,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=6)
        sg_txt = Entry(F3, width=15, textvariable=self.sg, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=4,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        tea_lb = Label(F3, text="Tea :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=5,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=6)
        tea_txt = Entry(F3, width=15, textvariable=self.tea, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(
            row=5, column=1, padx=5, pady=6)

        # Cold drinks details frame
        F4 = LabelFrame(self.root, text="Cold Drinks", font=("time new roman", 15, "bold"), fg="gold", bg=bg_color,
                        bd=8, relief=GROOVE)
        F4.place(x=570, y=157, width=280, height=350)

        # object of Groceries frame
        mz_lb = Label(F4, text="Maza :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=6)
        mz_txt = Entry(F4, width=15, textvariable=self.mz, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        ck_lb = Label(F4, text="Coke :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=1,
                                                                                                             column=0,
                                                                                                             padx=12,
                                                                                                             pady=6)
        ck_txt = Entry(F4, width=15, textvariable=self.ck, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=1,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        fr_lb = Label(F4, text="Frooti :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=2,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=6)
        fr_txt = Entry(F4, width=15, textvariable=self.fr, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        tu_lb = Label(F4, text="Thumbs Up :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=6)
        tu_txt = Entry(F4, width=15, textvariable=self.tu, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=3,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        pep_lb = Label(F4, text="Pepsi :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=4,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=6)
        pep_txt = Entry(F4, width=15, textvariable=self.pep, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(
            row=4, column=1, padx=5, pady=6)

        sp_lb = Label(F4, text="Sprite :", fg="white", bg=bg_color, font=("times new roman", 13, "bold")).grid(row=5,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=6)
        sp_txt = Entry(F4, width=15, textvariable=self.sp, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(row=5,
                                                                                                                 column=1,
                                                                                                                 padx=5,
                                                                                                                 pady=6)

        # Space for Bill Generate textarea
        F5 = Frame(self.root, bd=8, relief=GROOVE)
        F5.place(x=855, y=157, width=490, height=350)

        bill_title = Label(F5, text="Bill Area", font=("arial", 15, "bold"), bd=5, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scroll_y.set, font=("", 10))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH)

        # Billing menu frame
        F6 = LabelFrame(self.root, text="Billing Menu", font=("time new roman", 15, "bold"), fg="gold", bg=bg_color,
                        bd=8, relief=GROOVE)
        F6.place(x=0, y=512, relwidth=1, height=170)

        # Billing menu objects
        tt_cos_lb = Label(F6, text="Total cosmetics Price :", fg="white", bg=bg_color,
                          font=("times new roman", 13, "bold")).grid(row=0, column=0, padx=10, pady=6)
        tt_cos_txt = Entry(F6, width=15, textvariable=self.cos, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(
            row=0, column=1, padx=5, pady=6)

        cos_tax_lb = Label(F6, text="Total cosmetics Tax :", fg="white", bg=bg_color,
                           font=("times new roman", 13, "bold")).grid(row=0, column=2, padx=10, pady=6)
        cos_tax_txt = Entry(F6, width=15, textvariable=self.cos_tax, font=("arial", 10, "bold"), bd=2,
                            relief=SUNKEN).grid(row=0, column=3, padx=5, pady=6)

        tt_gry_lb = Label(F6, text="Total Groceries Price :", fg="white", bg=bg_color,
                          font=("times new roman", 13, "bold")).grid(row=1, column=0, padx=10, pady=6)
        tt_gry_txt = Entry(F6, width=15, textvariable=self.gry, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(
            row=1, column=1, padx=5, pady=6)

        gry_tax_lb = Label(F6, text="Total Groceries Tax :", fg="white", bg=bg_color,
                           font=("times new roman", 13, "bold")).grid(row=1, column=2, padx=10, pady=6)
        gry_tax_txt = Entry(F6, width=15, textvariable=self.gry_tax, font=("arial", 10, "bold"), bd=2,
                            relief=SUNKEN).grid(row=1, column=3, padx=5, pady=6)

        tt_cd_lb = Label(F6, text="Total Cold Drinks Price :", fg="white", bg=bg_color,
                         font=("times new roman", 13, "bold")).grid(row=2, column=0, padx=10, pady=6)
        tt_cd_txt = Entry(F6, width=15, textvariable=self.cd, font=("arial", 10, "bold"), bd=2, relief=SUNKEN).grid(
            row=2, column=1, padx=5, pady=6)

        cd_tax_lb = Label(F6, text="Total Cold Drinks Tax :", fg="white", bg=bg_color,
                          font=("times new roman", 13, "bold")).grid(row=2, column=2, padx=10, pady=6)
        cd_tax_txt = Entry(F6, width=15, textvariable=self.cd_tax, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=2, column=3, padx=5, pady=6)

        # menu frame in Billing menu frame
        F61 = Frame(F6, bg="white", bd=5, relief=GROOVE)
        F61.place(x=680, width=600, height=95)
        # buttom on f61 frame
        tot_btn = Button(F61, text="TOTAL", command=self.total, fg="white", bg="teal",
                         font=("times new roman", 14, "bold"), bd=5, relief=GROOVE, width=8, height=1).grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=3,
                                                                                                             pady=23)

        gen_bill_btn = Button(F61, text="GEN. BILL", command=self.genbill, fg="white", bg="teal",
                              font=("times new roman", 14, "bold"), bd=5, relief=GROOVE, width=8, height=1).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=8,
                                                                                                                  pady=23)

        clr_btn = Button(F61, command=self.clear, text="CLEAR", fg="white", bg="teal",
                         font=("times new roman", 14, "bold"), bd=5, relief=GROOVE, width=8, height=1).grid(row=0,
                                                                                                             column=2,
                                                                                                             padx=8,
                                                                                                             pady=23)

        exit_btn = Button(F61, command=self.exit, text="EXIT", fg="white", bg="teal",
                          font=("times new roman", 14, "bold"), bd=5, relief=GROOVE, width=8, height=1).grid(row=0,
                                                                                                              column=3,
                                                                                                              padx=8,pady=23)
        admin_btn=Button(F61,command=self.admin,text="ADMIN",fg="white",bg="teal",font=("times new roman",14,"bold"),bd=5,relief=GROOVE,
                         width=8,height=1).grid(row=0,column=4,padx=8,pady=23)



        self.welcome_bil()




    def total(self):
        self.costotal = (
                (self.bs.get() * self.bathadmin.get()) +
                (self.hs.get() * self.faceadmin.get()) +
                (self.bl.get() * self.hairadmin.get()) +
                (self.fc.get() * self.facewashadmin.get()) +
                (self.fw.get() * self.bodyadmin.get()) +
                (self.hg.get() * self.hairgeladmin.get())
        )
        self.cos.set(str(f"Rs. {self.costotal}"))
        self.cos_tax.set(str(f"Rs. {(self.costotal/100)*6}"))

        self.grytotal = (
                (self.rc.get() * self.riceadmin.get()) +
                (self.wt.get() * self.foodoiladmin.get()) +
                (self.fo.get() * self.daaladmin.get()) +
                (self.dl.get() * self.wheatadmin.get()) +
                (self.sg.get() * self.sugaradmin.get()) +
                (self.tea.get() * self.teaadmin.get())
        )
        self.gry.set(str(f"Rs. {self.grytotal}"))
        self.gry_tax.set(str(f"Rs. {(self.grytotal/100)*6}"))

        self.cdtotal = (
                (self.mz.get() * self.mazaadmin.get()) +
                (self.tu.get() * self.cokeadmin.get()) +
                (self.sp.get() * self.frootiadmin.get()) +
                (self.ck.get() * self.thumbsupadmin.get()) +
                (self.pep.get() * self.pepsiadmin.get()) +
                (self.fr.get() * self.spriteadmin.get())
        )
        self.cd.set(str(f"Rs. {self.cdtotal}"))
        self.cd_tax.set(str(f"Rs. {(self.cdtotal/100)*12}"))  #12%gst in cold drink

        # print(self.grytotal)
        self.total_price.set(self.costotal + self.grytotal + self.cdtotal)
        self.total_tax.set(((self.costotal/100)*6) + ((self.grytotal/100)*6) + ((self.cdtotal/100)*12))

    def welcome_bil(self):
        self.textarea.insert(END, "\t\t\tWelcome to Retail shoping")
        self.textarea.insert(END, f"\n\n Bill no: {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer name: {self.c_name.get()}")
        self.textarea.insert(END, f"\n Customer phone: {self.c_ph.get()}")
        self.textarea.insert(END,
                             "\n\n*************************************************************************************")
        self.textarea.insert(END, f"\nProduct\t\t\tQuantity\t\t\t\tPrice")
        self.textarea.insert(END,
                             "\n\n*************************************************************************************")

    def genbill(self):
        if self.c_name.get() == "" or self.c_ph.get() == "":
            messagebox.showerror("Error", "Customer Details are needed!!")


        elif self.total_price.get() == 0:
            messagebox.showerror("Error", "No product selected")
        else:

            self.textarea.delete('1.0', END)
            self.textarea.insert(END, "\t\t\tWelcome to Retail shoping")
            self.textarea.insert(END, f"\n\n Bill no: {self.bill_no.get()}")
            self.textarea.insert(END, f"\n Cust. name: {self.c_name.get()}")
            self.textarea.insert(END, f"\n Cust. phone: {self.c_ph.get()}")
            self.textarea.insert(END,
                                 "\n\n*************************************************************************************")
            self.textarea.insert(END, f"\nProduct\t\t\tQuantity\t\t\t\tPrice")
            self.textarea.insert(END,
                                 "\n\n*************************************************************************************")

            # cosmetic
            if self.bs.get() != 0:
                self.textarea.insert(END, f"\nBath Soup\t\t\t{self.bs.get()}\t\t\t\t{self.bs.get() * self.bathadmin.get()}")
                print(self.hairgeladmin.get())
                self.r.append("Bath Soup")
            if self.hs.get() != 0:
                self.textarea.insert(END, f"\nHair Spray\t\t\t{self.hs.get()}\t\t\t\t{self.hs.get() * self.hairadmin.get()}")
                self.r.append("hair spray")
            if self.bl.get() != 0:
                self.textarea.insert(END, f"\nBody Loshan\t\t\t{self.bl.get()}\t\t\t\t{self.bl.get() * self.bodyadmin.get()}")
                self.r.append("body losan")
            if self.fc.get() != 0:
                self.textarea.insert(END, f"\nFace Cream\t\t\t{self.fc.get()}\t\t\t\t{self.fc.get() * self.faceadmin.get()}")
                self.r.append("Face Cream")
            if self.fw.get() != 0:
                self.textarea.insert(END, f"\nFace wash\t\t\t{self.fw.get()}\t\t\t\t{self.fw.get() * self.facewashadmin.get()}")
                self.r.append("Face wash")
            if self.hg.get() != 0:
                self.textarea.insert(END, f"\nHair Gel\t\t\t{self.hg.get()}\t\t\t\t{self.hg.get() * self.hairgeladmin.get()}")
                self.r.append("Hair Gel")

            # groceries
            if self.rc.get() != 0:
                self.textarea.insert(END, f"\nRice\t\t\t{self.rc.get()}\t\t\t\t{self.rc.get() * self.riceadmin.get()}")
                self.r.append("Rice")
            if self.wt.get() != 0:
                self.textarea.insert(END, f"\nWheat\t\t\t{self.wt.get()}\t\t\t\t{self.wt.get() * self.wheatadmin.get()}")
                self.r.append("Wheat")
            if self.fo.get() != 0:
                self.textarea.insert(END, f"\nFood Oil\t\t\t{self.fo.get()}\t\t\t\t{self.fo.get() * self.foodoiladmin.get()}")
                self.r.append("Food Oil")
            if self.dl.get() != 0:
                self.textarea.insert(END, f"\nDaal\t\t\t{self.dl.get()}\t\t\t\t{self.dl.get() * self.daaladmin.get()}")
                self.r.append("Daal")
            if self.sg.get() != 0:
                self.textarea.insert(END, f"\nSugar\t\t\t{self.sg.get()}\t\t\t\t{self.sg.get() * self.sugaradmin.get()}")
                self.r.append("Sugar")
            if self.tea.get() != 0:
                self.textarea.insert(END, f"\nTea\t\t\t{self.tea.get()}\t\t\t\t{self.tea.get() * self.teaadmin.get()}")
                self.r.append("Tea")

            # Cold drink
            if self.mz.get() != 0:
                self.textarea.insert(END, f"\nMaaza\t\t\t{self.mz.get()}\t\t\t\t{self.mz.get() * self.mazaadmin.get()}")
                self.r.append("Maaza")
            if self.tu.get() != 0:
                self.textarea.insert(END, f"\nThumbs Up\t\t\t{self.tu.get()}\t\t\t\t{self.tu.get() * self.thumbsupadmin.get()}")
                self.r.append("Thumbs Up")
            if self.sp.get() != 0:
                self.textarea.insert(END, f"\nSprite\t\t\t{self.sp.get()}\t\t\t\t{self.sp.get() * self.spriteadmin.get()}")
                self.r.append("Sprite")
            if self.ck.get() != 0:
                self.textarea.insert(END, f"\nCoke\t\t\t{self.ck.get()}\t\t\t\t{self.ck.get() * self.cokeadmin.get()}")
                self.r.append("Coke")
            if self.pep.get() != 0:
                self.textarea.insert(END, f"\nPepsi\t\t\t{self.pep.get()}\t\t\t\t{self.pep.get() * self.pepsiadmin.get()}")
                self.r.append("Pepsi")
            if self.fr.get() != 0:
                self.textarea.insert(END, f"\nFrooti\t\t\t{self.fr.get()}\t\t\t\t{self.fr.get() * self.frootiadmin.get()}")
                self.r.append("Frooti")

            self.textarea.insert(END,
                                 "\n**************************************************************************************")

            self.textarea.insert(END, f"\n\n\t\t\t\t\tTotal Price : Rs.{self.total_price.get()}")
            self.textarea.insert(END, f"\n\t\t\t\t\tTotal Tax (Round of) : Rs.{self.total_tax.get()}")
            self.textarea.insert(END, f"\n\n\t\t\t\t\tGrand Total : Rs.{self.total_price.get() + self.total_tax.get()}")
            self.save_bill()





    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you wnat to save the Bill?")
        if op > 0:
            file = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            file.write(self.textarea.get("1.0", END))
            file.close()
            # CREATE TABLE data(billno VARCHAR(20),name VARCHAR(20),cphone VARCHAR(20),items VARCHAR(255),price VARCHAR(20))
            temp=",".join(self.r)
            print(temp)
            f=f"INSERT INTO data(billno,name,cphone,items,price) VALUES('{self.bill_no.get()}','{self.c_name.get()}','{self.c_ph.get()}','{temp}','{self.total_price.get()}');"
            print(f)
            self.c.execute(f)
            self.conn.commit()
            # self.c.execute("""SELECT * FROM data""")
            return
        else:
            return

    def bill_search(self):
        try:
            f = open("bills/" + self.srch_bill.get() + ".txt", "r")
            self.textarea.delete("1.0", END)
            m = f.readline()
            while m:
                self.textarea.insert(END, m)
                m = f.readline()

        except:
            messagebox.showerror("Error", "INVALID BILL NO")



    def admin(self):
        # print("clicked ")
        # self.root2 = Tk()
        self.Fadmin = LabelFrame(self.root, text="admin", font=("time new roman", 15, "bold"), fg="gold", bg='#4863A0',
                            bd=8, relief=GROOVE)
        self.Fadmin.place(x=100, y=100, width=1000, height=570)
        title_ad = Label(self.Fadmin, text="Billing Software-ADMIN PANNEL", fg="gold", bg='#4863A0', bd=12, relief=GROOVE,
                      font=("times new roman", 20, "bold"), pady=1).pack(fill=X)
        F1_admin = LabelFrame(self.Fadmin, text="cosmatics", font=("time new roman", 15, "bold"), fg="gold", bg='#4863A0',
                        bd=8, relief=GROOVE)
        F1_admin.place(x=0,y=45, width=300, height=300)
        F2_admin = LabelFrame(self.Fadmin, text="groceris", font=("time new roman", 15, "bold"), fg="gold",
                              bg='#4863A0',
                              bd=8, relief=GROOVE)


        F2_admin.place(x=300, y=45, width=300, height=300)
        F3_admin = LabelFrame(self.Fadmin, text="Cold drink", font=("time new roman", 15, "bold"), fg="gold",
                              bg='#4863A0',
                              bd=8, relief=GROOVE)
        F3_admin.place(x=600, y=45, width=300, height=300)
        F4_admin = LabelFrame(self.Fadmin, text="admin detils", font=("time new roman", 15, "bold"), fg="gold",
                              bg='#4863A0',
                              bd=8, relief=GROOVE)
        F4_admin.place(x=0, y=325, width=900, height=170)


        #coasmatics wale
        bath_lb_admin = Label(F1_admin, text="Bath Soup:", fg="white", bg='#4863A0', font=("times new roman", 13, "bold")).grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=6)
        bathadmin_tax_txt = Entry(F1_admin, width=15, textvariable=self.bathadmin, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=0, column=3, padx=5, pady=6)




        face_lb_admin = Label(F1_admin, text="Face Wash:", fg="white", bg='#4863A0',
                            font=("times new roman", 13, "bold")).grid(row=1,
                                                                       column=0,
                                                                       padx=10,
                                                                       pady=6)
        faceadmin_tax_txt = Entry(F1_admin, width=15, textvariable=self.faceadmin, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=1, column=3, padx=5, pady=6)



        hair_lb_admin = Label(F1_admin, text="Hair Spray :", fg="white", bg='#4863A0',
                            font=("times new roman", 13, "bold")).grid(row=2,
                                                                       column=0,
                                                                       padx=10,
                                                                       pady=6)
        hairadmin_tax_txt = Entry(F1_admin, width=15, textvariable=self.hairadmin, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=2, column=3, padx=5, pady=6)


        facewash_lb_admin = Label(F1_admin, text="Face Wash:", fg="white", bg='#4863A0',
                                 font=("times new roman", 13, "bold")).grid(row=3,
                                                                            column=0,
                                                                            padx=10, pady=6)
        facewashadmin_tax_txt = Entry(F1_admin, width=15, textvariable=self.facewashadmin, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=3, column=3, padx=5, pady=6)


        body_lb_admin = Label(F1_admin, text="Body Loasan :", fg="white", bg='#4863A0',
                            font=("times new roman", 13, "bold")).grid(row=4,
                                                                       column=0,
                                                                       padx=10,
                                                                       pady=6)
        bodyadmin_tax_txt = Entry(F1_admin, width=15, textvariable=self.bodyadmin, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=4, column=3, padx=5, pady=6)


        hairgel_lb_admin = Label(F1_admin, text="Hair Gel :", fg="white", bg='#4863A0',
                            font=("times new roman", 13, "bold")).grid(row=5,
                                                                       column=0,
                                                                      padx=10,pady=6)
        hairgeladmin_tax_txt = Entry(F1_admin, width=15, textvariable=self.hairgeladmin, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=5, column=3, padx=5, pady=6)

        #groceries
        rice_lb_admin = Label(F2_admin, text="rice :", fg="white", bg='#4863A0',
                                 font=("times new roman", 13, "bold")).grid(row=1,
                                                                            column=0,
                                                                            padx=10, pady=6)
        rice_tax_txt = Entry(F2_admin, width=15, textvariable=self.riceadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=1, column=3, padx=5, pady=6)



        foodoil_lb_admin = Label(F2_admin, text="Food Oil :", fg="white", bg='#4863A0',
                                 font=("times new roman", 13, "bold")).grid(row=2,
                                                                            column=0,
                                                                            padx=10, pady=6)
        foodoil_tax_txt = Entry(F2_admin, width=15, textvariable=self.foodoiladmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=2, column=3, padx=5, pady=6)



        daal_lb_admin = Label(F2_admin, text="Dall :", fg="white", bg='#4863A0',
                                 font=("times new roman", 13, "bold")).grid(row=3,
                                                                            column=0,
                                                                            padx=10, pady=6)
        daal_tax_txt = Entry(F2_admin, width=15, textvariable=self.daaladmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=3, column=3, padx=5, pady=6)



        wheat_lb_admin = Label(F2_admin, text="Wheat  :", fg="white", bg='#4863A0',
                                 font=("times new roman", 13, "bold")).grid(row=4,
                                                                            column=0,
                                                                            padx=10, pady=6)
        wheat_tax_txt = Entry(F2_admin, width=15, textvariable=self.wheatadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=4, column=3, padx=5, pady=6)



        sugra_lb_admin = Label(F2_admin, text="Sugar :", fg="white", bg='#4863A0',
                                 font=("times new roman", 13, "bold")).grid(row=5,
                                                                            column=0,
                                                                            padx=10, pady=6)
        sugar_tax_txt = Entry(F2_admin, width=15, textvariable=self.sugaradmin, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=5, column=3, padx=5, pady=6)




        tea_lb_admin = Label(F2_admin, text="Tea :", fg="white", bg='#4863A0',
                                 font=("times new roman", 13, "bold")).grid(row=6,
                                                                            column=0,
                                                                            padx=10, pady=6)
        tea_tax_txt = Entry(F2_admin, width=15, textvariable=self.teaadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=6, column=3, padx=5, pady=6)



        #cold drinks
        maza_lb_admin = Label(F3_admin, text="Maza:", fg="white", bg='#4863A0',
                              font=("times new roman", 13, "bold")).grid(row=1,
                                                                         column=0,
                                                                         padx=10, pady=6)
        maza_tax_txt = Entry(F3_admin, width=15, textvariable=self.mazaadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=1, column=3, padx=5, pady=6)



        coke_lb_admin = Label(F3_admin, text="Coke:", fg="white", bg='#4863A0',
                                 font=("times new roman", 13, "bold")).grid(row=2,
                                                                            column=0,
                                                                            padx=10, pady=6)
        coke_tax_txt = Entry(F3_admin, width=15, textvariable=self.cokeadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=2, column=3, padx=5, pady=6)



        frooti_lb_admin = Label(F3_admin, text="Frooti :", fg="white", bg='#4863A0',
                              font=("times new roman", 13, "bold")).grid(row=3,
                                                                         column=0,
                                                                         padx=10, pady=6)
        frooti_tax_txt = Entry(F3_admin, width=15, textvariable=self.frootiadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=3, column=3, padx=5, pady=6)



        thumbsup_lb_admin = Label(F3_admin, text="Thubs up  :", fg="white", bg='#4863A0',
                               font=("times new roman", 13, "bold")).grid(row=4,
                                                                          column=0,
                                                                          padx=10, pady=6)
        thumbsup_tax_txt = Entry(F3_admin, width=15, textvariable=self.thumbsupadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=4, column=3, padx=5, pady=6)



        pepsi_lb_admin = Label(F3_admin, text="Pepsi :", fg="white", bg='#4863A0',
                               font=("times new roman", 13, "bold")).grid(row=5,
                                                                          column=0,
                                                                          padx=10, pady=6)
        pepsi_tax_txt = Entry(F3_admin, width=15, textvariable=self.pepsiadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=5, column=3, padx=5, pady=6)




        sprite_lb_admin = Label(F3_admin, text="Sprite:", fg="white", bg='#4863A0',
                             font=("times new roman", 13, "bold")).grid(row=6,
                                                                        column=0,
                                                                        padx=10, pady=6)
        sprite_tax_txt = Entry(F3_admin, width=15, textvariable=self.spriteadmin, font=("arial", 10, "bold"), bd=2,
                           relief=SUNKEN).grid(row=6, column=3, padx=5, pady=6)

        #admin details
        nameadmin_lb_admin = Label(F4_admin, text="NAME:", fg="white", bg='#4863A0',
                              font=("times new roman", 13, "bold")).grid(row=1,
                                                                         column=0,
                                                                         padx=10, pady=6)
        nameadmin_tax_txt = Entry(F4_admin, width=15, textvariable=self.nameadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=1, column=2, padx=5, pady=6)



        passadmin_lb_admin = Label(F4_admin, text="password:", fg="white", bg='#4863A0',
                              font=("times new roman", 13, "bold")).grid(row=1,
                                                                         column=3,
                                                                         padx=10, pady=6)

        pass_tax_txt = Entry(F4_admin, width=15, textvariable=self.passadmin, font=("arial", 10, "bold"),
                                     bd=2,
                                     relief=SUNKEN).grid(row=1, column=4, padx=5, pady=6)
        tot2_btn = Button(F4_admin, text="SUBMIT", command=self.admincheck, fg="white", bg="teal",
                         font=("times new roman", 14, "bold"), bd=5, relief=GROOVE, width=8, height=1).grid(row=1,
                                                                                                            column=6,
                                                                                                            padx=10,
                                                                                                            pady=23)
        exit_btn = Button(F4_admin, text="exit", command=self.adminexit, fg="white", bg="teal",
                         font=("times new roman", 14, "bold"), bd=5, relief=GROOVE, width=8, height=1).grid(row=1,
                                                                                                            column=8,
                                                                                                            padx=10,
                                                                                                            pady=23)


    def setting(self):
        if self.bathadmin.get()==0:
            self.bathadmin.set(25)

        if self.faceadmin.get()==0:
            self.faceadmin.set(25)

        if self.hairadmin.get()==0:
            self.hairadmin.set(25)

        if self.facewashadmin.get()==0:
            self.facewashadmin.set(25)

        if self.bodyadmin.get()==0:
            self.bodyadmin.set(25)
        if self.hairgeladmin.get()==0:
            self.hairgeladmin.set(25)


        #gtocetris

        if self.riceadmin.get()==0:
            self.riceadmin.set(25)
        if self.foodoiladmin.get()==0:
            self.foodoiladmin.set(25)
        if self.daaladmin.get()==0:
            self.daaladmin.set(25)
        if self.wheatadmin.get()==0:
            self.wheatadmin.set(25)
        if self.sugaradmin.get()==0:
            self.sugaradmin.set(25)
        if self.teaadmin.get()==0:
            self.teaadmin.set(25)




        # codle drijck
        if self.mazaadmin.get()==0:
            self.mazaadmin.set(25)
        if self.cokeadmin.get()==0:
            self.cokeadmin.set(25)
        if self.frootiadmin.get()==0:
            self.frootiadmin.set(25)
        if self.pepsiadmin.get()==0:
            self.pepsiadmin.set(25)
        if self.thumbsupadmin.get()==0:
            self.thumbsupadmin.set(25)
        if self.spriteadmin.get()==0:
            self.spriteadmin.set(25)



    def adminexit(self):
        self.Fadmin.destroy()
    def admincheck(self):
        print("reached")
        if self.nameadmin.get()=='ROHIT' and self.passadmin.get()=='12345':
            self.setting()
            messagebox.showinfo("succesfull updates")
            self.adminexit()
        else:
            messagebox.showerror("errror","name or passowrd not match each others")
    def clear(self):
        # variables

        # -----customer details variable-------#
        self.c_name.set("")
        self.c_ph.set("")
        self.bill_no.set("")
        x = random.randint(10000000, 99999999)
        self.bill_no.set(str(x))

        # -----Help in bill print------#
        self.total_price.set(0)
        self.total_tax.set(0)

        # -----Cosmetics----#

        self.bs.set(0)
        self.fc.set(0)
        self.hs.set(0)
        self.fw.set(0)
        self.bl.set(0)
        self.hg.set(0)

        # ------Groceries------#

        self.rc.set(0)
        self.fo.set(0)
        self.dl.set(0)
        self.wt.set(0)
        self.sg.set(0)
        self.tea.set(0)

        # ------cold drink--------#

        self.mz.set(0)
        self.ck.set(0)
        self.fr.set(0)
        self.tu.set(0)
        self.pep.set(0)
        self.sp.set(0)

        # -------Billing menu-------#

        self.cos.set("")
        self.gry.set("")
        self.cd.set("")
        self.cos_tax.set("")
        self.gry_tax.set("")
        self.cd_tax.set("")

        # --------Bill search-------#
        self.srch_bill.set("")
        self.textarea.delete("1.0", END)
        self.welcome_bil()

    def exit(self):
        op = messagebox.askyesno("Do you really want to exit")
        if op > 0:
            self.final1()
            self.root.destroy()
        else:
            return
    def final1(self):


            self.conn.close()


# Main starting app
root = Tk()
obj = Bill_App(root)
root.mainloop()