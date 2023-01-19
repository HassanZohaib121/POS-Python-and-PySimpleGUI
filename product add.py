import PySimpleGUI as sg
import sqlite3
from catagory_spin import category_search

# create a connection to the database
conn = sqlite3.connect('products.db')
c = conn.cursor()

# create the table for product info
c.execute('''CREATE TABLE IF NOT EXISTS products
            (code TEXT PRIMARY KEY, 
            name TEXT, 
            price REAL, 
            quantity INTEGER, 
            category TEXT
            )
            ''')

# create the GUI
layout = [[sg.Text('Product Code'), sg.InputText()],
          [sg.Text('Name'), sg.InputText()],
          [sg.Text('Price'), sg.InputText()],
          [sg.Text('Quantity'), sg.InputText()],
          [sg.Text('Category'), sg.InputText()],
          [sg.Button('Add Product'), sg.Button('Search')]]

window = sg.Window('Product Management System', layout)

# loop to process events
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Add Product':
        # add the product to the database
        c.execute('''INSERT INTO products(code, name, price, quantity, category) 
                    VALUES (?, ?, ?, ?, ?)''',
                  (values[0], values[1], values[2], values[3], values[4]))
        conn.commit()
    elif event == 'Search':
        # search for the product
        category_search()

# close the database connection
conn.close()
