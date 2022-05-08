from colorama import Fore, Style
from matplotlib import pyplot as plt

import datainput
import solver
import system_solver


def plot(x, y):
    """ Отрисовать график по заданным x и y """
    # Настраиваем всплывающее окно
    # plt.rcParams['toolbar'] = 'None'
    plt.gcf().canvas.set_window_title("График функции")
    # Настриваем оси
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k',
            transform=ax.get_xaxis_transform(), clip_on=False)

    # Отрисовываем график
    plt.plot(x, y)
    plt.show(block=False)


if __name__ == '__main__':
    data = {"dots": []}
    print(Fore.BLUE + "Вторая лабораторная работа" + Style.RESET_ALL)
    print(Fore.BLUE + "Вариант №6" + Style.RESET_ALL)
    print("\nОсуществить ввод с файла(f), с клавиатуры(c)")
    choise = None
    second_choise = None
    while choise != 'f' and choise != 'c':
        choise = input(Fore.MAGENTA + ">>>" + Style.RESET_ALL)
        if choise == 'f':
            data = datainput.get_data_from_file()
        elif choise == 'c':
            while second_choise != '1' and second_choise != '2':
                second_choise = input("\nРешить систему нелинейных уравнений(2), решить уравнение (1)")
                if second_choise == '1':
                    data = datainput.get_data_from_keyboard()
                elif second_choise == '2':
                    data = datainput.get_data_from_keyboard_system()
    try:
        answer = None
        if data["method"] == "1":
            answer = solver.chord_method(data["a"], data["b"], data["function"], data["error"])
        elif data["method"] == "2":
            answer = solver.simple_iteration_method(data["a"], data["b"], data["function"], data["error"])
            if answer is None:
                print(Fore.RED + "Не выполняется условие сходимости!" + Style.RESET_ALL)
                raise ValueError
        elif data["method"] == "3":
            if data["system"] == "1":
                answer = system_solver.system_newtons_method(data["function1"], data["function2"], data["error"],
                                                             data["f1"], data["f2"])
            else:
                answer = solver.newtons_method(data["a"], data["b"], data["function"], data["error"])
        if answer is None:
            print(Fore.RED + "Не выполняется условие сходимости!" + Style.RESET_ALL)
            raise ValueError
        print(f"Корень уравнения: {answer[0]}")
        print(f"Значение функции: {answer[1]}")
        print(f"Число итераций: {answer[2]}")

        print("Вывести таблицу трассировки? (да/нет)")
        trace_choise = input("   >>>")
        while trace_choise != "да" and trace_choise != "нет":
            trace_choise = input("   >>>")
        if trace_choise == "да":
            for i in range(len(answer[3][0])):
                print("%10s" % answer[3][0][i], end=" ")
            print()
            for i in range(1, len(answer[3])):
                for j in range(len(answer[3][i])):
                    print("%10.10s" % answer[3][i][j], end=" ")
                print()
    except ValueError:
        print(Fore.RED + "Попробуйте снова!" + Style.RESET_ALL)
