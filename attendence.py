import tkinter as tk
from tkinter import ttk
from NewRecord import New_Record, Return_value
from UpdateRecord import updateRecord
from DisplayRecords import Display_Record
from Summary import total_no_of_present

root = tk.Tk()
root.geometry('600x400')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=8)
userdata = None


# Create a PanedWindow to split the window into two parts
pane = ttk.Panedwindow(root, orient='horizontal')
pane.grid(row=0, column=0, sticky='nsew')


# For Aside
frame1 = tk.Frame(pane, bg='green')
pane.add(frame1, weight=1)

new_record = ttk.Button(frame1, text= 'New Record', command=New_Record)
new_record.grid(row=0, column=0, sticky='EW', pady=(10,5), ipadx=5, ipady=5)

update_attendance = ttk.Button(frame1, text= 'Update Attendance', command=updateRecord)
update_attendance.grid(row=1, column=0, sticky='EW', pady=(0,5), ipadx=5, ipady=5)

display_record = ttk.Button(frame1, text= 'Display Record', command=Display_Record)
display_record.grid(row=2, column=0, sticky='EW', pady=(0,5), ipadx=5, ipady=5)

about = ttk.Button(frame1, text= 'About')
about.grid(row=3, column=0, sticky='EW', pady=(0,5), ipadx=5, ipady=5)

exit_app = ttk.Button(frame1, text= 'Exit', command=root.destroy)
exit_app.grid(row=4, column=0, sticky='EW', pady=(0,5), ipadx=5, ipady=5)


# Calculating Data for display

presence = total_no_of_present()


least_presence = min(presence.values())
most_presence = max(presence.values())
sum_p = 0

for name,present in presence.items():
    if present == least_presence:
        most_leave_by = f"{name} : {present}%"
    if present == most_presence:
        least_leave_by = f"{name} : {present}%"
    sum_p += float(present)


average = sum_p/len(presence.values())
average_presence = '{0:.2f}%'.format(average)


# For Summary Display
frame2 = tk.Frame(pane)
pane.add(frame2, weight=8)

summary = ttk.Label(frame2, text='SUMMARY', font=('Verdana',36))
summary.grid(row=0, column=0)

label1 = ttk.Label(frame2, text ='For the last Month')
label1.grid(row=1, column=0, sticky='EW', ipady=16)

label2 = ttk.Label(frame2, text ='Average Presence: ')
label2.grid(row=2, column=0, sticky='EW', ipady=16)
average_disp = ttk.Label(frame2, text =average_presence)
average_disp.grid(row=2, column=1, sticky='EW', ipady=16)

label3 = ttk.Label(frame2, text ='Maximum Presence in the Office was of')
label3.grid(row=3, column=0, sticky='EW', ipady=16)
leastleave = ttk.Label(frame2, text =least_leave_by)
leastleave.grid(row=3, column=1, sticky='EW', ipady=16)

label4 = ttk.Label(frame2, text ='Minimum Presence in the Office was of')
label4.grid(row=4, column=0, sticky='EW')
mostleave = ttk.Label(frame2, text =most_leave_by)
mostleave.grid(row=4, column=1, sticky='EW', ipady=16)

root.mainloop()

