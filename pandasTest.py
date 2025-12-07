import pandas as pd

tabl = pd.read_excel("rasp.xlsx")

print(tabl[tabl["День"] == "ВТ"])
