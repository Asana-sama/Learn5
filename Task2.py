# Создать текстовый файл (не программно), сохранить в него несколько строк,
# выполнить подсчет колличества строк, количества слова в каждой строке.
import re

def count(name="task2.txt"):
    file = open(name,"r")
    line_counter = 0
    word_counter = []
    for line in file:
        line_counter += 1
        word_counter.append(len(re.split("[\s,:!;]+", line)))
    file.close()
    return line_counter,word_counter 

def main():
    filename = input("Введите имя файла:")
    if filename != "":
        result = count(filename)
    else:
        result = count()
    print("Количество строк = ",result[0])
    print("Количество слов в строках = ",result[1])
    pass

if __name__ == "__main__":
    main()