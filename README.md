# eestech24

## Kratek opis rešitve: 
Za izziv smo razvili aplikacijo, ki prikazuje napoved “zasedenosti” gora na podani datum. Aplikacija za vsako od makro lokacij na zemljevidu prikaže ali je njena zasedenost nizka, srednja ali visoka. Napoved deluje na modelu RandomForest, ki je naučen na podatkih, ki smo jih počistili in augmentirali. Dodali smo tudi podatke o vremenu, praznikih in premikajoče povprečje. 


## Repozitorij po mapah
- backend

    Koda za zalednje aplikacije. Hrani bazo podatkov. Izpostavlja API za dostop do podatkov.
    Uporablili smo ogrodje FastAPI. Baza SQLite.

- frontend

    Koda za spletno aplikacijo. Prikazuje zemljevid in omogoča pregled nad napovedmi zasedenosti gora.
    Uporablili smo ogrodje Vue.

- model

    Hrani natrenirani model RandomForest, ki napoveduje zasedenost gora.

- data

    Hrani podatke, ki smo jih uporabili za učenje modela.
    * gorske_nesreče - nismo uporabili
    * planinstvo - glavni podatki o zasedenosti gora na katere smo vezali vse ostale podatke
    * prazniki - podatki o praznikih v Sloveniji
    * prenočišča - nismo uporabili
    * vreme - podatki o vremenu v Ljubljani - sonce, temperatura, padavine - Postaja Bežigrad

- src

    Skripte za pregled, vizualizacijo in obdelavo podatkov ter učenje modela.
    
    \*.ipynb - Jupyter notebooki za obdelavo podatkov in učenje modelov

    constants.py - večinoma poti do modelov in podatkov
