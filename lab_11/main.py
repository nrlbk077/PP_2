import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook1",
    user="postgres",
    password="nrlbk777",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)
    conn.commit()

def insert_from_csv():
    filename = input("Path to CSV: ")
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Successful CSV import.")

def insert_from_input():
    name = input("Insert name: ")
    phone = input("Insert phone number: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("User added or updated via procedure.")

def update_user():
    old_name = input("Insert name to update: ")
    new_name = input("New name (press Enter to skip): ")
    new_phone = input("New phone number (press Enter to skip): ")

    if new_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, new_name or old_name))
    conn.commit()
    print("Data updated.")

def query_data():
    print("1. Show all\n2. Search by name\n3. Search by phone\n4. Pattern search")
    choice = input("Choice: ")

    if choice == '1':
        cur.execute("SELECT * FROM phonebook")
    elif choice == '2':
        name = input("Insert name: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    elif choice == '3':
        phone = input("Insert phone number: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    elif choice == '4':
        pattern = input("Enter part of name or phone: ")
        pattern = f"%{pattern}%"
        cur.execute("""
            SELECT * FROM phonebook
            WHERE first_name ILIKE %s OR phone ILIKE %s
        """, (pattern, pattern))
    else:
        print("Wrong choice")
        return

    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user():
    print("Delete by:\n1. Name\n2. Phone")
    choice = input("Choice: ")

    if choice == '1':
        name = input("Insert name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif choice == '2':
        phone = input("Insert phone number: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    else:
        print("Wrong choice")
        return
    conn.commit()
    print("User deleted.")


def menu():
    create_table()
    while True:
        print("\n=== PHONEBOOK ===")
        print("1. Add from CSV")
        print("2. Add manually (with procedure)")
        print("3. Update user")
        print("4. Search")
        print("5. Delete user")
        
        print("0. Exit")

        choice = input("Choice: ")

        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_input()
        elif choice == '3':
            update_user()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_user()
       
        elif choice == '0':
            break
        else:
            print("Wrong choice.")

    cur.close()
    conn.close()
    print("Exiting program.")

if __name__ == "__main__":
    menu()
