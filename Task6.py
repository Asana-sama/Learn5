# Создать вручную и заполнить несколькими строками текстовый файл, в ктором каждая строка 
# должна содержать данные о фирме: название, форма собственности, выручка, издержки
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а так же среднюю
# прибыль. Если фрима получила обытки, в расчет средней прибыли не включать.
# Далее реализовать список. Он должен содержать словари с фирмами и их прибылями, а также
# словарь со средней прибылью. Если фирма получила убытки также добавить ее в словарь
# Итоговый список сохранить в виде json-объекта в соответствующий файл

import json
from contextlib import contextmanager

def firm_count(name="task6.txt"):
    result,average,counter,firm = [],0,0,{}
    file = open(name,"r",encoding="utf8")
    for line in file:
        counter += 1
        profit = float(line.split(" ")[2]) - float(line.split(" ")[3])
        if profit > 0:
            average += profit
        firm[line.split(" ")[0]] = profit
    file.close()
    result.append(firm)
    result.append({"average_profit":round(average/counter,2)})
    return result

def json_file(data,name="task6.json"):
    with open("task6.json","w",encoding="utf8") as file:
        json.dump(data,file,ensure_ascii=False)
    pass

def main():
    raw_json = firm_count("task6.txt")
    print ("Список: ",raw_json)
    json_file(raw_json,"task6.json")
    pass

if __name__ == "__main__":
    main()