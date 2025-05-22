import time
from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable[[Any], Any]:
    """
    Декоратор логирования, записывающий информацию о функции и её выполнении в файл, при указании его названия, либо
    выводящий информацию в консоль, при его отсутствии
    """

    def wrapper(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                func_start_time = time.time()
                result = func(*args, **kwargs)
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "w", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                return f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
            else:
                func_end_time = time.time()
                if filename is None:
                    print(f"{func.__name__} ok, function work time = {func_end_time - func_start_time}")
                else:
                    with open(filename, "w", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok, function work time = {func_end_time - func_start_time}")
            return result

        return inner

    return wrapper
