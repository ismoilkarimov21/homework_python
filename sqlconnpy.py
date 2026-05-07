# import sqlite3
#
# conn = sqlite3.connect("sample-database.db")
#
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM employees LIMIT 5")
#
# ans = cur.fetchall()
# for i in ans:
#     print(i)
#
# cur.close()
# conn.close()


import sqlite3
from contextlib import closing


# CRUD
def get_connection(database_path):
    return closing(sqlite3.connect(database_path))

def create_employee(database_path,employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id) VALUES (?, ?,?,?, ?,?,?, ?,?,?)", (employee_id,first_name, last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id))
        connection.commit()
        return cursor.lastrowid


def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
        return cursor.fetchone()


def update_employee(database_path, employee_id, first_name):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        if first_name:
            cursor.execute("UPDATE employees SET first_name=? WHERE employee_id=?", (first_name, employee_id))
        connection.commit()


def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE employee_id=?", (employee_id,))
        connection.commit()

database_path = "sample-database.db"

employee_get = get_employee(database_path,113)
print(employee_get)

employee_create = create_employee(database_path,207,"Ali","Valiyev","ali@gmail.com","+998931234567","08-08-2018", 5,1500,3,10)
print(employee_create)

employee_update = update_employee(database_path, 100, "Jasur")
print(employee_update)

employee_delete = delete_employee(database_path,100 )


import sqlite3
from abc import ABC, abstractmethod
from contextlib import closing

DATABASE_PATH = "sample-database.db"
class BaseCRUD(ABC):
    def __init__(self, database_path, country_name, country_id):
        self.database_path = database_path
        self.country_name = country_name
        self.country_id = country_id


    def get_connection(self):
        return closing(sqlite3.connect(self.database_path))

    def insert(self, **kwargs):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join('?' for _ in kwargs)
            query = f"INSERT INTO {self.country_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, tuple(kwargs.values()))
            connection.commit()
            return cursor.lastrowid

    def get(self, id, id_column="country_id"):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM countries WHERE {id_column}=?"
            cursor.execute(query, (id,))
            return cursor.fetchone()

    def update(self, id, id_column="country_id", **kwargs):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            columns = ', '.join(f"{key}=?" for key in kwargs)
            query = f"UPDATE {self.country_name} SET {columns} WHERE {id_column}=?"
            cursor.execute(query, (*kwargs.values(), id))
            connection.commit()

    def delete(self, id, id_column="id"):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"DELETE FROM {self.country_name} WHERE {id_column}=?"
            cursor.execute(query, (id,))
            connection.commit()

# country1 = BaseCRUD("sample-database.db", "Brazil", "BR")
# print(country1.get("BR"))

country1 = BaseCRUD("sample-database.db", "UZB", "UZ")
print(country1.update(country1.country_id))