import random

list = []
for i in range(15):
    list.append(random.randint(-15, 15))

print(len(list))
print(list)
# Create a list with the mood to write in excel

import pandas as pd
import xlrd
import matplotlib.pyplot as plt

# open Excel file
sh = pd.ExcelFile('templates/shedule.xlsx')
print(sh.sheet_names)
new_sh = sh.parse('shedule')
print(new_sh.columns)
print(new_sh['Days'])
print(new_sh['Mood'])
