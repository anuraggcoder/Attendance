import tkinter as tk
from tkinter import ttk
from RecordManip import *
import shelve
import pandas as pd
from pandastable import Table, TableModel


def Display_Record():
    root_new_rec = tk.Tk()
    root_new_rec.geometry('500x600')
    root_new_rec.columnconfigure(0, weight=1)
    root_new_rec.resizable(False,False)
    display = tk.StringVar()
    disp = tk.StringVar()
    

    # This line reads the Name of person from 'Employees' file and then
    # loads it for the Combo Box named 'menu' here via 'new_values' variable
    db = shelve.open('Employees')
    new_values = [f"{i}" for i in db]
    db.close()
    
    banner = ttk.Label(root_new_rec, text='Display Record Page', font=('Verdana', 32))
    banner.grid(row=0, column=0, pady=(10,10))

    root_frame = tk.Frame(root_new_rec)
    root_frame.grid(row=1, column=0, sticky='EW')

    table_frame = tk.Frame(root_new_rec)
    table_frame.grid(row=2, column=0, sticky='EW')
    table_frame.rowconfigure(0, weight=1)

    '''
    Below 4 lines are very important as they displays ugly looking Panda's
    Dataa Frame into a nice and visually appealing table. For this, we have
    used 'pandastable library' and its 'Table' method to create a Table widget.
    Creation is similar to tkinter style.
    '''
    table = Table(table_frame, dataframe=df, showtoolbar=False, showstatusbar=False, parentframe=table_frame)
    table.height = 650 # This controlls the height of table 
    table.grid(row=0, column=0, sticky='NSEW') 

    root_new_rec.rowconfigure(2, weight=1)

    def PrintRecord():
        '''
        Don't know why this function is not taking the values from variable:
        name, year and months. That's why I'm using menu.get(), menu2.get() and
        menu3.get(). If you happen to find the reason then please update
        '''
        df = displayrecord(menu.get(), int(menu2.get()), menu3.get())

        '''
        We could have created the 'Table' widget here but then it would mean that
        each time the 'Submit' button is pressed, the widget would have been
        redrawn again, this would be expensive. Hence, this function is updating
        the Data Frame using its 'updateModel' method and others
        '''
        table.updateModel(TableModel(dataframe=df))
        table.show()
        table.redraw()
        

    name = tk.StringVar()
    year = tk.IntVar()
    months = tk.StringVar()
    
    # Label and Combo Box for selecting the name
    message = ttk.Label(root_frame, text='Select the name: ')
    message.grid(row=0, column=0)

    menu = ttk.Combobox(root_frame, textvariable=name)
    menu.grid(row=0, column=1, sticky='EW')
    menu["state"] = 'readonly'
    menu['values'] = new_values

    # Label and Combo Box for selecting the year
    message2 = ttk.Label(root_frame, text='Select the Year: ')
    message2.grid(row=1, column=0)

    menu2 = ttk.Combobox(root_frame, textvariable=year)
    menu2.grid(row=1, column=1, sticky='EW')
    menu2["state"] = 'readonly'
    menu2['values'] = [2023, 2024,2025]

    # Label and Combo Box for selecting the month
    message3 = ttk.Label(root_frame, text='Select the Month: ')
    message3.grid(row=2, column=0)

    menu3 = ttk.Combobox(root_frame, textvariable=months)
    menu3.grid(row=2, column=1, sticky='EW')
    menu3["state"] = 'readonly'
    menu3['values'] = ['January', 'February','March','April','May','June','July','August','September','October','November', 'December']

    
    submit = ttk.Button(root_frame, text = 'Submit', command = PrintRecord)
    submit.grid(row=3, column=0, columnspan=2, sticky='EW', pady=(10,0))

    close = ttk.Button(root_frame, text = 'Close', command=root_new_rec.destroy)
    close.grid(row=4, column=0, columnspan=2, sticky='EW', pady=(10,0))

             
    root_new_rec.mainloop()
    

if __name__ == '__main__':
    Display_Record()
