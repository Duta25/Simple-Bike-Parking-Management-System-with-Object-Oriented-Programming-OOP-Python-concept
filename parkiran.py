class Motor:
    def __init__(self, tipe, merk, plat) -> None:
        self.tipe = tipe
        self.merk = merk
        self.plat = plat
        self.status = False


class Parkiran:
    def __init__(self):
        self.tarif = {
            "bebek": 2000,
            "sport": 3000
        }
        self.parkiran = []
        self.total = 0

    def info(self, plat):
        for motor in self.parkiran:
            if motor.plat == plat:
                if motor.status:
                    print("Terparkir")
                else:
                    print("Motor tidak Terparkir")
                return
        print("Motor tidak ditemukan")

    def parkir(self, tipe, merk, plat) -> str:
        for motor in self.parkiran:
            if motor.plat == plat:
                print("Motor sudah terparkir")
                return
            
        motor = Motor(tipe, merk, plat)
        motor.status = True
        self.parkiran.append(motor)

        print(f"Motor dengan plat {plat} telah parkir")

    def hitung_harga(self, plat, waktu): #perjam
        for motor in self.parkiran:
            if motor.tipe in self.tarif:
                self.total = self.tarif[motor.tipe] * waktu
                self.status = False
                self.parkiran.remove(motor)
                print(f"Motor dengan plat {plat} keluar, Total Bayar: {self.total}")
                return
        print("Motor tidak ditemukan")
            
    def data_parkiran(self):
        for motor in self.parkiran:
            print(motor.tipe, motor.merk, motor.plat)

p = Parkiran()

p.info("BA 9128 BS")
p.parkir("bebek", "supra", "BA 9128 BS")
p.parkir("sport", "ZX", "BA 8372 AB")
p.hitung_harga("BA 9128 BS", 2)
p.data_parkiran()
p.hitung_harga("BA 8372 AB", 2)




    
