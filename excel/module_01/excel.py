# Looge kindlasti virutal env
# pc:
# python -m venv C:\temp\minu_venv
# mac:
# python3 -m venv \Users\sinunimi\mingikaust

# acktiveerige venv
# C:\temp\minu_venv\Scripts\activate
# mac:
# source /Users/sinunimi/mingikaust/bin/activate

# Lisage vajalikud 2 moodulit:
# pip install pandas openpyxl





import csv
from datetime import datetime, timedelta
import calendar

nimi = "minufail.txt"
"""
fh = open(nimi,"r")
read = fh.readlines()
for rida in read:
    puhas_rida = rida.strip()
    
    print(puhas_rida,end="")
fh.close()
"""
"""
with open("numbrid.csv", "r") as fh:
    read = fh.readlines() 
    for rida in read:
        summa = 0
        print("uus rida:")
        puhas_rida = rida.strip()
        osad = puhas_rida.split(",")
        for number_text in osad:
            summa = summa +int(number_text)
        print("Rea summa = {}".format(summa))
            
            
        #print(puhas_rida)
"""


"""
fh = open("andmed.txt", "w")
while True:
    sisend = input("Sisesta arv, l6petamiseks 'q' v6i 'quit'>")
    if sisend in ['q','quit','exit']:
        break
    fh.write(sisend+"\n")
    
fh.close()
"""

import pandas as pd
import numpy as np
import IPython



file_path = 'numbrid.xlsx'


df = pd.read_excel(file_path)

# et pd n2itaks k6iki ridu ja columne
pd.set_option('display.max_row', None)
pd.set_option('display.max_columns', None)

#df['Sum'] = df.apply(lambda row: sum(cell for cell in row if isinstance(cell, (int, float, np.number))), axis=1)

#df.to_excel("numbrid_pythoniga_summeermine.xlsx", index=False, header=False)




# Get the current date
now = datetime.now()

# Calculate the first day of the current month
first_day_current_month = datetime(now.year, now.month, 1)

# Calculate the last day of the previous month
last_day_previous_month = first_day_current_month - timedelta(days=1)

# Calculate the first day of the previous month
first_day_previous_month = datetime(last_day_previous_month.year, last_day_previous_month.month, 1)

# Format the dates
start_date = first_day_previous_month.strftime('%Y-%m-%d')
end_date = last_day_previous_month.strftime('%Y-%m-%d')


df_ajavahemikuga = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
df_ajavahemikuga.to_excel("eelmise_kuu_koond.xlsx", index=False, header=True)


#IPython.embed(colors='neutral')






