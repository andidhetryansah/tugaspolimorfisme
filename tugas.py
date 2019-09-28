class FakultasTeknik:
    def __init__(self,Universitas, Fakultas, TahunAjar):
        self.univ = Universitas
        self.fak = Fakultas
        self.TA = TahunAjar
    def CetakData(self):
        print('Universitas   : ',self.univ)
        print('Fakultas      : ',self.fak)
        print('Tahun Ajaran  : ',self.TA)

class PendidikanTeknikMesin(FakultasTeknik):
    def __init__(self,Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self,Universitas, Fakultas, TahunAjar)
    def CetakData(self):
        print(70 * '=')
        print('Pendidikan Teknik Mesin')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di prodi Pendidikan Teknik Mesin adalah', self.JA)
        print(70 * '=')

class PTA(FakultasTeknik):
    def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)

    def CetakData(self):
        print('Pendidikan Teknik Arsitektus')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di prodi Pendidikan Teknik Arsitektur adalah', self.JA)
        print(70 * '=')
class Tekom(FakultasTeknik):
    def __init__(self, Universitas, Fakultas, TahunAjar, JumlahAngkatan):
        self.JA = JumlahAngkatan
        FakultasTeknik.__init__(self, Universitas, Fakultas, TahunAjar)

    def CetakData(self):
        print('Teknik Komputer')
        print('Universitas   : ', self.univ)
        print('Fakultas      : ', self.fak)
        print('Tahun Ajaran  : ', self.TA)
        print('Jumlah Angkatan di prodi Teknik Kompter adalah', self.JA)
        print(70 * '=')


def main():

    a = FakultasTeknik('UNM', 'Teknik', 2019, )
    a.CetakData()

    del a

    a = PendidikanTeknikMesin('UNM', 'Teknik', 2019, 9 )
    a.CetakData()

    b = PTA('UNM', 'Teknik', 2019, 9)
    b.CetakData()

    del b

    b = Tekom('UNM', 'Teknik', 2019, 2)
    b.CetakData()



if __name__ == "__main__":
    main()
