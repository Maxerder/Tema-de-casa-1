#tema 1 de casa pandas si matplotlib
#X = numarul de litere din numele studentului Ciobanu - 7
#Y = numarul de litere din (toate) prenumel studentului Andrei - 6
#.\pandas_vnv\Scripts\activate
#powershell Set-ExecutionPolicy Unrestricted - A
#pip instal pandas pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Citirea datelor din fisierul CSV
data = pd.read_csv('data.csv') #citeste fisierul 

#definirea variabilelor X si Y
X = 7  
Y = 6 

# Afișarea tuturor valorilor
plt.figure(figsize=(10, 6))# dimensiune imagine grafice
plt.plot(data.index, data['Durata'], label='Durata', marker='|', color = 'b')    #plot() functie pentru desenarea parkerelor pe diagrama
plt.plot(data.index, data['Puls'], label='Puls', marker='|', color = 'r')
plt.title('Grafic pentru durata si puls(tot)')# titlu - grafic
plt.xlabel('Puls')#denumire axa x
plt.ylabel('Durata')#denumire axa y
plt.legend()#label - afiseaza informatia despre fiecare linie
plt.show()#afisare grafice



#afisarea primelor X valori
plt.figure(figsize=(10, 5))
plt.plot(data.index[:X], data['Durata'][:X], label='Durata', marker='|',ms= 20, color = 'b')
plt.plot(data.index[:X], data['Puls'][:X], label='Puls', marker='|',ms = 20, color = 'r')
plt.title(f'Primele {X} valori pentru Durata si Puls')
plt.xlabel('Puls')
plt.ylabel('Durata')
plt.legend()
plt.show()

#afisarea ultimelor Y valori 
plt.figure(figsize=(10, 5))
plt.plot(data.index[-Y:], data['Durata'].tail(Y), label='Durata', marker='|',ms=20, color = 'b')
plt.plot(data.index[-Y:], data['Puls'].tail(Y), label='Puls', marker='|',ms=20, color = 'r')
plt.title(f'Ultimele {Y} valori pentru Durata si Puls')
plt.xlabel('Puls')
plt.ylabel('Durata')
plt.legend()
plt.show()
