
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