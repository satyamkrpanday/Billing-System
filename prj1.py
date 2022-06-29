from tkinter import*
import random
import os
from tkinter import messagebox

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing Software")
        bg_color = "#1ABC9C"
        title = Label(self.root, text="Super Market", font=('Calibri', 28, 'bold'), pady=2, bd=12, bg="#004d4d", fg="White", relief=GROOVE)
        title.pack(fill=X)
    # ================variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.Ointment = IntVar()
        self.thermal_gun = IntVar()
    # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.Noodles = IntVar()
        #=============Beverages Drinks=============================
        self.RedBull = IntVar()
        self.Sting = IntVar()
        self.Monster = IntVar()
        self.coke = IntVar()
        self.PaperBoat = IntVar()
        self.Real = IntVar()
    # ==============Total product price================
        self.Health_price = StringVar()
        self.grocery_price = StringVar()
        self.Beverages_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.Health_tax = StringVar()
        self.grocery_tax = StringVar()
        self.Beverages_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('Arial', 15, 'bold'), bd=10, fg="white", bg="#009999")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg="#009999", font=('Arial', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#009999", font=('Arial', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#009999", font=('Arial', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================Health====================================
        F2 = LabelFrame(self.root, text="Health Care ", font=('Arial', 15, 'bold'), bd=10, fg="white", bg="#009999")
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('Arial', 16, 'bold'), bd=5, relief =GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        dettol_lbl = Label(F2, text="Dettol", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        dettol_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        dettol_txt = Entry(F2, width=10, textvariable=self.dettol, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        dettol_txt.grid(row=3, column=1, padx=10, pady=10)

        Ointment_lbl = Label(F2, text="Ointment", font =('Arial', 16, 'bold'), bg = "#009999", fg = "white")
        Ointment_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        Ointment_txt = Entry(F2, width=10, textvariable=self.Ointment, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        Ointment_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=10, textvariable=self.thermal_gun, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('Arial', 15, 'bold'), bd=10, fg="white", bg="#009999")
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        daal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        daal_txt = Entry(F3, width=10, textvariable=self.daal, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        daal_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        Noodles_lbl = Label(F3, text="Noodles", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        Noodles_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Noodles_txt = Entry(F3, width=10, textvariable=self.Noodles, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        Noodles_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========BeveragesDrinks================================
        F4 = LabelFrame(self.root, text="Beverages", font=('Arial', 15, 'bold'), bd=10, fg="white", bg="#009999")
        F4.place(x=670, y=180, width=325, height=380)

        RedBull_lbl = Label(F4, text="RedBull", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        RedBull_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        RedBull_txt = Entry(F4, width=10, textvariable=self.RedBull, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        RedBull_txt.grid(row=0, column=1, padx=10, pady=10)

        Sting_lbl = Label(F4, text="Sting", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        Sting_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Sting_txt = Entry(F4, width=10, textvariable=self.Sting, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        Sting_txt.grid(row=1, column=1, padx=10, pady=10)

        Monster_lbl = Label(F4, text="Monster", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        Monster_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F4, width=10, textvariable=self.Monster, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        PaperBoat_lbl = Label(F4, text="PaperBoat", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        PaperBoat_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        PaperBoat_txt = Entry(F4, width=10, textvariable=self.PaperBoat, font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        PaperBoat_txt.grid(row=4, column=1, padx=10, pady=10)

        Real_lbl = Label(F4, text="Real", font=('Arial', 16, 'bold'), bg="#009999", fg="white")
        Real_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Real_txt = Entry(F4, width=10, textvariable=self.Real , font=('Arial', 16, 'bold'), bd=5, relief=GROOVE)
        Real_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================g_m_pFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('Arial', 14, 'bold'), bd=10, fg="white", bg="#009999")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Health Price", font=('Arial', 14, 'bold'), bg="#009999", fg="white")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.Health_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('Arial', 14, 'bold'), bg="#009999", fg="white")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Beverages Price", font=('Arial', 14, 'bold'), bg="#009999", fg="white")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.Beverages_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Health Tax", font=('Arial', 14, 'bold'), bg="#009999", fg="white")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.Health_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('Arial', 14, 'bold'), bg="#009999", fg="white")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Beverages Tax", font=('Arial', 14, 'bold'), bg="#009999", fg="white")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.Beverages_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

#================totalBill==========================
    def total(self):
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_s_p = self.sanitizer.get()*40
        self.m_m_p = self.mask.get()*10
        self.m_d_p = self.dettol.get()*30
        self.m_n_p = self.Ointment.get()*50
        self.m_t_g_p = self.thermal_gun.get()*15
        self.total_Health_price = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.Health_price.set("Rs. "+str(self.total_Health_price))
        self.c_tax = round((self.total_Health_price*0.05), 2)
        self.Health_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*50
        self.g_f_o_p = self.food_oil.get()*100
        self.g_w_p = self.wheat.get()*10
        self.g_d_p = self.daal.get()*60
        self.g_f_p = self.flour.get()*80
        self.g_m_p = self.Noodles.get()*15
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_d_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.05), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.RedBull.get()*150
        self.c_d_l_p = self.Sting.get()*20
        self.c_d_m_p = self.Monster.get()*200
        self.c_d_c_p = self.coke.get()*195
        self.c_d_f_p = self.PaperBoat.get()*40
        self.c_m_d = self.Real.get()*120
        self.total_Beverages_price = float(self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)

        self.Beverages_price.set("Rs. "+str(self.total_Beverages_price))
        self.c_d_tax = round((self.total_Beverages_price * 0.1), 2)
        self.Beverages_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_Health_price+self.total_grocery_price+self.total_Beverages_price+self.c_tax+self.g_tax+self.c_d_tax)

#==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t    Super Market    ")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

#=========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.Health_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.Beverages_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============Health===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.mask.get()}\t\t{self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        if self.dettol.get() != 0:
            self.txtarea.insert(END, f"\n Dettol\t\t{self.dettol.get()}\t\t{self.m_d_p}")
        if self.Ointment.get() != 0:
            self.txtarea.insert(END, f"\n Ointment\t\t{self.Ointment.get()}\t\t{self.m_n_p}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END , f"\n Thermal Gun\t\t{self.sanitizer.get()}\t\t{self.m_t_g_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.Noodles.get() != 0:
            self.txtarea.insert(END, f"\n Noodles\t\t{self.Noodles.get()}\t\t{self.g_m_p}")
        #================Beverages==========================
        if self.RedBull.get() != 0:
            self.txtarea.insert(END, f"\n RedBull\t\t{self.RedBull.get()}\t\t{self.c_d_s_p}")
        if self.Sting.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.Sting.get()}\t\t{self.c_d_l_p}")
        if self.Monster.get() != 0:
            self.txtarea.insert(END, f"\n Monster\t\t{self.Monster.get()}\t\t{self.c_d_m_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Dettol\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.PaperBoat.get() != 0:
            self.txtarea.insert(END, f"\n PaperBoat\t\t{self.Ointment.get()}\t\t{self.c_d_f_p}")
        if self.Real.get() != 0:
            self.txtarea.insert(END, f"\n Real \t\t{self.sanitizer.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
        # ===============taxes==============================
        if self.Health_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Health Tax\t\t\t{self.Health_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.Beverages_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Beverages  Tax\t\t\t{self.Beverages_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.dettol.set(0)
            self.Ointment.set(0)
            self.thermal_gun.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.Noodles.set(0)
    # =============BeveragesDrinks=============================
            self.RedBull.set(0)
            self.Sting.set(0)
            self.Monster.set(0)
            self.coke.set(0)
            self.PaperBoat.set(0)
            self.Real.set(0)
    # ====================taxes================================
            self.Health_price.set("")
            self.grocery_price.set("")
            self.Beverages_price.set("")

            self.Health_tax.set("")
            self.grocery_tax.set("")
            self.Beverages_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()

