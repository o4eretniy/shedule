# Create a list with the mood to write in excel
import random

list = []
for i in range(15):
    list.append(random.randint(-15, 15))

print(len(list))
print(list)
################################################

import pandas as pd
import xlrd
import matplotlib.pyplot as plt

# open Excel file
sh = pd.ExcelFile('templates/shedule.xlsx')
new_sh = sh.parse('shedule')

# assigned columns values to axes
days = new_sh['Days']
mood = new_sh['Mood']
plt.plot(days , mood, linewidth=3)

# gave the names of the axes and title
plt.title('Shedule', fontsize=24)
plt.xlabel(str(new_sh.columns[1]), fontsize=14)
plt.ylabel(str(new_sh.columns[0]), fontsize=14)

# show graph
plt.show()