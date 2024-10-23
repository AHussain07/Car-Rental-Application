from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3



root=tk.Tk()
root.geometry("1920x1080")
root.title("A-Level Computer Science NEA")


#functions_start


    #pages_start
def home_page():
    home_indicate.config(bg="White")
    
    hire_button["state"] = DISABLED
    rent_button["state"] = DISABLED
    reviews_button["state"] = DISABLED
    bookings_button["state"] = DISABLED
    
    
    def login():
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        
        cursor.execute("SELECT * FROM USER_INFO WHERE USERNAME = ? AND PASSWORD = ?",(username.get(),password.get(),))
        login_check=cursor.fetchone()
        
        if login_check:
            
            cursor.execute("SELECT USERID FROM USER_INFO WHERE USERNAME = ? AND PASSWORD = ?",(username.get(),password.get(),))
            global userid
            userid=cursor.fetchone()[0]
            print(userid)
            messagebox.showinfo(title="Login", message="Access Granted")
            delete_pages()
            hire_indicate.config(bg="White")
            home_indicate.config(bg="#00B1FF")
            hire_page()
            
            
            home_button["state"] = DISABLED
            join_button["state"] = DISABLED
            
            hire_button["state"] = NORMAL
            rent_button["state"] = NORMAL
            reviews_button["state"] = NORMAL
            bookings_button["state"] = NORMAL
            
            
            
        else:
            username.delete(0,"end")
            password.delete(0,"end")
            username.insert(0,"Username")
            password.insert(0,"Password")
            messagebox.showerror(title="Error", message="Login Failed! Please Try Again.")
               
    
    global signin_img
    home_frame = tk.Frame(main_frame)
    home_frame.configure(bg="#fff")
    home_frame.pack(pady=20)
    
    signin_img=PhotoImage(file='C.png')
    
    signin = tk.Label(home_frame, image=signin_img,bg="#fff").pack(pady=50)
    
    
    def on_enter(e):
        username.delete(0,"end")
    def on_leave(e):
        name=username.get()
        if name=="":
            username.insert(0,"Username")

    username= Entry(home_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    username.insert(0,"Username")
    username.pack(pady=5)
    username.bind("<FocusIn>",on_enter)
    username.bind("<FocusOut>",on_leave)
    
    Frame(home_frame,width=540,height=2,bg="black").pack(pady=2)
    
    space=Frame(home_frame,width=540,height=30,bg="#fff").pack(pady=2)
    
    def on_enter(e):
        password.delete(0,"end")
    def on_leave(e):
        name=password.get()
        if name=="":
            password.insert(0,"Password")

    password= Entry(home_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    password.insert(0,"Password")
    password.pack(pady=5)
    password.bind("<FocusIn>",on_enter)
    password.bind("<FocusOut>",on_leave)
    
    Frame(home_frame,width=540,height=2,bg="black").pack(pady=2)
    
    login_button=Button(home_frame,width=30,height=2,text="Sign In",font=(14),bg="#00B1FF",fg="white",border = 0,command = login).pack(pady=30)
    
    
def signup_page():
    
    def clear_signup():
        username.delete(0,"end")
        username.insert(0,"Username")
        password.delete(0,"end")
        password.insert(0,"Password")
        confirm_password.delete(0,"end")
        confirm_password.insert(0,"Confirm Password")
        address.delete(0,"end")
        address.insert(0,"Street Address")
        pc.delete(0,"end")
        pc.insert(0,"Postcode (e.g. SW1A 2AA)")
        age.set(0)
        driving_license.set(0)
        
    
    def signup():
        
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        
        check_age =age.get()
        check_dl = driving_license.get()
        
        cursor.execute("SELECT * FROM USER_INFO WHERE USERNAME=?",(username.get(),))
        check_username = cursor.fetchall()       
                        
        
        if check_age != 1 and check_dl != 1:
            messagebox.showerror(title="Error", message= "You do not meet the requirements to register a new account!" )
            clear_signup()
        elif username.get() == "Username" or password.get() =="Password" or address.get() == "Street Address" or pc.get() =="Postcode (e.g. SW1A 2AA)":
            messagebox.showerror(title="Error", message= "Please fill in all the required information " )
            clear_signup()
        elif len(password.get()) < 8:
            messagebox.showerror(title="Error", message= "Your Password Should Be At Least 8 Characters Long!" )
        
        elif len(pc.get()) < 4:
            messagebox.showerror(title="Error", message= "Invalid Postcode" )
            
        elif len(address.get()) < 5:
            messagebox.showerror(title="Error", message= "Invalid Street Address" )  
            
        
        elif password.get() != confirm_password.get():
            messagebox.showerror(title="Error", message= "Password does not match" )
            clear_signup()
        elif check_username:
            messagebox.showerror(title="Error", message= "Username has already been taken" )
            clear_signup()
            
        
            
            
        else:
            
            
            cursor.execute("INSERT INTO USER_INFO (USERNAME,PASSWORD,ADDRESS,POSTCODE) VALUES (:USER,:PASS,:ADDRESS,:POSTCODE)",
              {
                
                "USER":username.get(),
                "PASS":password.get(),
                "ADDRESS":address.get(),
                "POSTCODE":pc.get()
                
                
                 
              })
            
            
            
            connect.commit()
            
            
            
            connect.close()
            
            age.set(0)
            driving_license.set(0)
            
            delete_pages()
            hire_indicate.config(bg="White")
            join_indicate.config(bg="#00B1FF")
            messagebox.showinfo(title="Success", message="New account successfully registered!")
            hire_page()
            
            
            home_button["state"] = DISABLED
            join_button["state"] = DISABLED
            
            hire_button["state"] = NORMAL
            rent_button["state"] = NORMAL
            reviews_button["state"] = NORMAL
            bookings_button["state"] = NORMAL
            
            global userid
            userid = cursor.lastrowid
            
            
            
            
    
       
    
    global join_img
    signup_frame = tk.Frame(main_frame)
    signup_frame.configure(bg="#fff")
    signup_frame.pack(pady=20)
    
    join_img=PhotoImage(file='D.png')
    join_label = tk.Label(signup_frame, image=join_img,bg="#fff").pack(pady=50)
    
    def on_enter(e):
        username.delete(0,"end")
    def on_leave(e):
        name=username.get()
        if name=="":
            username.insert(0,"Username")

    username= Entry(signup_frame,width=40,font=("Microsoft YaHei UI Light",16),bd=0)
    username.insert(0,"Username")
    username.pack(pady=5)
    username.bind("<FocusIn>",on_enter)
    username.bind("<FocusOut>",on_leave)
    
    Frame(signup_frame,width=500,height=2,bg="black").pack(pady=2)
    
    def on_enter(e):
        password.delete(0,"end")
    def on_leave(e):
        name=password.get()
        if name=="":
            password.insert(0,"Password")

    password= Entry(signup_frame,width=40,font=("Microsoft YaHei UI Light",16),bd=0)
    password.insert(0,"Password")
    password.pack(pady=5)
    password.bind("<FocusIn>",on_enter)
    password.bind("<FocusOut>",on_leave)
    
    Frame(signup_frame,width=500,height=2,bg="black").pack(pady=2)
    
    def on_enter(e):
        confirm_password.delete(0,"end")
    def on_leave(e):
        name=confirm_password.get()
        if name=="":
            confirm_password.insert(0,"Confirm Password")

    confirm_password= Entry(signup_frame,width=40,font=("Microsoft YaHei UI Light",16),bd=0)
    confirm_password.insert(0,"Confirm Password")
    confirm_password.pack(pady=5)
    confirm_password.bind("<FocusIn>",on_enter)
    confirm_password.bind("<FocusOut>",on_leave)
    
    Frame(signup_frame,width=500,height=2,bg="black").pack(pady=2)
    
    
    def on_enter(e):
        address.delete(0,"end")
    def on_leave(e):
        name=address.get()
        if name=="":
            address.insert(0,"Street Address")

    address= Entry(signup_frame,width=40,font=("Microsoft YaHei UI Light",16),bd=0)
    address.insert(0,"Street Address")
    address.pack(pady=5)
    address.bind("<FocusIn>",on_enter)
    address.bind("<FocusOut>",on_leave)
    
    Frame(signup_frame,width=500,height=2,bg="black").pack(pady=2)
    
    def on_enter(e):
        pc.delete(0,"end")
    def on_leave(e):
        name=pc.get()
        if name=="":
            pc.insert(0,"Postcode (e.g. SW1A 2AA)")

    pc= Entry(signup_frame,width=40,font=("Microsoft YaHei UI Light",16),bd=0)
    pc.insert(0,"Postcode (e.g. SW1A 2AA)")
    pc.pack(pady=5)
    pc.bind("<FocusIn>",on_enter)
    pc.bind("<FocusOut>",on_leave)
    
    Frame(signup_frame,width=500,height=2,bg="black").pack(pady=2)
    
    
    age = IntVar()
    age_checkbox = Checkbutton(signup_frame,text="I am 18 or over",variable = age,bg="#fff",fg="#00B1FF",font=("bold",11,"bold")).pack(pady=5)
    
    driving_license = IntVar()
    driving_license_checkbox = Checkbutton(signup_frame,text="I have a driving license",variable = driving_license,bg="#fff",fg="#00B1FF",font=("bold",11,"bold")).pack(pady=5)
    
    
    
    signup_button=Button(signup_frame,width=30,height=2,text="JOIN",font=(14),bg="#00B1FF",fg="white",border = 0,command = signup).pack(pady=30)
 
       
       
def hire_page():
    
    
    def hire():
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        select_car = hire_tree.focus()
        car_details=hire_tree.item(select_car)
        print(car_details.get("values"))
        get_carid = car_details.get("values")[0]
        print(userid)
        print(get_carid)
        
        try:
        
            cursor.execute("SELECT CUSTOMER FROM BOOKINGS WHERE CUSTOMER=(:USERID)",
                           {"USERID":userid
                               })
            
            check_bookings=cursor.fetchone()
            print(check_bookings)
            
            cursor.execute("SELECT CAR FROM BOOKINGS WHERE CAR =(:CARID)",
                           {"CARID":get_carid
                               
                               })
            
            check_if_booked=cursor.fetchone()
            
            
            
            
            if check_bookings:
                
                messagebox.showerror(title="Error", message="You Have Already Hired A Car")
                
            elif check_if_booked:
                messagebox.showerror(title="Error", message="Sorry. That Car Has Been Booked By Another User")
                hire_tree.delete(select_car)
                
            
            else:                
                cursor.execute("INSERT INTO BOOKINGS (CAR, CUSTOMER) VALUES(:CAR,:CUSTOMER)",
                               
                               { "CAR":get_carid,
                                 "CUSTOMER":userid
                                   
                                   
                                })
                
                
                cursor.execute("UPDATE CARS_LISTED SET BOOKED = 'TRUE' WHERE CARID = (:CARID)",
                               {"CARID":get_carid
                                   
                                   
                                })
                
                confirmation=messagebox.askyesno(title="Confirmation", message="Are You Sure You Want To Book This Car?")
                
            
                
                if confirmation:
                    connect.commit()    
                    connect.close()
                    hire_tree.delete(select_car)
        except:
            messagebox.showerror(title="Error", message="Please Select The Car You Would Like To Hire")
        
        
            
#FILTERS        
    def price_asc():
        for i in hire_tree.get_children():
            hire_tree.delete(i)
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        
        cursor.execute("""SELECT CARID,BRAND,MODEL,ENGINE,LOCATION,DURATION,PRICE
FROM CARS_LISTED
INNER JOIN CAR_MODEL ON CARS_LISTED.MODELID=CAR_MODEL.CARMODELID
WHERE BOOKED = 'FALSE'
ORDER BY PRICE ASC 
 """)
    
    
    
        hire_result = cursor.fetchall()
        for row in hire_result:
        
            hire_tree.insert("",tk.END, values=row)
            
    def price_desc():
        
        for i in hire_tree.get_children():
            hire_tree.delete(i)
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        
        cursor.execute("""SELECT CARID,BRAND,MODEL,ENGINE,LOCATION,DURATION,PRICE
FROM CARS_LISTED
INNER JOIN CAR_MODEL ON CARS_LISTED.MODELID=CAR_MODEL.CARMODELID
WHERE BOOKED = 'FALSE'
ORDER BY PRICE DESC 
 """)
    
    
    
        hire_result = cursor.fetchall()
        
        for row in hire_result:
        
            hire_tree.insert("",tk.END, values=row)
            
            
    def duration_desc():
        
        for i in hire_tree.get_children():
            hire_tree.delete(i)
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        
        cursor.execute("""SELECT CARID,BRAND,MODEL,ENGINE,LOCATION,DURATION,PRICE
FROM CARS_LISTED
INNER JOIN CAR_MODEL ON CARS_LISTED.MODELID=CAR_MODEL.CARMODELID
WHERE BOOKED = 'FALSE'
ORDER BY DURATION DESC 
 """)
    
    
    
        hire_result = cursor.fetchall()
        
        for row in hire_result:
        
            hire_tree.insert("",tk.END, values=row)
            
    def duration_asc():
        
        for i in hire_tree.get_children():
            hire_tree.delete(i)
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        
        cursor.execute("""SELECT CARID,BRAND,MODEL,ENGINE,LOCATION,DURATION,PRICE
FROM CARS_LISTED
INNER JOIN CAR_MODEL ON CARS_LISTED.MODELID=CAR_MODEL.CARMODELID
WHERE BOOKED = 'FALSE'
ORDER BY DURATION ASC
 """)
    
    
    
        hire_result = cursor.fetchall()
        
        for row in hire_result:
        
            hire_tree.insert("",tk.END, values=row)
            
    
           
#FILTERS END        
        
    
    hire_frame = tk.Frame(main_frame)
    hire_frame.configure(bg="#fff")
    lb = tk.Label(hire_frame, text="Hire A Car",font=("bold",30,"bold"),fg="#00B1FF",bg="#fff")
    lb.pack()
    hire_frame.pack(pady=50)
    
    connect = sqlite3.connect("CAR DB.db")
    cursor = connect.cursor()
    

    
    cursor.execute("""SELECT CARID,BRAND,MODEL,ENGINE,LOCATION,DURATION,PRICE
FROM CARS_LISTED
INNER JOIN CAR_MODEL ON CARS_LISTED.MODELID=CAR_MODEL.CARMODELID
WHERE BOOKED = 'FALSE'
""")
    
    
    
    hire_result = cursor.fetchall()
    print(hire_result)
    
    
    
    
    hire_tree = ttk.Treeview(hire_frame, height=25,selectmode="browse")
    hire_tree["columns"]=("CARID","Brand","Model","Engine Type","Pick Up Location","Duration","Price")
    hire_tree.column("#0",width = 0, stretch = NO)
    hire_tree.column("CARID",width = 0, stretch = NO)
    hire_tree.column("Brand",width = 240,anchor = W)
    hire_tree.column("Model",width = 240,anchor = W)
    hire_tree.column("Engine Type",width = 240,anchor = W)
    hire_tree.column("Pick Up Location",width = 240,anchor = W)
    hire_tree.column("Duration",width = 240,anchor = W)
    hire_tree.column("Price",width = 240,anchor = W)
    
    
    hire_tree.heading("#0",text="",anchor=W)
    hire_tree.heading("CARID",text="",anchor=W)
    hire_tree.heading("Brand",text="Brand",anchor=W)
    hire_tree.heading("Model",text="Model",anchor=W)
    hire_tree.heading("Engine Type",text="Engine Type",anchor=W)
    hire_tree.heading("Pick Up Location",text="Location",anchor=W)
    hire_tree.heading("Duration",text="Duration",anchor=W)
    hire_tree.heading("Price",text="Price in £",anchor=W)
    
    
    for row in hire_result:
        
        hire_tree.insert("",tk.END, values=row)
    
    hire_tree.pack(pady=5)
    
    filter_options = tk.Label(hire_frame, text="Sort By",font=("bold",16),fg="Black",bg="#fff")
    filter_options.pack(pady=10)
    pricedec_button=Button(hire_frame,width=20,height=1,text="Price:High To Low",font=(14),bg="White",fg="#00B1FF",border = 0,command = price_desc).pack(pady=3)
    priceasc_button=Button(hire_frame,width=20,height=1,text="Price:Low To High",font=(14),bg="White",fg="#00B1FF",border = 0,command = price_asc).pack(pady=3)
    durationdec_button=Button(hire_frame,width=20,height=1,text="Duration:High To Low",font=(14),bg="White",fg="#00B1FF",border = 0,command = duration_desc).pack(pady=3)
    durationasc_button=Button(hire_frame,width=20,height=1,text="Duration:Low To High",font=(14),bg="White",fg="#00B1FF",border = 0,command = duration_asc).pack(pady=3)

    hire_button=Button(hire_frame,width=30,height=2,text="HIRE",font=(14),bg="#00B1FF",fg="white",border = 0,command = hire)
    hire_button.pack(pady = 30 )
        
    
    
    
def rent_page():
    
    rent_frame = tk.Frame(main_frame)
    rent_frame.configure(bg="#fff")
    lb = tk.Label(rent_frame, text="List Your Car",font=("bold",30,"bold"),fg="#00B1FF",bg="#fff")
    lb.pack(pady=50)
    
    
    
    def clear_list():
        
        car_brand.delete(0,"end")
        car_model.delete(0,"end")
        location.delete(0,"end")
        price.delete(0,"end")
        Duration.delete(0,"end")
        engine_type.delete(0,"end")
            

        car_brand.insert(0,"Car Brand (e.g. Tesla)")
        car_model.insert(0,"Model (e.g. Tesla Model s)")
        location.insert(0,"Address (City)")
        price.insert(0,"Price")
        Duration.insert(0,"Duration (In Days)")
        engine_type.insert(0,"Engine Type (Manual or Automatic)")
    
    def rent_info():
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        
        engine_type_check = engine_type.get().upper()
        
        cursor.execute("SELECT CARMODELID FROM CAR_MODEL WHERE BRAND = ? AND MODEL = ? AND ENGINE = ?",(car_brand.get(),car_model.get(),engine_type.get(),))
        
        
        model_check=cursor.fetchone()
        print(model_check)
         
        
        
        
        if car_brand.get() == "Car Brand (e.g. Tesla)" or car_model.get() =="Model (e.g. Tesla Model s)" or engine_type.get() == "Engine Type (Manual or Automatic)" or location.get() == "Address (City)" or price.get() == "Price" or Duration.get() == "Duration (In Days)"  :
            messagebox.showerror(title="Error", message= "Please Fill In All The Required Information" )
            clear_list()
        
        elif len(car_brand.get()) < 3:
            messagebox.showerror(title="Error", message= "Please Enter A Vaild Car Brand" )
        elif len(engine_type.get()) < 4:
            messagebox.showerror(title="Error", message= "Please Enter A Engine Type" )
            
            
            
        elif model_check:
            
            cursor.execute("INSERT INTO CARS_LISTED (OWNER,LOCATION,PRICE,DURATION,MODELID) VALUES (:OWNER,:LOCATION,:PRICE,:DURATION,:MODEL)",
                  {
                    
                    "OWNER":userid,
                    "LOCATION":location.get(),
                    "PRICE":price.get(),
                    "DURATION":Duration.get(),
                    "MODEL":model_check[0]
                    
                    
                    
                    
                     
                  })
            
            connect.commit()
            connect.close()
            
            
            
            messagebox.showinfo(title="Success", message="Car Has Successfully Been Listed!")
            clear_list()
            
            
            
        else:
            
        
            cursor.execute("INSERT INTO CAR_MODEL (BRAND,MODEL,ENGINE) VALUES (:BRAND,:MODEL,:ENGINE)",
                  {
                    
                    "BRAND":car_brand.get().upper(),
                    "MODEL":car_model.get().upper(),
                    "ENGINE":engine_type.get().upper()
                    
                    
                    
                     
                  })
            
                
            # connect.commit()
            new_car_id = cursor.lastrowid
            
            
            
            
            #cursor.execute("SELECT CARMODELID FROM CAR_MODEL WHERE BRAND = ? AND MODEL = ? AND ENGINE = ?",(car_brand.get(),car_model.get(),engine_type.get(),))
            
            
            
            #carid=cursor.fetchone()
            
            cursor.execute("INSERT INTO CARS_LISTED (OWNER,LOCATION,PRICE,DURATION,MODELID) VALUES (:OWNER,:LOCATION,:PRICE,:DURATION,:MODEL)",
                  {
                    
                    "OWNER":userid,
                    "LOCATION":location.get(),
                    "PRICE":price.get(),
                    "DURATION":Duration.get(),
                    "MODEL":new_car_id
                    
                    
                    
                    
                     
                  })
            
            connect.commit()
            connect.close()
            
            
            
            messagebox.showinfo(title="Success", message="Car Has Successfully Been Listed!")
            clear_list()
        
               

    
    def on_enter(e):
        car_brand.delete(0,"end")
    def on_leave(e):
        name=car_brand.get()
        if name=="":
            car_brand.insert(0,"Car Brand (e.g. Tesla)")

    car_brand= Entry(rent_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    car_brand.insert(0,"Car Brand(e.g. Tesla)")
    car_brand.pack(pady=5)
    car_brand.bind("<FocusIn>",on_enter)
    car_brand.bind("<FocusOut>",on_leave)
    
    Frame(rent_frame,width=540,height=2,bg="black").pack(pady=2)

    def on_enter(e):
        car_model.delete(0,"end")
    def on_leave(e):
        name=car_model.get()
        if name=="":
            car_model.insert(0,"Model (e.g. Tesla Model s)")
            
    car_model= Entry(rent_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    car_model.insert(0,"Model (e.g. Tesla Model s)")
    car_model.pack(pady=5)
    car_model.bind("<FocusIn>",on_enter)
    car_model.bind("<FocusOut>",on_leave)
    
    Frame(rent_frame,width=540,height=2,bg="black").pack(pady=2)
    
    def on_enter(e):
        location.delete(0,"end")
    def on_leave(e):
        name=location.get()
        if name=="":
            location.insert(0,"Address (City)")
    
    location= Entry(rent_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    location.insert(0,"Address (City)")
    location.pack(pady=5)
    location.bind("<FocusIn>",on_enter)
    location.bind("<FocusOut>",on_leave)
    
    Frame(rent_frame,width=540,height=2,bg="black").pack(pady=2)
    
    def on_enter(e):
        price.delete(0,"end")
    def on_leave(e):
        name=price.get()
        if name=="":
            price.insert(0,"Price")
    
    price= Entry(rent_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    price.insert(0,"Price")
    price.pack(pady=5)
    price.bind("<FocusIn>",on_enter)
    price.bind("<FocusOut>",on_leave)
    
    Frame(rent_frame,width=540,height=2,bg="black").pack(pady=2)
    
    def on_enter(e):
        Duration.delete(0,"end")
    def on_leave(e):
        name=Duration.get()
        if name=="":
            Duration.insert(0,"Duration(In Days)")
    
    Duration= Entry(rent_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    Duration.insert(0,"Duration (In Days)")
    Duration.pack(pady=5)
    Duration.bind("<FocusIn>",on_enter)
    Duration.bind("<FocusOut>",on_leave)
    
    Frame(rent_frame,width=540,height=2,bg="black").pack(pady=2)
    
    def on_enter(e):
        engine_type.delete(0,"end")
    def on_leave(e):
        name=engine_type.get()
        if name=="":
            engine_type.insert(0,"Engine Type (Manual or Automatic)")
    
    engine_type= Entry(rent_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    engine_type.insert(0,"Engine Type (Manual or Automatic)")
    engine_type.pack(pady=5)
    engine_type.bind("<FocusIn>",on_enter)
    engine_type.bind("<FocusOut>",on_leave)
    
    Frame(rent_frame,width=540,height=2,bg="black").pack(pady=2)
    
  
    rent_submit=tk.Button(rent_frame,text="List My Car!",font=(14),bg="#00B1FF",fg="White",border = 0,width=30,height=2,command=rent_info)
    rent_submit.pack(pady=10)
      
    
    rent_frame.pack(pady=20)


def bookings_page():
    
    bookings_frame = tk.Frame(main_frame)
    bookings_frame.configure(bg="#fff")
    lb = tk.Label(bookings_frame, text="My Bookings",font=("bold",30,"bold"),fg="#00B1FF",bg="#fff")
    lb.pack()
    bookings_frame.pack(pady=50)
    
    def review():
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        
        
        
        
        try:
            
            select_booking = bookings_tree.focus()
            booking_details= bookings_tree.item(select_booking)
            get_carid = booking_details.get("values")[1]
            print(get_carid)
           
            cursor.execute("SELECT GIVEN_BY,CARMODEL FROM REVIEWS WHERE GIVEN_BY=(:USERID) AND CARMODEL=(:CARID)",
                       {"USERID":userid,
                        "CARID":get_carid
                           })
            
            review_check = cursor.fetchall()
            
            
            
            
            
            if review_check:
                messagebox.showerror(title="Error", message="You have already given this car a review")
            
                
            
                
            else:               
                cursor.execute("INSERT INTO REVIEWS (GIVEN_BY,RATING,CARMODEL) VALUES(:GIVEN_BY,:RATING,:CARID)",
                               
                               {"GIVEN_BY":userid,
                                "RATING":rating.get(),
                                "CARID":get_carid
                                   
                                   
                                   })
                
                
                
                
                connect.commit()
                connect.close()
        except:
            messagebox.showerror(title="Error", message="Please Select The Car You Would Like To Review")
       
            
    
    def cancel():
        connect = sqlite3.connect("CAR DB.db")
        cursor = connect.cursor()
        try:
            select_booking = bookings_tree.focus()
            booking_details= bookings_tree.item(select_booking)
            get_bookingid = booking_details.get("values")[0]
            print(get_bookingid)
            
            select_booking = bookings_tree.focus()
            booking_details= bookings_tree.item(select_booking)
            get_carid = booking_details.get("values")[1]
            print(get_carid)
            
            cursor.execute("DELETE FROM BOOKINGS WHERE BOOKINGID = (:BOOKINGID)",
                           {"BOOKINGID":get_bookingid
                               })
            
            
            cursor.execute("UPDATE CARS_LISTED SET BOOKED = 'FALSE' WHERE CARID = (:CARID)",
                               {"CARID":get_carid
                                   
                                   
                                })
            
            connect.commit()
            connect.close()
            bookings_tree.delete(select_booking)
        except:
            messagebox.showerror(title="Error", message="Please Select The Booking You Would Like To Cancel")
        
        
    connect = sqlite3.connect("CAR DB.db")
    cursor = connect.cursor()
   
    
    bookings_tree = ttk.Treeview(bookings_frame, height=15,selectmode="browse")
    bookings_tree["columns"]=("ID","CARID","Pick Up Location","Duration","Price")
    bookings_tree.column("#0",width = 0,stretch = NO)
    
    bookings_tree.column("ID",width = 300,anchor = W)
    bookings_tree.column("CARID",width = 0,stretch = NO)
    bookings_tree.column("Pick Up Location",width = 300,anchor = W)
    bookings_tree.column("Duration",width = 300,anchor = W)
    bookings_tree.column("Price",width = 300,anchor = W)
    
    
    bookings_tree.heading("#0",text="",anchor=W)
    
    bookings_tree.heading("ID",text="ID",anchor=W)
    bookings_tree.heading("CARID",text="",anchor=W)
    bookings_tree.heading("Pick Up Location",text="Pick Up Location",anchor=W)
    bookings_tree.heading("Duration",text="Duration",anchor=W)
    bookings_tree.heading("Price",text="Price in £",anchor=W)
        
    bookings_tree.pack(pady=5)
    

    cursor.execute("""SELECT BOOKINGID,CARID,ADDRESS,DURATION,PRICE
FROM BOOKINGS
INNER JOIN CARS_LISTED ON BOOKINGS.CAR=CARS_LISTED.CARID
INNER JOIN USER_INFO ON CARS_LISTED.OWNER=USER_INFO.USERID
WHERE CUSTOMER = (:USER)

""",{"USER":userid
    
    
    })
        
    booking_result = cursor.fetchall()
    print(booking_result)
        
    for row in booking_result:
        
        bookings_tree.insert("",tk.END, values=row)
        
    
        
    else:
        pass
    
    cancel_button=Button(bookings_frame,width=30,height=2,text="CANCEL ORDER",font=(14),bg="#00B1FF",fg="white",border = 0,command = cancel).pack(pady=30)
    return_button=Button(bookings_frame,width=30,height=2,text="RETURN CAR",font=(14),bg="#00B1FF",fg="white",border = 0,command = cancel).pack(pady=5)
    
    rating_label = tk.Label(bookings_frame, text="Rate Your Car",font=("bold",16),fg="Black",bg="#fff").pack(pady=30)
    def on_enter(e):
        rating.delete(0,"end")
    def on_leave(e):
        name=rating.get()
        if name=="":
            rating.insert(0,"Enter a number from 1-10")
    
    rating= Entry(bookings_frame,width=40,font=("Microsoft YaHei UI Light",18),bd=0)
    rating.pack(pady=5)
    rating.insert(0,"Enter a number from 1-10")
    rating.bind("<FocusIn>",on_enter)
    rating.bind("<FocusOut>",on_leave)
    
    
    
    Frame(bookings_frame,width=540,height=2,bg="black").pack(pady=2)
    cancel_button=Button(bookings_frame,width=30,height=2,text="SUBMIT RATING",font=(14),bg="#00B1FF",fg="white",border = 0,command = review).pack(pady=20)
def reviews_page():
    reviews_frame = tk.Frame(main_frame)
    reviews_frame.configure(bg="#fff")
    lb = tk.Label(reviews_frame, text="REVIEWS",font=("bold",30,"bold"),fg="#00B1FF",bg="#fff")
    lb.pack()
    reviews_frame.pack(pady=50)
    
    reviews_tree = ttk.Treeview(reviews_frame, height=40,selectmode="browse")
    reviews_tree["columns"]=("BRAND","MODEL","ENGINE","RATING","USERNAME")
    reviews_tree.column("#0",width = 0,stretch = NO)
    reviews_tree.column("BRAND",width = 200,anchor = W)
    reviews_tree.column("MODEL",width = 200,stretch = NO)
    reviews_tree.column("ENGINE",width = 200,anchor = W)
    reviews_tree.column("RATING",width = 200,anchor = W)
    reviews_tree.column("USERNAME",width = 200,anchor = W) 
    reviews_tree.heading("#0",text="",anchor=W)    
    reviews_tree.heading("BRAND",text="Brand",anchor=W)
    reviews_tree.heading("MODEL",text="Model",anchor=W)
    reviews_tree.heading("ENGINE",text="Engine Type",anchor=W)
    reviews_tree.heading("RATING",text="Rating",anchor=W)
    reviews_tree.heading("USERNAME",text="Username",anchor=W)
    reviews_tree.pack(pady=5)
    
    connect = sqlite3.connect("CAR DB.db")
    cursor = connect.cursor()
    
    cursor.execute("""SELECT BRAND,MODEL,ENGINE,RATING,USERNAME
FROM REVIEWS
INNER JOIN CARS_LISTED ON REVIEWS.CARMODEL = CARS_LISTED.CARID
INNER JOIN CAR_MODEL ON CARS_LISTED.MODELID = CAR_MODEL.CARMODELID
INNER JOIN USER_INFO ON REVIEWS.GIVEN_BY = USER_INFO.USERID
ORDER BY RATING DESC
""")
    
    reviews_result = cursor.fetchall()
    
    for row in reviews_result:
        
        reviews_tree.insert("",tk.END, values=row)
       
    
    
    
    #pages_end
def hide_indicators():
    home_indicate.config(bg="#00B1FF")
    hire_indicate.config(bg="#00B1FF")
    rent_indicate.config(bg="#00B1FF")
    join_indicate.config(bg="#00B1FF")
    #locations_indicate.config(bg="#00B1FF")
    reviews_indicate.config(bg="#00B1FF")    
    bookings_indicate.config(bg="#00B1FF")

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
        
   
    
def indicate(lb,page):
    hide_indicators()
    lb.config(bg="White")
    delete_pages()
    page()
#functions_end   

menu_frame = tk.Frame(root,bg="#00B1FF")

#Buttons_start

home_button =tk.Button(menu_frame,text="HOME",font=('Bold', 15, 'bold'),fg="White",bd=0,bg="#00B1FF",command=lambda:indicate(home_indicate,home_page))
home_button.place(x=20,y=100)
home_indicate= tk.Label(menu_frame,text="",bg="#00B1FF")
home_indicate.place (x=5, y=100,width= 8,height=40)

join_button =tk.Button(menu_frame,text="JOIN",font=('Bold', 15, 'bold'),fg="White",bd=0,bg="#00B1FF",command=lambda:indicate(join_indicate,signup_page))
join_button.place(x=20,y=150)
join_indicate= tk.Label(menu_frame,text="",bg="#00B1FF")
join_indicate.place (x=5, y=150,width= 8,height=40)

hire_button =tk.Button(menu_frame,text="HIRE A CAR",font=('Bold', 15, 'bold'),fg="White",bd=0,bg="#00B1FF",command=lambda:indicate(hire_indicate,hire_page))
hire_button.place(x=20,y=200)
hire_indicate= tk.Label(menu_frame,text="",bg="#00B1FF")
hire_indicate.place (x=5, y=200,width= 8,height=40)

rent_button =tk.Button(menu_frame,text="LIST YOUR CAR",font=('Bold', 15, 'bold'),fg="White",bd=0,bg="#00B1FF",command=lambda:indicate(rent_indicate,rent_page))
rent_button.place(x=20,y=250)
rent_indicate= tk.Label(menu_frame,text="",bg="#00B1FF")
rent_indicate.place (x=5, y=250,width= 8,height=40)

bookings_button =tk.Button(menu_frame,text="MY BOOKINGS",font=('Bold', 15, 'bold'),fg="White",bd=0,bg="#00B1FF",command=lambda:indicate(bookings_indicate,bookings_page))
bookings_button.place(x=20,y=300)
bookings_indicate= tk.Label(menu_frame,text="",bg="#00B1FF")
bookings_indicate.place (x=5, y=300,width= 8,height=40)

reviews_button =tk.Button(menu_frame,text="RATINGS",font=('Bold', 15, 'bold'),fg="White",bd=0,bg="#00B1FF",command=lambda:indicate(reviews_indicate,reviews_page))
reviews_button.place(x=20,y=350)
reviews_indicate= tk.Label(menu_frame,text="",bg="#00B1FF")
reviews_indicate.place (x=5, y=350,width= 8,height=40)


exit_button =tk.Button(menu_frame,command=root.destroy,text="EXIT",font=('Bold', 15, 'bold'),fg="White",bd=0,bg="#00B1FF")
exit_button.place(x=20,y=400)
#Buttons_end
menu_frame.pack(side=tk.LEFT)
menu_frame.pack_propagate(False)
menu_frame.configure(width = 200,height = 1080)


main_frame=tk.Frame(root)
main_frame.configure(bg="#fff")
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width = 1920,height = 1080)

home_page()
root.mainloop()
