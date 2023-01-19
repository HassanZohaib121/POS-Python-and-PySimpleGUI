import sqlite3
import PySimpleGUI as sg
from search import *

# create our sqlite3 database
conn = sqlite3.connect('products.db')
c = conn.cursor()

# create the table to store product information
try:
    c.execute('CREATE TABLE products (code TEXT PRIMARY KEY, name TEXT, price REAL, quantity INTEGER, category TEXT)')
except sqlite3.OperationalError:
    # table already exists
    pass

# create a window to enter product information
layout = [[sg.Text('Code'), sg.InputText(key='code')],
          [sg.Text('Name'), sg.InputText(key='name')],
          [sg.Text('Price'), sg.InputText(key='price')],
          [sg.Text('Quantity'), sg.InputText(key='quantity')],
          [sg.Text('Category'), sg.InputText(key='category')],
          [sg.Button('Add Product'), sg.Button('Cancel'), sg.Button('Search by Code'), sg.Button('Search by Category')]]

# show the window
window = sg.Window('Add Product', layout)

# event loop to add products
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'Add Product':
        # check if a product with the same code exists
        c.execute('SELECT * FROM products WHERE code=?', (values['code'],))
        if c.fetchone() is not None:
            sg.Popup('Product code already exists')
            continue
        c.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?)',
                  (values['code'], values['name'], values['price'], values['quantity'], values['category']))
        conn.commit()
        sg.Popup('Product added')
    elif event == 'Search by Code':
        product_code_search()
    elif event == 'Search by Category':
        product_category_search()

window.close()
