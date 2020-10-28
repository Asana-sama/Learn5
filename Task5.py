# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать
# словарь, содержащий название предмета и общее количество занятий по нему.
import re

def hours_count(name="task5.txt"):
    result = {}
    file = open(name,"r",encoding='utf8')
    for line in file:
        summ = 0
        name = line.split(':')[0]
        hours = re.findall(r'\d+',line.split(':')[1])
        for hour in hours:
            summ += int(hour)
        result[name] = summ
    file.close()
    return result

def main():
    result = hours_count("task5.txt")
    for k in result:
        print(k,result[k])
    pass

if __name__ == "__main__":
    main()