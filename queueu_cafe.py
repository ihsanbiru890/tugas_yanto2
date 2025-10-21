# queue_kafe.py
# Program antrian pengunjung kafe beserta pesanan (import dari queue_konsumen)

from queue_konsumen import Queue

def tampilkan_antrian_kafe(queue):
    if not queue.items:
        print("Antrian kosong.")
    else:
        print("Daftar antrian pengunjung:")
        for i, data in enumerate(queue.items, start=1):
            print(f"{i}. {data['nama']} - Pesanan: {data['pesanan']}")

def layani_pengunjung(queue):
    if not queue.items:
        print("Tidak ada pengunjung dalam antrian.")
    else:
        data = queue.items.pop(0)
        print(f"{data['nama']} dengan pesanan {data['pesanan']} telah selesai dilayani.")

def main():
    print("=== Sistem Antrian Pengunjung Pojok Cafe ===")
    antrian_kafe = Queue("Pengunjung Kafe")

    while True:
        print("\nMenu:")
        print("1. Tambah pengunjung dan pesanan")
        print("2. Layani pengunjung (keluar dari antrian)")
        print("3. Lihat antrian pengunjung")
        print("4. Keluar program")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            nama = input("Masukkan nama pengunjung: ")
            pesanan = input("Masukkan pesanan: ")
            antrian_kafe.enqueue({"nama": nama, "pesanan": pesanan})

        elif pilihan == "2":
            layani_pengunjung(antrian_kafe)

        elif pilihan == "3":
            tampilkan_antrian_kafe(antrian_kafe)

        elif pilihan == "4":
            print("Program selesai. Terima kasih telah mengunjungi Pojok Cafe!")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
