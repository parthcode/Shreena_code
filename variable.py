def user_input():
    operation = int(input("Enter 1 to create new account or 2 to login "))
    return operation


def new_account():
    name = input("Enter the name")
    user_name, password = log_in()
    return name, user_name, password


def log_in():
    user_name = input("Enter the user name")
    password = input("Enter the password")
    return user_name, password


def file_operation(location, operation, content):
    meta_data = open(location, operation)
    if operation == 'a':
        meta_data.write(content)
        print("Write is successful")
    elif operation == 'r':
        data = meta_data.read()
        return data
