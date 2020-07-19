from tkinter import *

# Create Window object
app = Tk()

app.title('Part Manager')
app.geometry('600x300')

# Part
part_text = StringVar()
part_label = Label(app, text='Part Name', pady=20, padx=10)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', pady=20, padx=10)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', padx=10)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_label = Label(app, text='Price', padx=10)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# Parts List
parts_list = Listbox(app, height=8, width=50, border=1)
parts_list.grid(row=3, column=0, rowspan=6, columnspan=3, pady=20, padx=20)

# Create Scrollbar
scrollbar = Scrollbar(app, border=1)
scrollbar.grid(row=3, column=3)

# Set scrollbar to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Buttons
add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1, pady=20)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2, pady=20)

clear_btn = Button(app, text='Clear Part', width=12, command=clear_item)
clear_btn.grid(row=2, column=3, pady=20)

# Start program
app.mainloop()
