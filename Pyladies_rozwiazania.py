print ("Ucze się")
print ("Pythona!:)")
print('count przyjmujstring:'.count('na'))
print(len('Karolina Kowalska'))

def sum(dzien, miesiac, rok):
    return dzien+miesiac+rok
print(sum(28,5,2023))
def get_name(imie,nazwisko):
    razem=imie+" "+nazwisko
    return razem.title()
print("napisz:"+get_name("karolina","kowalska"))
imie_nazwisko_otrzymane = get_name('Karolina', 'Kowalska')

lista_uczestnikow = ['Kamil']
def zaaktualizuj_liste_uczestnikow(ls):
    ls.append('Dorota')
    return ls
zaaktualizuj_liste_uczestnikow(lista_uczestnikow)
print(lista_uczestnikow)

def dodaj_imie_do_listy(ls,imie):
    ls.append(imie)
    return ls
print(dodaj_imie_do_listy(lista_uczestnikow,'Karolina'))

def pole_kola(promien):
    wynik = 3.14 * (promien ** 2)
    return (wynik)
print(pole_kola(6))










      
    
      



    




