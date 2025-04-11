class Urzadzenie:
    def Wyswietl_komunikat(self, komunikat):
        print(komunikat)


class Pralka(Urzadzenie):
    def __init__(self):
        self.__numer_prania = 0 # Private

    def ustaw_program(self, numer_prania):
        ...
class Odkurzac(Urzadzenie):
    def __init__(self):
        self.__stan = False

    def on(self):
        ...

    def off(self):
        ...
if __name__ == '__main__':
    pralka = Pralka()
    odkurzac = Odkurzac()
