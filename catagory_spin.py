import PySimpleGUI as sg
import sqlite3
from search_program import get_products_by_category

# create connection to database
conn = sqlite3.connect('products.db')

# create cursor
c = conn.cursor()


def category_search():
    try:
        # execute query
        c.execute("SELECT category FROM products")
        # fetch all rows from the table
        rows = c.fetchall()
        # create list of column names
        column_names = [i[0] for i in rows]
        # create layout
        layout = [
            [sg.Text('Select a Category')],
            [sg.Spin(values=column_names, s=16, key='-CATEGORY-')],
            [sg.OK(s=16), sg.Cancel(s=16)]
        ]
        # create window
        window = sg.Window('Select Column Name', layout)
        # read values
        event, values = window.read()
        category = values['-CATEGORY-']

        if event == 'OK':
            get_products_by_category(category)

    except sqlite3.OperationalError as e:
        print("An error occured: ", e)
    finally:
        # close cursor and connection
        c.close()
        conn.close()

        # close the window
        window.close()
