import numpy as np
##########1#########
#######EXAMEN#######
##########2#########
print("##########2#########")
ceros = np.zeros(10)
print(ceros)
print(len(ceros))
##########3#########
print("##########3#########")
ceros_2 = np.zeros(10)
ceros_2[4] = 1
print(ceros_2)
print(len(ceros_2))
##########4#########
print("##########4#########")
rango = np.arange(0,50)
print(rango)
print(len(rango))
reversa = rango[::-1]
print(reversa)
print(len(reversa))
##########5#########
print("##########5#########")
valores = np.arange(0,9)
print(valores)
print(len(valores))
re = valores.reshape(3,3)
print(re)
print(len(re))
##########6#########
print("##########6#########")
arreglo = np.array([1,2,0,0,4,0])
indices = np.where(arreglo!=0)
print(indices)
##########7#########
print("##########7#########")
identi = np.eye(3)
print(identi)
##########8#########
print("##########8#########")
arr_random = np.random.randint(0,100,27)
mat = arr_random.reshape(3,3,3)
print(mat)
##########9#########
print("##########9#########")
arr_2 = np.random.randint(0,500,100)
mat_2 = arr_2.reshape(10,10)
print(mat_2)
maxi = mat_2.max()
mini = mat_2.min()
print("Máximo:"+str(maxi))
print("Mínimo:"+str(mini))
##########10#########
print("##########10#########")
from PIL import Image
from scipy import misc
mapache = misc.face()
#image = Image.open("./white.jpg") # Para otra imagen
#originalArray = np.asarray(image) # Para otra imagen
originalArray = mapache
#Obtengo tamaño del array
print(originalArray.shape)
#Veo []'s RGB dentro del array
print(originalArray)
#Coloco en una fila todos los []'s de RGB 
allrows = originalArray.flatten().reshape(-1,3)
print(len(allrows)) # => Ancho * Alto
#Obtengo todos los []'s únicos dentro de la lista previa
unique = np.unique(allrows,axis=0)
print("Colores únicos (RGB's):")
print(unique)
print("Número de colores únicos:"+str(len(unique)))
##########11#########
print("##########11#########")
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
print(mydict)
serie_list = pd.Series(mylist)
serie_array = pd.Series(myarr)
serie_dict = pd.Series(mydict)
print(serie_list)
print(serie_array)
print(serie_dict)
##########12#########
print("##########12#########")
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
#Los indices de la serie son una columna más del dataframe
datafr = pd.DataFrame(ser.index,columns=["indice"])
#Los indices de la serie son indices en el dataframe también
datafr2 = pd.DataFrame(ser,columns=["valor"])
##########13#########
print("##########13#########")
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
#Dataframe con series combinadas
ser_concat = pd.concat([ser1,ser2])
datafr_1 = pd.DataFrame(ser,columns=['Combinadas'])
#Dataframe con ambas series en diferentes columnas
datafr_2 = pd.DataFrame(ser1,columns=['serie1'])
datafr_2['serie2'] = ser2
##########14#########
print("##########14#########")
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
tienen = pd.Series(np.intersect1d(ser1,ser2))
ti = []
for x in ser1:
    if not x in tienen.unique():
        ti.append(x)
print (ti)
##########15#########
print("##########15#########")
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
tienen = pd.Series(np.intersect1d(ser1,ser2))
ser3  = pd.concat([
    ser1,
    ser2],
    verify_integrity = False)
no_comun = []
for x in ser3.unique(): 
    if not x in tienen.unique():
        no_comun.append(x)
print(no_comun)
##########16#########
print("##########16#########")
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
valor = 'f'
count = 0
for x in ser:
    if x==valor:
        count += 1
print("Respuesta:"+str(count))
##########17#########
print("##########17#########")
np.random.RandomState(100)
sert = pd.Series(np.random.randint(1, 5, [12]))
#moda = sert.mode()
#print(len(moda))
print(sert)
te = sert.value_counts()[:2].index #[0,2[ Más repetidos
counter = 0
for z in sert:
    if (z!=te[0]) and (z!=te[1]):
        sert[counter]=0
    counter+=1
print(sert)
##########18#########
print("##########18#########")
#shape(7,5)
ser18 = np.random.randint(1, 10, 35).reshape(7,5)
df1 = pd.DataFrame(ser18)
##########19#########
print("##########19#########")
ser19 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
tod = ser19[pos]
print(tod)
##########20#########
print("##########20#########")
ser20 = pd.Series(range(5))
ser200 = pd.Series(list('abcde'))
df2 = pd.DataFrame(ser20)
#Vertical
df2[1] = ser200
#Horizontal
df2 = df2.append(ser20,ignore_index=True)
##########21#########
print("##########21#########")
frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
pesos.groupby(frutas).mean()
##########22#########
print("##########22#########")
path = "/home/nebelschwaden/Documents/2020A/PythonGR1/BostonHousing.csv"
columnas = ['crim','indus','nox','tax','ptratio','medv']
dfa = pd.read_csv(
    path,
    nrows = 10,
    usecols = columnas)
