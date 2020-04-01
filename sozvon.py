import csv  #импортируется модуль csv
buffer = []

with open('data.csv') as file:
    reader = csv.reader(file)  #csv-файл передаётся функции csv.reader, которая возвращает объект-считыватель,
                               #позволяющий выполнять итерацию над каждым рядом в объекте-считывателе и отобразить строку данных без запятых
    for row in reader:
        buffer.append(row)  #строка переносится в конец

call_duration = 0  #буфер, где хранятся суммы минут звонков
sms_number = -10  #буфер, где хранится количество смс. "-10", так как первые 10 шт. - бесплатно

for i in range(1, 10):  #рассматриваем данные звонков и смс
    if '933156729' in buffer[i][1]:  #проверяется наличие номера
        call_duration += float(buffer[i][3])  #складываем минуты
        sms_number += float(buffer[i][4])  #складываем количество смс

print(call_duration*2, sms_number*1)  #выводится итоговая стоимость звонков и смс с учётом тарифа
