# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих 
# сотрудников. Вывести подсчет средней величины дохода сотрудника.

def employee(name="task3.txt"):
    file = open(name,"r",encoding='utf8')
    sallary_count = 0.0
    employee_count = 0
    for line in file:
        employee_count += 1
        if float(line.split(" ")[1]) < 20000.0:
            print (line.split(" ")[0])
        sallary_count += float(line.split(" ")[1])
    file.close()
    return sallary_count/employee_count

def main():
    filename = input("Введите имя файла:")
    if filename != "":
        result = employee(filename)
    else:
        result = employee()
    print("Средняя зарплата = ",result)
    pass

if __name__ == "__main__":
    main()