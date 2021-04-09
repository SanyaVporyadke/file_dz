# 1 задание. Переведите содержимое файла purchase_log.txt в словарь purchases вида:{‘1840e0b9d4’: ‘Продукты’, …}

import json

di = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        current = json.loads(line)
        for k, v in current.items():
            key = current['user_id']
            value = current['category']
            if key != 'user_id':
                di[key] = value


# Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки
# (если покупка была, сам файл visit_log.csv изменять не надо).
#  Запишите в файл funnel.csv визиты из файла visit_log.csv, в которых были покупки с указанием категории.


with open('visit_log.csv', 'r', encoding='utf-8') as f1:
    with open('funnel.csv', 'w') as f2:
        for line in f1:
            line = line.strip().split(',')
            if line[0] in di.keys():
                line.append(di[line[0]])
                f2.write(json.dumps(line))
                




                