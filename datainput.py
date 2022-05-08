from colorama import Fore, Style
import numpy as np
import matplotlib.pyplot as plt
import main

FILE_INPUT = "/Users/nurgunmakarov/PycharmProjects/Lab2/input.txt"


def handle_method(method, data):
    function = data["function"]
    if method == "1" or method == "3" or method == "2":
        print("Выберите границы интервала")
        while True:
            try:
                print("Начало")
                a = float(input(">>>"))
                print("Конец")
                b = float(input(">>>"))
                if b < a:
                    a, b = b, a
                elif a == b:
                    raise ArithmeticError
                elif function(a) * function(b) > 0:
                    raise AttributeError
                break
            except ArithmeticError:
                print(Fore.RED + "Границы интервала должны отличаться!" + Style.RESET_ALL)
            except AttributeError:
                print(Fore.RED + "Нет корней!" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Границы интервала должны быть числом!" + Style.RESET_ALL)
        data["a"] = a
        data["b"] = b
    # elif method == "2":
    #     print("Выберите начальное приближение")
    #     while True:
    #         try:
    #             start = float(input(Fore.MAGENTA + ">>>" + Style.RESET_ALL))
    #             break
    #         except ValueError:
    #             print(Fore.RED + "Начальное приближение должно быть числом!" + Style.RESET_ALL)
    #     data["x0"] = start
    print("Введите погрешность")
    while True:
        try:
            error = float(input(Fore.MAGENTA + "   >>>" + Style.RESET_ALL))
            if error <= 0:
                raise ArithmeticError
            break
        except ArithmeticError:
            print("Погрешность не должна быть меньше или равна нулю!")
        except ValueError:
            print("Погрешность должна быть числом!")
    data["error"] = error
    return data


def get_method():
    print("\nВыберите метод решения:")
    print(Fore.GREEN + "1 - " + Style.RESET_ALL, "Метод хорд")
    print(Fore.GREEN + "2 - " + Style.RESET_ALL, "Метод простой итерации")
    print(Fore.GREEN + "3 - " + Style.RESET_ALL, "Метод Ньютона")
    method = input(Fore.MAGENTA + ">>>" + Style.RESET_ALL)
    while method != "1" and method != "2" and method != "3":
        method = input(Fore.MAGENTA + ">>>" + Style.RESET_ALL)
    return method


def get_func(function_number):
    if function_number == "1":
        return np.linspace(-5, 13, 100), \
               lambda x: 2 * x ** 3 + 3.41 * x ** 2 - 23.74 * x + 2.95
    elif function_number == "2":
        return np.linspace(-5, 13, 100), \
               lambda x: x ** 3 - x + 4
    elif function_number == "3":
        return np.linspace(-5, 13, 100), \
               lambda x: np.sin(x) + 0.2
    elif function_number == "4":
        return np.linspace(-2, 2, 30), \
               lambda x: np.sqrt(4 - x ** 2), \
               lambda x: 3 * x ** 2
    else:
        return "Oops"


def get_data_from_file():
    with open(FILE_INPUT, "rt") as f:
        try:
            data = {}

            function_data = get_func(f.readline().strip())
            if function_data is None:
                raise ValueError
            x, function = function_data
            main.plot(x, function(x))
            data['function'] = function

            method = f.readline().strip()
            if (method != '1') and (method != '2') and (method != '3'):
                raise ValueError
            data["method"] = method

            if method == '1' or method == '3':
                a, b = map(float, f.readline().strip().split())
                if a > b:
                    a, b = b, a
                elif a == b:
                    raise ArithmeticError
                elif function(a) * function(b) > 0:
                    raise AttributeError
                data['a'] = a
                data['b'] = b
            elif method == '2':
                x0 = float(f.readline().strip())
                data['x0'] = x0

            error = float(f.readline().strip())
            if error < 0:
                raise ArithmeticError
            data['error'] = error

            return data
        except (ValueError, ArithmeticError, AttributeError):
            return None


def get_data_from_keyboard():
    data = {}
    print("\nВыберите функцию: ")
    print(Fore.GREEN + "1 - " + Style.RESET_ALL, "2x³ + 3.41x² - 23.74x + 2.95")
    print(Fore.GREEN + "2 - " + Style.RESET_ALL, "x³ - x + 4")
    print(Fore.GREEN + "3 - " + Style.RESET_ALL, "sin(x) + 0.2")
    func_data = get_func(input(Fore.MAGENTA + ">>>" + Style.RESET_ALL))
    while func_data == "Oops":
        print("Упс, кажется вы не туда нажали, попробуйте снова")
        func_data = get_func(input(Fore.MAGENTA + "   >>> " + Style.RESET_ALL))
    x, function = func_data
    main.plot(x, function(x))
    plt.plot(x, function(x))
    data["function"] = function
    method = get_method()
    data["method"] = method
    data = handle_method(method, data)
    return data


def get_data_from_keyboard_system():
    data = {}
    print("\nВыберите систему уравнений:")
    print(Fore.GREEN + "--------|1|-------- " + Style.RESET_ALL, "\nx^2 + y^2 - 4")
    print("-y + 3x^2")
    data["f1"] = 'x**2 + y**2 - 4'
    data["f2"] = "-3*x**2 + y"
    func_data = get_func("4")
    x, function1, function2 = func_data
    plt.plot(x, function1(x))
    plt.plot(x, function2(x))
    plt.show()
    data["function1"] = function1
    data["function2"] = function2
    data["system"] = "1"
    data["method"] = "3"
    error = None
    while True:
        try:
            print("Введите погрешность")
            error = float(input(Fore.GREEN + ">>>" + Style.RESET_ALL))
            break
        except ValueError:
            print("Упс, что-то пошло не так")
            pass
    data["error"] = error
    return data
