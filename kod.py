import itertools
cargo = [40, 20, 40, 9, 15, 2, 6, 40, 20, 7, 5, 3, 9, 19]
pojemnosckontenera = 50
kontener = []
min_ilosc_kontenerow = len(cargo)
#Problem jest złozony. Jedyne pewne podejscie jest sprawdzenie wszystkich mozliwych kombinacji 

min_ilosc_kontenerow = len(cargo)

def uloz_elementy(sklad):
    ilosc_kontenerow = 1
    pelnosc_kontenera =0 
    for przedmiot in sklad:
        if pelnosc_kontenera + przedmiot < pojemnosckontenera:
            pelnosc_kontenera += przedmiot
        else:
            pelnosc_kontenera = przedmiot
            ilosc_kontenerow +=1
    return ilosc_kontenerow
        

kombinacje = itertools.permutations(cargo,len(cargo))
for kombb in kombinacje:
    ilosc_kontenerow = uloz_elementy(kombb)
    if min_ilosc_kontenerow > ilosc_kontenerow:
        print(f"{kombb} : {ilosc_kontenerow}")
        min_ilosc_kontenerow = ilosc_kontenerow
    

    