import csv
from datetime import datetime

filename = 'CVS_book\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Чтение максимальных температур из файла.
filename = 'CVS_book\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #highs = []
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        #highs.append(row[1])
        high = int(row[1])
        highs.append(high)
    #print(highs)


# Нанесение данных на диаграмму

from matplotlib import pyplot as plt

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
#plt.plot(highs, c='red')

# Форматирование диаграммы.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# Представление дат на диаграмме
