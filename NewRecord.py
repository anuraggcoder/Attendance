import shelve
import tkinter as tk
from tkinter import ttk
from csv import writer
    
user_name = ''
db = open('Employee.csv','a')
record_writer = writer(db)

def Return_value():
    return user_name

def New_Record():
    root_new_rec = tk.Tk()
    root_new_rec.geometry('450x300')
    root_new_rec.resizable(False,False)

        
    banner = ttk.Label(root_new_rec, text='New Record Page', font=('Verdana', 32))
    banner.grid(row=0, column=0, pady=(10,10))


    root_frame = tk.Frame(root_new_rec)
    root_frame.grid(row=1, column=0, sticky='EW')

    message = ttk.Label(root_frame, text='Enter the name: ')
    message.grid(row=0, column=0)


    Name = tk.StringVar()
    new_name = ttk.Entry(root_frame, width='20')
    new_name.grid(row=0, column=1, padx=(10,0))


    # This function takes the name entered by user and updates it to
    # a Database file named 'AttendanceRegister' which intializes
    # the name with a dictionary having attendance record for given
    # month with 'None' value
    def Update_Record():
        global user_name
        user_name = new_name.get()
        db = shelve.open('Employees')
        db[user_name] = user_name
        db.close()
        
        
        

    submit = ttk.Button(root_frame, text = 'Submit', command=Update_Record)
    submit.grid(row=1, column=0, columnspan=2, sticky='EW', pady=(10,0))

    close = ttk.Button(root_frame, text = 'Close', command=root_new_rec.destroy)
    close.grid(row=2, column=0, columnspan=2, sticky='EW', pady=(10,0))

             
    root_new_rec.mainloop()
    print('New Record Page closed')
    

if __name__ == '__main__':
    New_Record()
