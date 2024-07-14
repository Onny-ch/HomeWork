from src.decorators import log


def test_log_console_print_with_exception(capsys):
    @log()
    def my_function(x, y):
        return x + y
    my_function("wrong", 3)
    captured = capsys.readouterr()
    expected_result = '''my_function error: can only concatenate str (not "int") to str. Inputs: ('wrong', 3), {}\n'''
    assert captured.out == expected_result


def test_log_file_write_with_exception():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y
    expected_result = '''my_function error: can only concatenate str (not "int") to str. Inputs: ('wrong', 3), {}'''
    assert my_function("wrong", 3) == expected_result


def test_log_console_print_no_exception(capsys):
    @log()
    def my_function(x, y):
        return x + y
    my_function(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok, function work time = 0.0\n"


def test_log_file_write():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y
    assert my_function(2, 3) == 5
