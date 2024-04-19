import sqlite3

def create_connection(hw_db):
    conn = None
    try:
        conn = sqlite3.connect(hw_db)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            product_title TEXT NOT NULL,
                            price NUMERIC(10, 2) DEFAULT 0.0 NOT NULL,
                            quantity INTEGER DEFAULT 0 NOT NULL
                        )''')
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, product_title, price, quantity):
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO products (product_title, price, quantity) 
                          VALUES (?, ?, ?)''', (product_title, price, quantity))
        conn.commit()
        print("Product added successfully")
    except sqlite3.Error as e:
        print(e)

def add_multiple_products(conn):
    products = [
        ("Product 1", 10.99, 50),
        ("Product 2", 20.49, 30),
        ("Product 3", 5.99, 100),
        ("Product 4", 15.75, 20),
    ]
    for product in products:
        insert_product(conn, *product)

def update_quantity(conn, product_id, quantity):
    try:
        cursor = conn.cursor()
        cursor.execute('''UPDATE products 
                          SET quantity = ? 
                          WHERE id = ?''', (quantity, product_id))
        conn.commit()
        print("Quantity updated successfully")
    except sqlite3.Error as e:
        print(e)

def update_price(conn, product_id, price):
    try:
        cursor = conn.cursor()
        cursor.execute('''UPDATE products 
                          SET price = ? 
                          WHERE id = ?''', (price, product_id))
        conn.commit()
        print("Price updated successfully")
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, product_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM products 
                          WHERE id = ?''', (product_id,))
        conn.commit()
        print("Product deleted successfully")
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM products''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_specific_products(conn, limit_price, limit_quantity):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM products 
                          WHERE price < ? AND quantity > ?''', (limit_price, limit_quantity))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def search_products(conn, keyword):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM products 
                          WHERE product_title LIKE ?''', ('%'+keyword+'%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    db_name = 'hw.db'
    conn = create_connection(db_name)
    if conn is not None:
        create_table(conn)
        add_multiple_products(conn)
        select_all_products(conn)
        update_quantity(conn, 1, 60)
        update_price(conn, 2, 25.99)
        delete_product(conn, 3)
        select_specific_products(conn, 100, 5)
        search_products(conn, "мыло")
        conn.close()
