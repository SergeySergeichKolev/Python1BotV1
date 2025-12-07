# #Линейная модель
from sklearn.linear_model import LinearRegression

#создаем модель нейросети
model1 = LinearRegression()

rost = [[5], [4]]
ves = [100, 90]

#обучаем модель
model1.fit(rost, ves)

#предположить, узнать
x = model1.predict([[3]])

print(x)



#[{}, {}, {}, {}]
data = []

# размер 1-5 - яблоко
# размер 6-10 - апельсин
# тощина 0.1 - 1 - яблоко
# толщина 1.1 - 2 апельсин

row = {"size": 2, "tolsh": 0.2, "name": "yabl"}
data.append(row)

row = {"size": 1, "tolsh": 0.1, "name": "yabl"}
data.append(row)

row = {"size": 4, "tolsh": 0.4, "name": "yabl"}
data.append(row)

row = {"size": 0.1, "tolsh": 2, "name": "apels"}
data.append(row)

row = {"size": 2, "tolsh": 1.3, "name": "apels"}
data.append(row)

row = {"size": 2, "tolsh": 1.5, "name": "apels"}
data.append(row)


def fruits(size, tolsh):
    if size < 5 or tolsh <1:
        print("apple")
    else:
        print("orange")

fruits(6, 2)

[{}, {}, {}, {}]

for i in data:
    print(f"Размер - {i["size"]} ,  Толщина - {i["tolsh"]}, Это - {i["name"]} ")