import psycopg2
import csv
from tabulate import tabulate

# Подключение к базе данных
conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres", password="point0000", port=5432)
cur = conn.cursor()

# Создание таблицы phonebook
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL
)
""")

# Создание необходимых функций и процедур в PostgreSQL

# Функция для поиска по шаблону
cur.execute("""
CREATE OR REPLACE FUNCTION search_phonebook(template TEXT)
RETURNS TABLE(user_id INT, name VARCHAR, surname VARCHAR, phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT user_id, name, surname, phone
    FROM phonebook
    WHERE name LIKE '%' || template || '%'
       OR surname LIKE '%' || template || '%'
       OR phone LIKE '%' || template || '%';
END;
$$ LANGUAGE plpgsql;
""")

# Процедура для вставки нового пользователя или обновления телефона, если пользователь уже существует
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_or_update_user(name TEXT, surname TEXT, phone TEXT)
AS
$$
BEGIN
    INSERT INTO phonebook (name, surname, phone)
    VALUES (name, surname, phone)
    ON CONFLICT (name, surname) 
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$ LANGUAGE plpgsql;
""")

# Процедура для вставки большого количества пользователей с проверкой телефона
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_bulk_users(users TEXT[])
AS
$$
DECLARE
    user RECORD;
    is_valid BOOLEAN;
BEGIN
    FOR user IN ARRAY users LOOP
        -- Проверяем корректность номера телефона (например, длина 10 символов)
        is_valid := LENGTH(user.phone) = 10;
        IF is_valid THEN
            INSERT INTO phonebook (name, surname, phone)
            VALUES (user.name, user.surname, user.phone);
        ELSE
            RAISE NOTICE 'Invalid phone number for user: % %', user.name, user.surname;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
""")

# Функция для пагинации
cur.execute("""
CREATE OR REPLACE FUNCTION get_paginated_data(limit INT, offset INT)
RETURNS TABLE(user_id INT, name VARCHAR, surname VARCHAR, phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT user_id, name, surname, phone
    FROM phonebook
    LIMIT limit OFFSET offset;
END;
$$ LANGUAGE plpgsql;
""")

# Процедура для удаления по имени или телефону
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user_by_name_or_phone(name TEXT, phone TEXT)
AS
$$
BEGIN
    DELETE FROM phonebook
    WHERE name = name OR phone = phone;
END;
$$ LANGUAGE plpgsql;
""")

# Функция для добавления пользователя в таблицу
def insert_data():
    print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter a file path with proper extension: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", tuple(row))

# Функция для обновления данных
def update_data():
    column = input('Type the name of the column that you want to change: ')
    value = input(f"Enter {column} that you want to change: ")
    new_value = input(f"Enter the new {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()

# Функция для удаления данных
def delete_data():
    phone = input('Type phone number which you want to delete: ')
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

# Функция для запроса данных
def query_data():
    column = input("Type the name of the column which will be used for searching data: ")
    value = input(f"Type {column} of the user: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {column} = %s", (value,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))

# Функция для отображения всех данных
def display_data():
    cur.execute("SELECT * from phonebook;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

# Функция для поиска по шаблону
def search_by_template():
    template = input("Enter the template (part of name, surname, or phone): ")
    cur.execute("SELECT * FROM search_phonebook(%s)", (template,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))

# Функция для вставки большого количества данных
def insert_bulk_users():
    users = []  # Пример: список кортежей с данными
    # Допустим, ты загружаешь их из CSV или как-то иначе
    cur.execute("CALL insert_bulk_users(%s)", (users,))
    conn.commit()

# Функция для получения пагинированных данных
def get_paginated_data():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_paginated_data(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))

# Функция для удаления данных по имени или телефону
def delete_user():
    name_or_phone = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_user_by_name_or_phone(%s, %s)", (name_or_phone, name_or_phone))
    conn.commit()

# Основное меню
while True:
    print("""
    List of the commands:
    1. Type "i" or "I" in order to INSERT data to the table.
    2. Type "u" or "U" in order to UPDATE data in the table.
    3. Type "q" or "Q" in order to make specific QUERY in the table.
    4. Type "d" or "D" in order to DELETE data from the table.
    5. Type "s" or "S" in order to see the values in the table.
    6. Type "f" or "F" in order to close the program.
    7. Type "search" to search by template.
    8. Type "bulk_insert" to insert bulk data.
    9. Type "paginated" to get paginated results.
    10. Type "del_user" to delete user by name or phone.
    """)

    command = input().lower()

    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        query_data()
    elif command == "s":
        display_data()
    elif command == "search":
        search_by_template()
    elif command == "bulk_insert":
        insert_bulk_users()
    elif command == "paginated":
        get_paginated_data()
    elif command == "del_user":
        delete_user()
    elif command == "f":
        break

# Закрытие соединения с базой данных
conn.commit()
cur.close()
conn.close()
