# -*- coding: utf-8 -*-

import string
import re
import unicodedata
import textwrap
import pandas as pd

aa = "to jest to. A to jest to .Lub to"
print(list(aa))

x = "To jest przykladowy tekst. Tak jest!"
print(x[3:7])                              # wyswietla czesc napisu
print(x[3:7] + " " + "duzy")               # konkatenacja
print(x[3:8]*5)                            # powielanie

if "To" in x:                              # sprawdzenie czy napis cos zawiera
    print("Napis: To jest w x","\n")
else:
    print("Napis: To nie wystepuje w x","\n")
    
for l in x:                                # iterowanie 
    print(l, end =" ")
print("\n")
print(list(x),"\n")                             # zmiana na liste

print(string.ascii_letters,"\n")                # litery alfabetu lacinskiego
print(string.ascii_lowercase,"\n")              # male litery
print(string.ascii_uppercase,"\n")              # wielkie litery
print(string.digits,"\n")                       # cyfry
print(string.punctuation,"\n")                  # znaki interpunkcyjne

print(pd.Series(list(string.ascii_uppercase)),"\n")

print("Liczba calkowita reprezentujaca w Unicode litere k to:",ord("k"),"\n")
print("Cyfra 108 w Unicode reprezentuje litere:",chr(108),"\n")

print([unicodedata.name(n) for n in "Sb#^9"],"\n")
print([unicodedata.category(n) for n in "Sb#^9"],"\n")
       
# Kategorie
# L - wszystkie litery Lu - wielkie oraz Ll - male
# N - cyfry
# Z - separatory
# P - znaki interpunkcyjne
# S - symbole

if x.startswith("To"):
    print("Napis x zaczyna się od: To","\n")
else:
    print("Napis x nie zaczyna się od: To","\n")

if x.endswith("jest"):
    print("Napis x konczy sie na: jest","\n")
else:
    print("Napis x nie konczy sie na: jest","\n")
    
print(x.count("jest"),"\n")                      # zlicza ilosc wystapienia danego wzorca

print(x.find("jest"),"\n")                       # zwraca indeks od ktorego rozpoczyna sie pierwsze wystapienie danego podnapisu
print(x.rfind("jest"),"\n")                      # zwraca indeks od ktorego zaczyna sie ostatnie wystapienie danego podnapisu

print(x.replace("To","Oto"),"\n")                # zastapienie napisu innym

print("   biale  znaki".lstrip())                # usuniecie bialych znakow z poczatku npisu
print("   biale  znaki".rstrip())                # usuniecie bialych znakow z konca npisu
print("   biale  znaki".strip())                 # usuniecie bialych znakow z poczatku i konca npisu
print("\n")
print("to jest NOWE zdanie.".capitalize(),"\n")
print("to jest NOWE zdanie.".title(),"\n")
print("to jest NOWE zdanie.".upper(),"\n")
print("to jest NOWE zdanie.".lower(),"\n")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("to jest NOWE zdanie.".translate(str.maketrans(".","!")),"\n")

y = "Matematycznym modelem czasoprzestrzeni jest przestrzen pseudoriemanowska. Powinna byc ona niezwarta, parazwarta,spojna i spelniac drugi aksjomat przeliczalnosci."
yw = textwrap.wrap(y,60)                         # dzielenie napisu
print(yw,"\n")

ys = y.split(".")                                # dzielenie napisu
print(ys,"\n")

print("\n".join(yw),"\n")                        # laczenie napisu

print(textwrap.shorten(y,60,placeholder =" [Czytaj wiecej ...]"),"\n")

# Wyszukiwanie za pomoca wyrazen regularnych

w = re.finditer(r"\d{3}-\d{3}-\d{3}","Zapamietaj numery 111-112-211, 222-111-444 oraz 555-222-986")

for i in w:
    print(i.start(),i.end(),i.group(),"\n")
    
# Zastosowanie do tabeli danych
    
z = pd.Series(["Ala","ma","kota"])
print(z,"\n")

print(z.str.len(),"\n")
print(z.str.upper(),"\n")
print(z.str.replace("Ala","Ola"),"\n")


       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       