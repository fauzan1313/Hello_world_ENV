class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas_permukaan(self):
        return 6 * (self.sisi ** 2)
