import sqlite3
import PySimpleGUI as sg


def product_code_search():
    # connect to the database
    conn = sqlite3.connect('products.db')
    # create a cursor
    c = conn.cursor()
    # create a table for storing product details
    c.execute(
        "CREATE TABLE IF NOT EXISTS Product (Code TEXT, Name TEXT, Price REAL, Quantity INTEGER)")
    conn.commit()

    # create a window to show product information
    layout = [[sg.Text('Product Code'), sg.InputText(key='code')],
              [sg.Button('Search'), sg.Button('Cancel')]]
    window = sg.Window('Show Product', layout)

    # event loop to show product information
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        elif event == 'Search':
            # search for the product with the given code
            c.execute('SELECT * FROM products WHERE code=?', (values['code'],))
            product = c.fetchone()
            if product is None:
                sg.Popup('No product found')
                continue
            # show the product information in a table
            layout = [[sg.Text('Product Information')],
                      [sg.Text('Code'), sg.Text(product[0], key='code')],
                      [sg.Text('Name'), sg.Text(product[1], key='name')],
                      [sg.Text('Price'), sg.Text(
                          str(product[2]), key='price')],
                      [sg.Text('Quantity'), sg.Text(
                          str(product[3]), key='quantity')],
                      [sg.Text('Category'), sg.Text(
                          product[4], key='category')],
                      [sg.Button('OK')]]
            window2 = sg.Window('Product Information', layout)
            window2.read()
            window2.close()

    window.close()
    # close the database connection
    conn.close()


def product_category_search():
    # connect to the database
    conn = sqlite3.connect('products.db')
    # # create a cursor
    c = conn.cursor()
    # # create a table for storing product details
    # c.execute(
    #     "CREATE TABLE IF NOT EXISTS Product (Code TEXT, Name TEXT, Price REAL, Quantity INTEGER)")
    # conn.commit()

    c.execute("SELECT category FROM products")
    # fetch all rows from the table
    rows = c.fetchall()
    # create list of column names
    column_names = [i[0] for i in rows]

    # [sg.Text('Category'), sg.InputText(key='category')],
    # create a window to show products in each category
    layout = [[sg.Spin(values=column_names, s=16, key='category')],
              [sg.Button('Show Products'), sg.Button('Cancel')]
              ]

    window = sg.Window('Show Products', layout)

    # event loop to show products in each category
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        elif event == 'Show Products':
            # search for the products in the given category
            c.execute('SELECT * FROM products WHERE category=?',
                      (values['category'],))
            products = c.fetchall()
            if len(products) == 0:
                sg.Popup('No products found')
                continue
                # show the products in a table
            layout = [
                [sg.Text('Products in Category {}'.format(values['category']))]]
            for product in products:
                layout.append([sg.Text(product[0]), sg.Text(product[1]),
                               sg.Text(str(product[2])), sg.Text(str(product[3]))])
            layout.append([sg.Button('OK')])
            window2 = sg.Window('Products in Category', layout)
            window2.read()
            window2.close()


        window.close()

        # close the database connection
        conn.close()
