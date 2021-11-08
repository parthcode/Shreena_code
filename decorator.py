import time

def calcutale_time(some_function):
    t1 = time.time()
    some_function()
    t2 = time.time()
    print("time taken to execute is :", t2 - t1)


def function_one():
    for i in range(5):
        time.sleep(0.2)

@calcutale_time
def function_two():
    for i in range(3):
        time.sleep(0.5)


