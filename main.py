from variable import user_input, new_account, log_in, file_operation
""""
Try to write content of data variable into a file by callig "file_operation"
"""

name, user_name, password = '', '', ''

if user_input() == 1:
    name, user_name, password = new_account()
elif user_input() == 2:
    user_name, password = log_in()
else:
    print("Please enter 1 or 2")

data = {
    name: {
        "user_name": user_name,
        "password": password
    }
}
