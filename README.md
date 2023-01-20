# Index_stari
Python program na výpočet indexu stáří, umožňuje grafické rozhraní, vstupní hodnoty musí být zadávány bez mezer.

## Ukázka 

![image](https://user-images.githubusercontent.com/71701503/213783976-a6671913-5355-42f3-b515-c5de7da149e1.png)


## Jak ho spustit

Odkaz na stáhnutí: [https://github.com/MitasVit/Index_stari/blob/main/index_stari.exe?raw=true](https://github.com/MitasVit/Index_stari/blob/main/index_stari.exe?raw=true)

Upozornění pro zadávání hodnot: hodnoty čísel musí být vždy zadávané tak, aby neobsahovali mezery.

Pokud se vám zobrazí chybová zpráva typu: `Soubor XXX.dll se nenašel. Opravte reinstalací programu.` Tak to znamená, že vám chybí v počítači knihovny, díky kterým tento program běží. Můžete je stáhnout z: [https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

## Zkompilování ze zdrojového kódu
Umožňuje například měnit či upravovat program dle libovolných požadavků.

1. Pro zkompilování budete potřebovat program [Python](https://www.python.org/), jelikož tento program je napsaný ve stejnomeném jazyce. Odkaz na stránku se stáhnutím tohoto programu pro operační systém Windows: [odkaz na stránku s možnými instalacemi pro Windows](https://www.python.org/downloads/windows/), [přímý odkaz na stáhnutí](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)
2. V průzkumníkovi souborů otevřete složku `Stažené soubory` a rozklikněte instalátor, na úvodní stránce zaklikněte `Add Python to PATH`, poté rozklikněte Install now. Dokončete instalaci.
3. Najděte cestu typu `C:\Users\VAŠE_UŽIVATELSKÉ_JMÉNO\AppData\Local\Programs\Python\Python311\Scripts` v průzkumníkovi souborů. Poznámka: Tato cesta se může lišit na základě verze programu python.
4. Přidejte cestu do systémové proměné `PATH`. Toto můžete udělat například takto: zkopírujte výše uvedenou cestu z průzkumníka. Rozklikněte vyhledávání z hlavního panelu. Napište: `proměnné` a rozkliněte `Upravit proměné prostředí systému`. Zde rozklikněte tlačítko `Proměnné prostředí` nacházející se dole v tomto okně. Dále najděte v oddělení `Systémové proměnné` tu, s názvem `Path` a dvojklikem ji rozklikněte. Zde klikněte na tlačítko `Nový` a vložte cestu z průzkumníka. Potvrďte změny odklikáním tlačítek `Ok` ve všech otevřených oknech.
5. Otevřete příkazovou řádku a zadejte: `pip install pyinstaller`. Prozatím můžete minimalizovat příkazovou řádku a přejít k dalšímu kroku.
6. Otevřete poznámkový blok a vložte tento kód: 
```python 
import tkinter

hlavni = tkinter.Tk()

#tvorba platna kam se budou vykreslovat veci
platno = tkinter.Canvas(hlavni, width=200, height=270)
platno.pack()

ctext = tkinter.Text(hlavni)

#funkce vypocitej - vypocita hustotu zalidneni ze ziskanych hodnot z inputu -> prida text na obrazovku s vysledkem
def vypocitej():
    #txt je promena ktera drzi hodnotu hustoty zalidneni
    #ctext.delete("1.0")
    #ctext.delete("1.0", tkinter.END)
    #ctext.insert("1.0", "Index stáří v %: " + str(round(int(vel1.get()) / int(vel2.get())*100, 1)) + " %")
    txt="Index stáří v %: " + str(round(int(vel1.get()) / int(vel2.get())*100, 1)) + " %"
    platno.create_rectangle(40,200,300,500, fill="#f0f0f0", outline="#f0f0f0")
    platno.create_text(100, 220, text=txt)
    #platno.create_window(100,220, window=ctext)

#tvorba inputu a tlacitka
vel1 = tkinter.Entry(hlavni)
vel2 = tkinter.Entry(hlavni)
tlacitko = tkinter.Button(hlavni, text="Vypočítej", command=vypocitej)

#zobrazeni inputu a tlacitka (x,y, window=pouzit_okno)
platno.create_window(100,180,window=tlacitko)
platno.create_window(100,60,window=vel1)
platno.create_window(100,140,window=vel2)
platno.create_text(100, 20, text="Podíl obyvatel 65+")
platno.create_text(100, 100, text="Podíl obyvatel 0-14")

#hlavni cyklus behu okna
hlavni.mainloop()
```
7. Uložte tento soubor pod názvem: `index_stari.py` do složky: `C:/Users/VAŠE_UŽIVATELSKÉ_JMÉNO`.
8. Vraťte se do příkazové řádky a zadejte: 
```bash
python index_stari.py
```
Pro spuštění tohoto programu. Nebo:
```bash
pyinstaller --onefile index_stari.py
```
Pro zkompilování programu do aplikace `.exe`, kterou bude možné najít v podsložce dané složky s názvem: `dist`.

## Pro uživatele gitu nebo githubu

### Potřebné programy:
- Python (musí být přidaný do PATH)
- pip (součást pythonu - ale je ho potřeba také přidat do PATH)
- pyinstaller, instalace pomocí pip: `pip install pyinstaller`
- git nebo git desktop

### Spuštění
```
git clone https://github.com/MitasVit/Index_stari.git
cd Index_stari
python index_stari.py
```

### Zkompilování
```
git clone https://github.com/MitasVit/Index_stari.git
cd Index_stari
pyinstaller --onefile index_stari.py
```
