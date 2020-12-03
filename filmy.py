'''
Moduł 7
Zadanie: Biblioteka filmów
'''

class Film:
    def __init__(self, tytul, rok, gatunek, liczba_odtworzenen):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzenen

    def play(self):
        self.liczba_odtworzen += 1

    def __str__(self):
        return f'{self.tytul} ({self.rok})'


class Serial(Film):
    def __init__(self, nr_odcinka, nr_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nr_odcinka = nr_odcinka
        self.nr_sezonu = nr_sezonu

    def __str__(self):
        return f'{self.tytul} S{self.nr_sezonu}E{self.nr_odcinka}'

film_pierwszy = Film("Pulp Fiction", 1994, "Gangsterski", 0)
film_drugi = Film("Ojciec Chrzestny", 1972, "Gangsterski", 0)
film_trzeci = Film("Forrest Gump", 1994, "Komediowy", 0)
film_czwarty = Film("Incepcja", 2010, "Sci-Fi", 0)
film_piaty = Film("Gladiator", 2000, "Historyczny", 0)

serial_pierwszy = Serial(1, 1, "Sherlok", 2010, "Kryminalny", 0)
serial_drugi = Serial(1, 1, "Przyjaciele", 1994, "Komediowy", 0)
serial_trzeci = Serial(1, 1, "House of Cards", 2013, "Polityczny", 0)

'''
print(film_pierwszy)
print(f'{film_pierwszy.tytul} ')
print(f'tytuł {serial_pierwszy.tytul}, S{serial_pierwszy.nr_sezonu}, E{serial_pierwszy.nr_odcinka}')
print(serial_drugi)
print(serial_trzeci)
'''
Biblioteka_filmow = []

def dodaj_film(film_lub_serial):
    Biblioteka_filmow.append(film_lub_serial)

dodaj_film(film_pierwszy)
dodaj_film(film_drugi)
dodaj_film(film_trzeci)
dodaj_film(film_czwarty)
dodaj_film(film_piaty)
dodaj_film(serial_pierwszy)
dodaj_film(serial_drugi)
dodaj_film(serial_trzeci)

print(Biblioteka_filmow[0])

print()
'''
def __repr__(self):
    return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"

def __eq__(self, other):
    return (
        self.make == other.make and
        self.model_name == other.model_name and
        self.top_speed == other.top_speed and
        self.color == other.color
    )
'''

'''
wizytowka_nr1 = WizytowkaBiznesowa(imie="Ksenia", nazwisko="Adamczyk", nazwa_firmy="Destiny Realty", stanowisko="technik",
                          adres_email="KseniaAdamczyk@armyspy.com", nr_tel="+48 658 325 951")
wizytowka_nr2 = WizytowkaBiznesowa(imie="Eligia", nazwisko="Kucharska", nazwa_firmy="Tapicerstwo EK", stanowisko="tapicer",
                          adres_email="EligiaKucharska@rhyta.com", nr_tel="+48 357 954 824")
wizytowka_nr3 = WizytowkaBiznesowa(imie="Asia", nazwisko="Lasińska", nazwa_firmy="S&W Cafeteria", stanowisko="Web designer",
                          adres_email="AsiaJasinska@teleworm.us", nr_tel="+48 831 319 458")
wizytowka_nr4 = WizytowkaBiznesowa(imie="Kunegunda", nazwisko="Górska", nazwa_firmy="Keeney's", stanowisko="kontroler",
                          adres_email="KunegundaGorska@jourrapide.com", nr_tel="+48 215 995 466")
wizytowka_nr5 = WizytowkaBiznesowa(imie="Bazyli", nazwisko="Pawlak", nazwa_firmy="Anthony's", stanowisko="kierowca",
                          adres_email="BazyliPawlak@dayrep.com", nr_tel="+48 883 115 654")
wizytownik = [wizytowka_nr1, wizytowka_nr2, wizytowka_nr3, wizytowka_nr4, wizytowka_nr5]
'''
'''
for nr_wizytowki in wizytownik:
    print(f"imię: {nr_wizytowki.imie}, nazwisko: {nr_wizytowki.nazwisko}, firma: {nr_wizytowki.nazwa_firmy}, e-mail: {nr_wizytowki.adres_email}")
po_imieniu = sorted(wizytownik, key=lambda Wizytowka: Wizytowka.imie)
po_nazwisku = sorted(wizytownik, key=lambda Wizytowka: Wizytowka.nazwisko)
po_emailu = sorted(wizytownik, key=lambda Wizytowka: Wizytowka.adres_email)
print("____________________________________________________________________________________________________________________")
for nr_wizytowki in po_imieniu:
    print(f"imię: {nr_wizytowki.imie}, nazwisko: {nr_wizytowki.nazwisko}, firma: {nr_wizytowki.nazwa_firmy}, e-mail: {nr_wizytowki.adres_email}")
print("____________________________________________________________________________________________________________________")
for nr_wizytowki in po_nazwisku:
    print(f"imię: {nr_wizytowki.imie}, nazwisko: {nr_wizytowki.nazwisko}, firma: {nr_wizytowki.nazwa_firmy}, e-mail: {nr_wizytowki.adres_email}")
print("____________________________________________________________________________________________________________________")
for nr_wizytowki in po_emailu:
    print(f"imię: {nr_wizytowki.imie}, nazwisko: {nr_wizytowki.nazwisko}, firma: {nr_wizytowki.nazwa_firmy}, e-mail: {nr_wizytowki.adres_email}")
'''