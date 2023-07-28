def show_menu():
    print("Консольное меню")


def option1():
    print("Вы выбрали Вариант 1.")


def option2():
    print("Вы выбрали Вариант 2.")


def option3():
    print("Вы выбрали Вариант 3.")


# Основной код
while True:
    show_menu()
    choice = input("Введите номер выбранной опции: ")

    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите опцию снова.")
