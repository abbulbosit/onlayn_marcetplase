from classes import Country, City, Address, Customers, PaymentStatus, Category, Store, Staff, Product, Order

def country_tables():
    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        Country.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return country_tables()

    elif services == "2":
        name = input("Name: ")
        country = Country(name)
        print(country.insert())
        return country_tables()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(Country.update(column, new_data, old_data))

        return country_tables()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(Country.delete(column, data))
        return country_tables()


def city_tables():

    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        City.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return city_tables()

    elif services == "2":
        name = input("Name: ")
        city_id = int(input("Country ID: "))
        city = City(name, city_id)
        print(city.insert())
        return city_tables()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(City.update(column, new_data, old_data))

        return city_tables()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(City.delete(column, data))
        return city_tables()


def address_tables():

    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        Address.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return address_tables()

    elif services == "2":
        name = input("Name: ")
        city_id = int(input("City ID: "))
        city = Address(name, city_id)
        print(city.insert())

        return city_tables()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(Address.update(column, new_data, old_data))

        return address_tables()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(Address.delete(column, data))
        return address_tables()

def customers_tables():


    customers = Customers


    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        customers.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return customers_tables()

    elif services == "2":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        username = input("Username: ")
        password = int(input("Password: "))
        birth_ate = int(input("enter birth date:"))
        address_id = int(input("Address ID: "))
        city = Customers(first_name, last_name, username, password,birth_ate, address_id)
        print(city.insert())
        return customers_tables()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(customers.update(column, new_data, old_data))

        return customers_tables()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(customers.delete(column, data))
        return customers_tables()


def payment_s():


    payment = PaymentStatus


    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        payment.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return payment_s()

    elif services == "2":
        first_name = input(" Name: ")
        city = payment(first_name)
        print(city.insert())
        return payment_s()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(payment.update(column, new_data, old_data))

        return payment_s()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(payment_s().delete(column, data))
        return payment_s()


def category_():


    category = Category


    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        category.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return customers_tables()

    elif services == "2":
        first_name = input("First Name: ")
        city = category(first_name)
        print(city.insert())
        return category_()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(category.update(column, new_data, old_data))

        return category_()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(category.delete(column, data))
        return category_()


def store():

    stores = Store


    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        stores.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return store()

    elif services == "2":
        first_name = input("First Name: ")
        city = stores(first_name)
        print(city.insert())
        return category_()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(stores.update(column, new_data, old_data))

        return category_()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(stores.delete(column, data))
        return category_()

def product():

    products = Product


    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        products.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return product()

    elif services == "2":
        first_name = input("Name: ")
        description = input("Description: ")
        price = input("Price: ")
        count = input("Count: ")
        serial_number = input("Serial Number: ")
        start_date = input("Start Date: ")
        end_date = input("End Date: ")
        store_id = input("Store ID: ")
        category_id = input("Category ID: ")
        city = products(first_name, description, price, count, serial_number,
                        start_date, end_date, store_id, category_id)
        print(city.insert())
        return product()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(products.update(column, new_data, old_data))

        return product()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(products.delete(column, data))
        return product()


def orders():

    order = Order


    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        order.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return orders()

    elif services == "2":
        first_name = input("First Name: ")
        city = order(first_name)
        print(city.insert())
        return product()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(order.update(column, new_data, old_data))

        return product()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(order.delete(column, data))
        return product()

def staff():

    staffs = Staff

    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        staffs.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return staff()

    elif services == "2":
        first_name = input("First Name: ")
        city = staffs(first_name)
        print(city.insert())
        return product()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(staffs.update(column, new_data, old_data))

        return product()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(staffs.delete(column, data))
        return product()


def main():
    table = input("""
        1. Country
        2. City
        3. Address
        4. Customers
        5. PaymentStatus
        6. Category
        7. Store
        8. Product
        9. Orders
        10. Staff
            >>> """)

    if table == '1':
        return country_tables()

    elif table == '2':
        return city_tables()

    elif table == '3':
        return address_tables()

    elif table == '4':
        return customers_tables()

    elif table == '5':
        return payment_s()

    elif table == '6':
        return category_()

    elif table == '7':
        return store()

    elif table == '8':
        return product()

    elif table == '9':
        return orders()

    elif table == '10':
        return staff()

    else:
        print("error")
        return main()

if __name__ == "__main__":
    main()