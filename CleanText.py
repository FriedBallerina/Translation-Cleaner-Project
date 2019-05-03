import pandas as pd
import matplotlib.pyplot as plot
import re
import sys

fail = 'tekstid.csv'
andmed = pd.read_csv(fail, delimiter=';', encoding = 'unicode_escape')
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 180)

tekstid = andmed['valmis'].tolist()
andmed = andmed.set_index('valmis')
teksti_suurused = []

def tekste_pole():
    print("Töötlemiseks vajalikke tekste pole")
    print("\n")
    print("*     " * 5)
    print("Programmi töö on lõppenud")
    sys.exit()
    
if len(tekstid) == 0:
    tekste_pole()

lk_hind = int(input("Sisesta kehtiv hind lk kohta: "))
ebavajalikud = input("Sisesta eemaldamisele kuuluvad sümbolid ilma tühikuta") + ('\n')

lk_arv = []

def tootle_fail(fail):

    sisu = open(fail, encoding = "UTF-8")
    sisu_tekst = sisu.read()
    numbriteta_sisu_tekst = sisu_tekst.translate({ord(i): None for i in ebavajalikud})
    numbriteta_sisu_tekst = re.sub(' +', ' ', numbriteta_sisu_tekst)
    teksti_suurused.append(len(numbriteta_sisu_tekst))   
    
for tekst in tekstid:
    tootle_fail(tekst)

andmed['maht'] = teksti_suurused
lk_arv = []

for i in teksti_suurused:
    lk_arv.append(round(i/1800, 2))

andmed['lk arv'] = lk_arv
hind = []

for i in lk_arv:
    hind.append(round(i * lk_hind, 2))

andmed['hind'] = hind

tolkede_suurused = pd.Series(andmed["maht"], index = tekstid)
tolkede_suurused.plot.bar(title = "Tõlkemahud")
#plot.show()

def kirjuta_faili(fail):
    uus_fail = fail.strip('.csv') + '_aruanne.csv'
    andmed.to_csv(uus_fail, sep =';', encoding='utf-8')

#kirjuta_faili(fail)
print(andmed)
print("\nKõik tekstid on töödeldud")
tekste_pole()
