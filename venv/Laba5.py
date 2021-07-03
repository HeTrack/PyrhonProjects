import random
import pandas as pd
from bitarray import bitarray
#Эталон
NormaKkal = 2225.0;
NormaBelki = 65.0;
NormaFat = 74.0;
NormaUglevod = 324.0;

#Количество продуктов в рационе
k = 0;

Normal = [NormaBelki, NormaFat, NormaUglevod, NormaKkal];
Menu = pd.read_excel('D:\iliya\Desktop\Лаба_5. Нечёткая логика.xlsx').to_numpy();
FitnessFunc = [0] * len(Menu); #фитнес-функция для каждого объекта
Population = [];
PrisposoblMassiv = [];
OtborPopulation = [];
#Инициализация популяции
def InitPopulation():
    for i in range(0,100):
        a = 40 * bitarray('0')
        #Кол-во продуктов в хромосоме
        odin = random.randint(2, 10)
        for j in range(1, odin):
            pos = random.randint(0, 39)
            if(a[pos] == 0):
                a[pos] = 1;
        Population.append(a)
        print(Population[i])
#Вычисление фитнес-функции для каждого объекта
def Fitness():
    for i, food in enumerate(Menu):
        sum = 0.0;
        for j in range(len(Normal)):
            sum = sum + (float(food[j+2])/Normal[i]);
        print(food[1], FitnessFunc[i]);
#Оценка приспособленности
def Prisposobl(population):
    PrisposoblMassiv.clear();
    for individ in population:
        sum = 0;
        for bit in range(len(individ)):
            sum += individ[bit]*FitnessFunc[bit];
        PrisposoblMassiv.append(sum)
        print(PrisposoblMassiv[-1])
#Отбор приспособленных с удельной вероятностью
def Otbor():
    for counter, individ in enumerate(PrisposoblMassiv):
        live_rate = individ/sum(PrisposoblMassiv)*15;
        print(live_rate)
        if(live_rate > 1):
            OtborPopulation.append(Population[counter]);
            print(OtborPopulation[-1]);
#Кроссовер
def Krossover():
    size = len(OtborPopulation);
    print(size)
    i = 0;
    while i <= size:
        tochka = random.randint(1, 38)
        # первый элемент одноточечного кроссовера
        krosover_first = 40 * bitarray('0');
        krosover_first[0:tochka] = OtborPopulation[i][0:tochka];
        krosover_first[tochka:39] = OtborPopulation[i+1][tochka:39];
        print(krosover_first);
        # второй элемент одноточечного кроссовера
        krosover_second = 40 * bitarray('0');
        krosover_second[0:tochka] = OtborPopulation[i+1][0:tochka];
        krosover_second[tochka:39] = OtborPopulation[i][tochka:39];
        print(krosover_second);
        #Добавление в популяцию
        OtborPopulation.pop(i);
        OtborPopulation.pop(i+1);
        size-=2;
        OtborPopulation.append(krosover_first);
        OtborPopulation.append(krosover_second);
#Мутация
def Mutation():
    for individ in OtborPopulation:
        if(random.random() > 0.8):
            for i in range(random.randint(1,3)):
                pos = random.randint(0,39);
                individ[pos] = not individ[pos];
            print(individ);

k = input("Введите количество продуктов в рационе питания");
print();

print("Начальная популяция");
InitPopulation();
print();

print("Фитнес-функцияя для каждого элемента");
Fitness();
print();

print("Приспособленность объектов первой популяции");
Prisposobl(Population)
print();

print("Отбор наиболее приспособленных объектов");
Otbor()
print()
count = 0;
exitFlag = False;
while(count < 7):
    print("Результат кроссовера");
    Krossover();
    print();

    print("Результат мутации");
    Mutation();
    print();

    print("Приспособленность объектов отбора");
    Prisposobl(OtborPopulation);
    for c, individ in enumerate(PrisposoblMassiv):
        if(individ < 1500):
            print("Конец ген. алгоритма")
            print(OtborPopulation[c])
            exitFlag = True
            break

    if (exitFlag):
        break
    print();
    count+=1;
if (not exitFlag):
    print(min(PrisposoblMassiv))
    print(OtborPopulation[PrisposoblMassiv.index(min(PrisposoblMassiv))])