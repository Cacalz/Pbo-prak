import math

class Volume:
    @staticmethod
    def volume(bentuk, parameter):
        if bentuk == "kubus":
            sisi = parameter["sisi"]
            return sisi ** 3
        elif bentuk == "balok":
            panjang = parameter["panjang"]
            lebar = parameter["lebar"]
            tinggi = parameter["tinggi"]
            return panjang * lebar * tinggi 
        elif bentuk == "tabung":
            jari_jari = parameter["jari_jari"]
            tinggi = parameter["tinggi"]
            return math.pi * jari_jari ** 2 * tinggi 
        else:
            return "Bentuk bangun ruang tidak valid"

print("Nama : Calista Azzahra")
print("Nim  : 064002300008")

# Contoh penggunaan
parameter_kubus = {"sisi": 5}
print("Volume kubus adalah:", Volume.volume("kubus", parameter_kubus), "cm^3")

parameter_balok = {"panjang": 4, "lebar": 3, "tinggi": 6}
print("Volume balok adalah:", Volume.volume("balok", parameter_balok), "cm^3")

parameter_tabung = {"jari_jari": 2, "tinggi": 8}
print("Volume tabung adalah:", Volume.volume("tabung", parameter_tabung), "cm^3")
