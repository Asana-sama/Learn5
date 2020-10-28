# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

def file_generate(N):
    with open("task4.txt","w") as file:
        for i in range(N):
            file.write(str(round(random.uniform(1, 100),2))+" ")
    pass

def file_summary():
    summ = 0.0
    file = open("task4.txt","r")
    line = file.readline()
    for v in line.strip().split(" "):
        summ += float(v)
    return round(summ,2)

def main():
    N = random.randint(20, 30) # Количество чисел для записи в файл
    file_generate(N)
    print(file_summary())
    pass

if __name__ == "__main__":
    main()