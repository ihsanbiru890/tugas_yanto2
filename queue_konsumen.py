# queue_konsumen.py
# Program antrian konsumen di Pojok Cafe (dengan input nama)

class Queue:
    def __init__(self, nama_antrian):
        self.nama_antrian = nama_antrian
        self.items = []

    def enqueue(self, data):
        self.items.append(data)
        print(f"{data} masuk ke antrian {self.nama_antrian}.")

    def dequeue(self):
        if not self.items:
            print(f"Antrian {self.nama_antrian} kosong.")
            return None
        keluar = self.items.pop(0)
        print(f"{keluar} keluar dari antrian {self.nama_antrian}.")
        return keluar

    def tampilkan(self):
        if not self.items:
            print(f"Antrian {self.nama_antrian} kosong.")
        else:
            print(f"Isi antrian {self.nama_antrian}: {self.items}")

def main():
    print("=== Sistem Antrian Konsumen di Pojok Cafe ===")
    antrian = Queue("Konsumen")

    while True:
        print("\nMenu:")
        print("1. Tambah konsumen ke antrian")
        print("2. Layani konsumen (keluar dari antrian)")
        print("3. Lihat antrian")
        print("4. Keluar program")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            nama = input("Masukkan nama konsumen: ")
            antrian.enqueue(nama)

        elif pilihan == "2":
            antrian.dequeue()

        elif pilihan == "3":
            antrian.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
