def kepernyore_kiir(szoveg):
    print(szoveg)


# Közvetlenül hívjuk a függvényt
kepernyore_kiir('Közvetlenül hívva')

# Közvetve hívjuk a függvényt
eljaras_hivatkozas = kepernyore_kiir
eljaras_hivatkozas('KÖZVETETTEN hívva')
