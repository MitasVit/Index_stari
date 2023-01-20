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