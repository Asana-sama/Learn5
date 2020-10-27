# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

def file_input(name="task1.txt"):
    file = open(name, "w")
    input_string = input("Введите строку:")
    while (input_string != ""):
        file.write(input_string + "\n")
        input_string = input("Введите следующую строку:")
    file.close()
    pass 

def main():
    filename = input("Введите имя файла:")
    if filename != "":
        file_input(filename)
    else:
        file_input()
    pass

if __name__ == "__main__":
    main()