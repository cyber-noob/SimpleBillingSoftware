from tkinter import *
import tkinter.messagebox as tm

class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("RETAIL BILLING SYSTEM")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.attributes('-fullscreen', True)
        self.root.geometry("%dx%d+0+0"%(width,height))
        bgColor = "#074463"
        self.root.config(bg=bgColor)
        title = Label(self.root, text="RETAIL BILLING SYSTEM",
                      bd=12,relief=GROOVE,bg=bgColor,fg="white",
                      font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #==============================Input Handling===========================================#
        
        def callback(input): 
      
            if input.isdigit(): 
                # print(input) 
                return True
            
            elif input is "": 
                # print(input) 
                return True
                
            else: 
                # print(input) 
                return False
        
        reg = root.register(callback)
        
        def on_click(event):
    
            event.widget.delete(0,"end")       #Auto clears widgetbox
            
        #===========================================Variable======================================#
        
        self.c_name = StringVar()
        self.phone = StringVar()
        self.bill_num = StringVar()
        self.cos_price = StringVar()
        self.snack_price = StringVar()
        self.household_price = StringVar()
        self.cos_tax = StringVar()
        self.snack_tax = StringVar()
        self.household_tax = StringVar()
        
        self.cream = IntVar()
        self.scent = IntVar()
        self.hair_gel = IntVar()
        self.lotion = IntVar()
        self.body_wash = IntVar()
        self.soap = IntVar()
        
        self.ice_cream = IntVar()
        self.cake = IntVar()
        self.samosa = IntVar()
        self.chips = IntVar()
        self.smoothie = IntVar()
        self.mixture = IntVar()
        
        self.cleaners = IntVar()
        self.vessels = IntVar()
        self.matress = IntVar()
        self.oils = IntVar()
        self.grains = IntVar()
        self.flour = IntVar()

        #==============================CUSTOMER DETAILS FRMAE=====================================#

        F1 = LabelFrame(self.root, text="Customer Details", font=("times new roman",15,"bold"),
                        fg="gold",bg=bgColor, bd=10, relief=GROOVE)
        F1.place(x=0,y=82,relwidth=1)
        
        name_lbl = Label(F1,text="Customer Name",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="white").grid(row=0,column=0,padx=20,pady=5)
        name_txt = Entry(F1, width=15, font=("arial",15), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        
        phone_lbl = Label(F1,text="Phone Number",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="white").grid(row=0,column=2,padx=20,pady=5)
        phone_txt = Entry(F1, width=15, font=("arial",15), bd=5, relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)
        
        bill_lbl = Label(F1,text="Bill Number",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="white").grid(row=0,column=4,padx=20,pady=5)
        bill_txt = Entry(F1, width=15, font=("arial",15), bd=5, relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)
        
        btn = Button(F1, text="Search",font=("arial 12 bold"),bd=5,width=10).grid(row=0,column=6,padx=25)
        
        #==============================COSMETICS_FRAME===============================================#
        
        F2 = LabelFrame(self.root, text="Cosmetics", font=("times new roman",15,"bold"),
                        fg="gold",bg=bgColor, bd=10, relief=GROOVE)
        F2.place(x=2,y=182,width=315,height=380)
        
        cream_lbl = Label(F2,text="Cream",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10, sticky="w")
        cream_txt = Entry(F2, width=10, font=("arial",15), bd=5,
                          textvariable=self.cream,validate="key",
                           validatecommand=(reg,'%P') ,relief=SUNKEN)
        cream_txt.bind("<Button-1>",on_click)
        cream_txt.bind("<FocusIn>",on_click)
        cream_txt.grid(row=0,column=1,padx=10,pady=10)
        if len(cream_txt.get())==0:
            cream_txt.set(0)
        
        scent_lbl = Label(F2,text="Scent",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10, sticky="w")
        scent_txt = Entry(F2, width=10, font=("arial",15), bd=5,
                          textvariable=self.scent,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        scent_txt.bind("<Button-1>",on_click)
        scent_txt.bind("<FocusIn>",on_click)
        scent_txt.grid(row=1,column=1,padx=10,pady=10)
        
        hairGel_lbl = Label(F2,text="Hair Gel",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10, sticky="w")
        hairGel_txt = Entry(F2, width=10, font=("arial",15), bd=5,
                            textvariable=self.hair_gel,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        hairGel_txt.bind("<Button-1>",on_click)
        hairGel_txt.bind("<FocusIn>",on_click)
        hairGel_txt.grid(row=2,column=1,padx=10,pady=10)
        
        lotion_lbl = Label(F2,text="Lotion",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10, sticky="w")
        lotion_txt = Entry(F2, width=10, font=("arial",15), bd=5,
                           textvariable=self.lotion,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        lotion_txt.bind("<Button-1>",on_click)
        lotion_txt.bind("<FocusIn>",on_click)
        lotion_txt.grid(row=3,column=1,padx=10,pady=10)
        
        bodyWash_lbl = Label(F2,text="Body Wash",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10, sticky="w")
        bodyWash_txt = Entry(F2, width=10, font=("arial",15), bd=5,
                             textvariable=self.body_wash,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        bodyWash_txt.bind("<Button-1>",on_click)
        bodyWash_txt.bind("<FocusIn>",on_click)
        bodyWash_txt.grid(row=4,column=1,padx=10,pady=10)
        
        soap_lbl = Label(F2,text="Soap",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10, sticky="w")
        soap_txt = Entry(F2, width=10, font=("arial",15), bd=5,
                         textvariable=self.soap,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        soap_txt.bind("<Button-1>",on_click)
        soap_txt.bind("<FocusIn>",on_click)
        soap_txt.grid(row=5,column=1,padx=10,pady=10)
        
        
        #=================================Snack_Section================================================#
        
        F3 = LabelFrame(self.root, text="Snack Corner", font=("times new roman",15,"bold"),
                        fg="gold",bg=bgColor, bd=10, relief=GROOVE)
        F3.place(x=319,y=182,width=315,height=380)
        
        iceCream_lbl = Label(F3,text="Ice Cream",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10, sticky="w")
        iceCream_txt = Entry(F3, width=10, font=("arial",15), bd=5,
                             textvariable=self.ice_cream,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        iceCream_txt.bind("<Button-1>",on_click)
        iceCream_txt.bind("<FocusIn>",on_click)
        iceCream_txt.grid(row=0,column=1,padx=10,pady=10)
        
        cake_lbl = Label(F3,text="Cake",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10, sticky="w")
        cake_txt = Entry(F3, width=10, font=("arial",15), bd=5,
                         textvariable=self.cake,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        cake_txt.bind("<Button-1>",on_click)
        cake_txt.bind("<FocusIn>",on_click)
        cake_txt.grid(row=1,column=1,padx=10,pady=10)
        
        samosa_lbl = Label(F3,text="Samosa",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10, sticky="w")
        samosa_txt = Entry(F3, width=10, font=("arial",15), bd=5,
                           textvariable=self.samosa,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        samosa_txt.bind("<Button-1>",on_click)
        samosa_txt.bind("<FocusIn>",on_click)
        samosa_txt.grid(row=2,column=1,padx=10,pady=10)
        
        chips_lbl = Label(F3,text="Chips",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10, sticky="w")
        chips_txt = Entry(F3, width=10, font=("arial",15), bd=5,
                          textvariable=self.chips,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        chips_txt.bind("<Button-1>",on_click)
        chips_txt.bind("<FocusIn>",on_click)
        chips_txt.grid(row=3,column=1,padx=10,pady=10)
        
        smoothie_lbl = Label(F3,text="Smoothies",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10, sticky="w")
        smoothie_txt = Entry(F3, width=10, font=("arial",15), bd=5,
                             textvariable=self.smoothie,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        smoothie_txt.bind("<Button-1>",on_click)
        smoothie_txt.bind("<FocusIn>",on_click)
        smoothie_txt.grid(row=4,column=1,padx=10,pady=10)
        
        mixture_lbl = Label(F3,text="Mixture",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10, sticky="w")
        mixture_txt = Entry(F3, width=10, font=("arial",15), bd=5,
                            textvariable=self.mixture,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        mixture_txt.bind("<Button-1>",on_click)
        mixture_txt.bind("<FocusIn>",on_click)
        mixture_txt.grid(row=5,column=1,padx=10,pady=10)
        
        #========================================Household_Essentials================================#
        
        F4 = LabelFrame(self.root, text="Household Essentials", font=("times new roman",15,"bold"),
                        fg="gold",bg=bgColor, bd=10, relief=GROOVE)
        F4.place(x=636,y=182,width=315,height=380)
        
        cleaners_lbl = Label(F4,text="Cleaners",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10, sticky="w")
        cleaners_txt = Entry(F4, width=10, font=("arial",15), bd=5,
                             textvariable=self.cleaners,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        cleaners_txt.bind("<Button-1>",on_click)
        cleaners_txt.bind("<FocusIn>",on_click)
        cleaners_txt.grid(row=0,column=1,padx=10,pady=10)
        
        vessels_lbl = Label(F4,text="Vessels",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10, sticky="w")
        vessels_txt = Entry(F4, width=10, font=("arial",15), bd=5,
                            textvariable=self.vessels,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        vessels_txt.bind("<Button-1>",on_click)
        vessels_txt.bind("<FocusIn>",on_click)
        vessels_txt.grid(row=1,column=1,padx=10,pady=10)
        
        matress_lbl = Label(F4,text="Matresses",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10, sticky="w")
        matress_txt = Entry(F4, width=10, font=("arial",15), bd=5,
                            textvariable=self.matress,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        matress_txt.bind("<Button-1>",on_click)
        matress_txt.bind("<FocusIn>",on_click)
        matress_txt.grid(row=2,column=1,padx=10,pady=10)
        
        oils_lbl = Label(F4,text="Oils",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10, sticky="w")
        oils_txt = Entry(F4, width=10, font=("arial",15), bd=5,
                         textvariable=self.oils,validate="key",
                           validatecommand=(reg,'%P') , relief=SUNKEN)
        oils_txt.bind("<Button-1>",on_click)
        oils_txt.bind("<FocusIn>",on_click)
        oils_txt.grid(row=3,column=1,padx=10,pady=10)
        
        grains_lbl = Label(F4,text="Grains",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10, sticky="w")
        grains_txt = Entry(F4, width=10, font=("arial",15), bd=5,
                           textvariable=self.grains,validate="key",
                           validatecommand=(reg,'%P') ,relief=SUNKEN)
        grains_txt.bind("<Button-1>",on_click)
        grains_txt.bind("<FocusIn>",on_click)
        grains_txt.grid(row=4,column=1,padx=10,pady=10)
               
        flour_lbl = Label(F4,text="Flour",font=("times new roman",15,"bold"),
                         bg=bgColor, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10, sticky="w")
        flour_txt = Entry(F4, width=10, font=("arial",15), bd=5,
                          textvariable=self.flour,validate="key",
                           validatecommand=(reg,'%P'), relief=SUNKEN)
        flour_txt.bind("<Button-1>",on_click)
        flour_txt.bind("<FocusIn>",on_click)
        flour_txt.grid(row=5,column=1,padx=10,pady=10)
        
        #========================================Bill_Area=======================================#
        
        F5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        F5.place(x=953,y=182,width=315,height=380)
        
        title_lbl = Label(F5, text="Bill Area", font="ariel 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        
        #========================================Botton_Frame=====================================#
        
        F6 = LabelFrame(self.root, text="Bill Menu", font=("times new roman",15,"bold"),
                        fg="gold",bg=bgColor, bd=10, relief=GROOVE)
        F6.place(x=0,y=570,relwidth=1,height=150)
        
        m1_lbl = Label(F6, text="Cosmetics Price", font=("times new roman",14,"bold"),
                       bg=bgColor,fg="white").grid(row=0,column=0,padx=20,pady=3,sticky="w")
        m1_txt = Entry(F6,width=15,font="arial 10 bold",bd=7,
                       textvariable=self.cos_price,relief=SUNKEN).grid(row=0,column=1,padx=15,pady=3)
        
        m2_lbl = Label(F6, text="Snacks Price", font=("times new roman",14,"bold"),
                       bg=bgColor,fg="white").grid(row=1,column=0,padx=20,pady=3,sticky="w")
        m2_txt = Entry(F6,width=15,font="arial 10 bold",bd=7,
                       textvariable=self.snack_price,relief=SUNKEN).grid(row=1,column=1,padx=15,pady=3)
        
        m3_lbl = Label(F6, text="Household Price", font=("times new roman",14,"bold"),
                       bg=bgColor,fg="white").grid(row=2,column=0,padx=20,pady=3,sticky="w")
        m3_txt = Entry(F6,width=15,font="arial 10 bold",bd=7,
                       textvariable=self.household_price,relief=SUNKEN).grid(row=2,column=1,padx=15,pady=3)
        
        #-----------------------------------Taxes-------------------------------------------------#
        
        t1_lbl = Label(F6, text="Cosmetics Taxes", font=("times new roman",14,"bold"),
                       bg=bgColor,fg="white").grid(row=0,column=2,padx=20,pady=3,sticky="nsew")
        t1_txt = Entry(F6,width=15,font="arial 10 bold",bd=7,
                       textvariable=self.cos_tax,relief=SUNKEN).grid(row=0,column=3,padx=15,pady=3)
        
        t2_lbl = Label(F6, text="Snacks Taxes", font=("times new roman",14,"bold"),
                       bg=bgColor,fg="white").grid(row=1,column=2,padx=20,pady=3,sticky="w")
        t2_txt = Entry(F6,width=15,font="arial 10 bold",bd=7,
                       textvariable=self.snack_tax,relief=SUNKEN).grid(row=1,column=3,padx=15,pady=3)
        
        t3_lbl = Label(F6, text="Household Taxes", font=("times new roman",14,"bold"),
                       bg=bgColor,fg="white").grid(row=2,column=2,padx=20,pady=3,sticky="w")
        t3_txt = Entry(F6,width=15,font="arial 10 bold",bd=7,
                       textvariable=self.household_tax,relief=SUNKEN).grid(row=2,column=3,padx=15,pady=3)
        
        btnFrame = Frame(F6, bd=7, relief=GROOVE)
        btnFrame.place(x=675,width=580,height=110)
        
        total_btn = Button(btnFrame, text="Total",font=("arial 13 bold"),command=self.total,
                     bd=5,width=10,bg="cadetblue",fg="white",pady=15).grid(row=0,column=0,padx=12,pady=10)
        
        print_btn = Button(btnFrame, text="Print",font=("arial 13 bold"),
                     bd=5,width=10,bg="cadetblue",fg="white",pady=15).grid(row=0,column=1,padx=12,pady=10)
        
        clear_btn = Button(btnFrame, text="Clear",font=("arial 13 bold"),
                     bd=5,width=10,bg="cadetblue",fg="white",pady=15).grid(row=0,column=2,padx=12,pady=10)
        
        exit_btn = Button(btnFrame, text="Exit",font=("arial 13 bold"),
                     bd=5,width=10,bg="cadetblue",fg="white",pady=15).grid(row=0,column=3,padx=12,pady=10)

        #===============================================Callbacks=========================================#
    
    def total_cosmetics(self):
        
            self.price = float((self.cream.get()*60)+ 
                                (self.scent.get()*110)+ 
                                (self.hair_gel.get()*90)+ 
                                (self.lotion.get()*72)+ 
                                (self.body_wash.get()*263)+ 
                                (self.soap.get()*25)) 
        
            self.cos_price.set("Rs "+str(round(self.price,2)))      #We round the numbers in order to make sure
                                                                    #that the decimal number doesn't flood our widget
                                                                    #and to prevent overflow
        
            self.cos_tax.set("Rs "+str(round(self.price*0.05,2)))
        
    def total_snacks(self):
        
        self.price = float((self.ice_cream.get()*56)+ 
                      (self.cake.get()*172)+ 
                      (self.samosa.get()*1000)+ 
                      (self.chips.get()*2)+ 
                      (self.smoothie.get()*263)+ 
                      (self.mixture.get()*125)) 
        
        self.snack_price.set("Rs "+str(round(self.price,2)))
        
        self.snack_tax.set("Rs "+str(round(self.price*0.12,2)))
        
    def total_household(self):
        
        self.price = float((self.cleaners.get()*98)+ 
                      (self.vessels.get()*124)+ 
                      (self.matress.get()*230)+ 
                      (self.oils.get()*52)+ 
                      (self.grains.get()*273)+ 
                      (self.flour.get()*85)) 
        
        self.household_price.set("Rs "+str(round(self.price,2)))
        
        self.household_tax.set("Rs "+str(round(self.price*0.08,2)))
        
    def total(self):
        
        self.total_cosmetics()
        self.total_snacks()
        self.total_household()

if __name__ == "__main__":

    root = Tk()
    app = Student(root)
    root.mainloop() 
    