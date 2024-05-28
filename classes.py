from db.manage import Database


class Country:
    table_name = "country"
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = f"SELECT * FROM {Country.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO country( name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE country SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE country SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM country WHERE {column} = {data}"
        else:
            query = f"DELETE FROM country WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class City(Country):
    table_name = "city"

    def __init__(self, name, city_id):
        Country.__init__(self, name)
        self.city_id = city_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {City.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO city(name, country_id) VALUES('{self.name}', {self.city_id})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        names = "city"
        if column == "id":
            query = f"UPDATE {names} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {names} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        name = "city"
        if column == "id":
            query = f"DELETE FROM {name} WHERE {column} = {data}"
        else:
            query = f"DELETE FROM {name} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Address(City):
    table_name = "address"

    def __init__(self, name, city_id):
        City.__init__(self, name, city_id)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Address.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO {Address.table_name}(name, city_id ) VALUES('{self.name}', {self.city_id})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        names = "address"
        if column == "id":
            query = f"UPDATE {names} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {names} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        name = "address"
        if column == "id":
            query = f"DELETE FROM {name} WHERE {column} = {data}"
        else:
            query = f"DELETE FROM {name} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Customers(Country):
    table_name = "customers"
    def __init__(self, first_name, last_name, username, password, birth_date, address_id):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.birth_date = birth_date
        self.address_id = address_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {Customers.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)


    def insert(self):
        query = f"""
            INSERT INTO customers(first_name, last_name, username, password, birth_date, address_id ) 
            VALUES('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}', '{self.birth_date}', '{self.address_id}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE {Customers.table_name} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {Customers.table_name} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM {Customers.table_name} WHERE {column} = {data}"
        else:
            query = f"DELETE FROM {Customers.table_name} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class PaymentStatus(Customers):
    table_name = "payment_status"
    def __init__(self, name):
        Country.__init__(self, name)


    @staticmethod
    def select():
        query = f"SELECT * FROM {PaymentStatus.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)


    def insert(self):
        query = f"""
            INSERT INTO {PaymentStatus.table_name}(name) 
            VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE {PaymentStatus.table_name} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {PaymentStatus.table_name} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM {PaymentStatus.table_name} WHERE {column} = name"
        else:
            query = f"DELETE FROM {PaymentStatus.table_name} WHERE {column} = id "
        return Database.connect(query, "delete")


class Category(Country):
    table_name = "category"
    def __init__(self, name):
        Country.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Category.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO category( name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE category SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE category SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM category WHERE {column} = {data}"
        else:
            query = f"DELETE FROM category WHERE {column} = '{data}'"
        return Database.connect(query, "delete")




class Store(Category):
    def __init__(self, name):
        Category.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Store.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO store( name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE store SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE store SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM store WHERE {column} = {data}"
        else:
            query = f"DELETE FROM store WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Product(Category):
    table_name = "product"
    def __init__(self, name, description, price, count, serial_number, start_date, end_date, store_id, category_id):
        self.description = description
        self.price = price
        self.count = count
        self.serial_number = serial_number
        self.start_date = start_date
        self.end_date = end_date
        self.store_id = store_id
        self.category_id = category_id
        Category.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Product.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO {Product.table_name}( name, description, price, count, serial_number, start_date, end_date, store_id, category_id)
             VALUES('{self.name}', '{self.description}', '{self.price}', '{self.count}', '{self.serial_number}', '{self.start_date}', '{self.end_date}', '{self.store_id}', '{self.category_id}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE {Product.table_name} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {Product.table_name} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM {Product.table_name} WHERE {column} = {data}"
        else:
            query = f"DELETE FROM {Product.table_name} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")



class Order(Country):
    table_name = "orders"
    def __init__(self, name):
        Country.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Order.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO {Order.table_name}( name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE {Order.table_name} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {Order.table_name} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM {Order.table_name} WHERE {column} = {data}"
        else:
            query = f"DELETE FROM {Order.table_name} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")

class Staff(Country):
    table_name = "staff"
    def __init__(self, name):
        Country.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Staff.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
             INSERT INTO {Staff.table_name}( name) VALUES('{self.name}')
         """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE {Staff.table_name} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {Staff.table_name} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM {Staff.table_name} WHERE {column} = {data}"
        else:
            query = f"DELETE FROM {Staff.table_name} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")