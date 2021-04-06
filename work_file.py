# 1 задание. Переведите содержимое файла purchase_log.txt в словарь purchases вида:{‘1840e0b9d4’: ‘Продукты’, …}

import json

di = {}
with open('purchase_log.txt', encoding='utf-8') as file:
    for i, line in enumerate(file):
        line = line.strip()
        di = json.loads(line)


# Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки
# (если покупка была, сам файл visit_log.csv изменять не надо).
#  Запишите в файл funnel.csv визиты из файла visit_log.csv, в которых были покупки с указанием категории.

with open('visit_log.csv', 'r', encoding='utf-8') as f1:
    with open('funnel.csv', 'w') as f2:
        for line in f1:
            if 'context' in line:
                f2.write(line)