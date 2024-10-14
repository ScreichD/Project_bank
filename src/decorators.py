from functools import wraps


def log(filename=None):
    """Функция декоратор логирует начало и конец работы функцииБ результаты и ошибки"""

    def decorator(my_func):
        @wraps(my_func)
        def wrapper(*args, **kwargs):
            result = None
            if not filename:
                print(f"{my_func.__name__} started")
                try:
                    result = my_func(*args, **kwargs)
                    print(f"{my_func.__name__} ok")
                    print(f"{my_func.__name__} finished")
                except Exception as e:
                    print(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            else:
                try:
                    result = my_func(*args, **kwargs)
                    with open(filename, "w") as file:
                        file.write(f"{my_func.__name__} ok")
                except Exception as e:
                    with open(filename, "w") as file:
                        file.write(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            return result
        return wrapper
    return decorator
@log()
def my_function(x, y):
    return x / y


result = my_function(10, 5)
print(result)
