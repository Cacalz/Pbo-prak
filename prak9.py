class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
class KalkulatorVolume:
    @staticmethod
    def volume_kubus(sisi):
        return sisi ** 3

    @staticmethod
    def volume_balok(panjang, lebar, tinggi):
        return panjang * lebar * tinggi

    @staticmethod
    def volume_tabung(jari_jari, tinggi):
        import math
        return math.pi * jari_jari ** 2 * tinggi

# Hitung volume
volume_kubus = KalkulatorVolume.volume_kubus(5)
volume_balok = KalkulatorVolume.volume_balok(4, 3, 6)
volume_tabung = KalkulatorVolume.volume_tabung(2, 8)

print("Nama : Calista Azzahra")
print("Nim  : 064002300008")

# Cetak volume
print("Volume kubus dengan sisi 5 adalah:", volume_kubus, "cm^3")
print("Volume balok dengan panjang 4, lebar 3, dan tinggi 6 adalah:", volume_balok, "cm^3")
print("Volume tabung dengan jari-jari 2 dan tinggi 8 adalah:", volume_tabung, "cm^3")
