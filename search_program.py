import PySimpleGUI as sg
import sqlite3


def get_products_by_category(category):
    """Retrieves all products in a specified category"""
    # Connect to the database
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    # Query the database for products in the specified category
    c.execute("SELECT * FROM products WHERE category = ?", (category,))
    products = c.fetchall()
    conn.close()
    for product in products:
        print(product)

    if len(products) == 0:
        sg.Popup('No products found')

    # show the products in a table
    layout = [
        [sg.Text('Products in Category {}'.format(products))]]
    for product in products:
        layout.append([sg.Text(product[0]), sg.Text(product[1]), sg.Text(
            str(product[2])), sg.Text(str(product[3]))])
    layout.append([sg.Button('OK')])
    window = sg.Window('Products in Category', layout)
    window.read()
    window.close()
    # close the database connection
    conn.close()
