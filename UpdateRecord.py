import tkinter as tk
from tkinter import ttk
import shelve
import CsvChecker



def updateRecord():
    root_update_attendance = tk.Tk()
    root_update_attendance.geometry('600x400') 
    name = tk.StringVar()
    month_name = tk.StringVar()
    month_day = tk.IntVar()
    year_name = tk.IntVar()
    month_att = tk.StringVar()

    def attendance():
        
        selected_name = menu.get()
        selected_year = year.get()
        selected_month = month.get()
        selected_day = day.get()
        selected_att = att.get()
        
        CsvChecker.check_csv(selected_name, selected_year, selected_month,
                             selected_day, selected_att)
    
    # Defining a Drop down menu to select name    
    label_name = ttk.Label(root_update_attendance,
                           text='Select Name to enter attendance for:')
    label_name.grid(row=0, column=0, sticky='EW')

    menu = ttk.Combobox(root_update_attendance, textvariable=name)
    menu.grid(row=0, column=1, sticky='EW')

    # Defining a Drop down menu to select year
    label_year = ttk.Label(root_update_attendance,
                           text='Select Year:')
    label_year.grid(row=1, column=0, sticky='EW')
    
    year = ttk.Combobox(root_update_attendance, textvariable=year_name)
    year.grid(row=1, column=1, sticky='EW')
    year["values"] = (2023,2024, 2025)

    # Defining a Drop down menu to select month
    label_month = ttk.Label(root_update_attendance,
                           text='Select Month:')
    label_month.grid(row=2, column=0, sticky='EW')
    
    month = ttk.Combobox(root_update_attendance, textvariable=month_name)
    month.grid(row=2, column=1, sticky='EW')
    month["values"] = ('January', 'February','March','April','May','June',
                       'July','August','September','October','November',
                       'December')

    # Defining a Drop down menu to select Date
    label_day = ttk.Label(root_update_attendance,
                           text='Select Day:')
    label_day.grid(row=3, column=0, sticky='EW')
    
    day = ttk.Combobox(root_update_attendance, textvariable=month_day)
    day.grid(row=3, column=1, sticky='EW')
    a = list(range(1,32))
    day["values"] = (a)

    # Defining a Drop down menu to select attendance
    label_att = ttk.Label(root_update_attendance,
                           text='Select Attendance:')
    label_att.grid(row=4, column=0, sticky='EW')
    
    att = ttk.Combobox(root_update_attendance, textvariable=month_att)
    att.grid(row=4, column=1, sticky='EW')
    att["values"] = ('A','P')

    # Defining Submit Button
    submit_button = ttk.Button(root_update_attendance, text= 'Submit Record',
                               command=attendance)
    submit_button.grid(row=5, column=0, sticky='EW', pady=(10,5), ipadx=5, ipady=5)

    close = ttk.Button(root_update_attendance, text= 'Done with Update',
                       command=root_update_attendance.destroy)
    close.grid(row=6, column=0, sticky='EW', pady=(0,5), ipadx=5, ipady=5)
    

    
    # Database to store Employees name
    db1 = shelve.open('Employees')
    

    # Initializing the name and loading it to the 'menu' which contains name
    # of employees obtained from 'NewRecord' module
    new_values = [f"{i}" for i in db1]
    menu['values'] = new_values 
    
    db1.close()
    menu["state"] = 'readonly'
    

    '''
    Removed these lines because they are triggering the attendance
    function for each Combo Box sepearately:
    menu.bind("<<ComboboxSelected>>", attendance)
    year.bind("<<ComboboxSelected>>", attendance)
    month.bind("<<ComboboxSelected>>", attendance)
    day.bind("<<ComboboxSelected>>", attendance)
    att.bind("<<ComboboxSelected>>", attendance)
    '''

    root_update_attendance.mainloop()





if __name__ == '__main__':
    #check_if_record_update()
    #print(check_if_record_update().__doc__)
    updateRecord()
    
