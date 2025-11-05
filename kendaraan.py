# Kelas induk
class Kendaraan:
    def __init__(self, jenis, warna):
        self.jenis = jenis
        self.warna = warna

    def info_kendaraan(self):
        print(f"Jenis Kendaraan : {self.jenis}")
        print(f"Warna Kendaraan : {self.warna}")


# Subclass Mobil mewarisi dari Kendaraan
class Mobil(Kendaraan):
    def __init__(self, warna, merk, tahun):
        super().__init__("Mobil", warna)  # panggil constructor dari kelas induk
        self.merk = merk
        self.tahun = tahun

    def tampilkan_info(self):
        print("\n=== Informasi Mobil ===")
        self.info_kendaraan()
        print(f"Merk Mobil      : {self.merk}")
        print(f"Tahun Produksi  : {self.tahun}")


# Subclass Motor mewarisi dari Kendaraan
class Motor(Kendaraan):
    def __init__(self, warna, merk, tahun):
        super().__init__("Motor", warna)
        self.merk = merk
        self.tahun = tahun

    def tampilkan_info(self):
        print("\n=== Informasi Motor ===")
        self.info_kendaraan()
        print(f"Merk Motor      : {self.merk}")
        print(f"Tahun Produksi  : {self.tahun}")


# --- Bagian utama program ---
# if __name__ == "__main__":
    # Buat objek dari subclass
mobil1 = Mobil("Merah", "Toyota Avanza", 2020)
motor1 = Motor("Hitam", "Honda Beat", 2022)

    # Tampilkan informasi kendaraan
mobil1.tampilkan_info()
motor1.tampilkan_info()
