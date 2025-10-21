# ================================
# DOUBLE LINKED LIST PAKAI NIM (240705008) dari nama rahmad sriyanto
# ================================

# Kelas Node: menyimpan satu data + penghubung ke kiri & kanan
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # node sebelumnya
        self.next = None  # node sesudahnya


# Kelas DoubleLinkedList: operasi utama
class DoubleLinkedList:
    def __init__(self):
        self.kepala = None  # node pertama (head)

    # Tambah data di akhir list
    def tambah_data(self, data):
        simpul_baru = Node(data)
        if self.kepala is None:
            self.kepala = simpul_baru
        else:
            sekarang = self.kepala
            while sekarang.next is not None:
                sekarang = sekarang.next
            sekarang.next = simpul_baru
            simpul_baru.prev = sekarang

    # Hapus data sebelum data tertentu
    def hapus_sebelum(self, nilai):
        if self.kepala is None or self.kepala.next is None:
            print("List kosong atau hanya 1 data, tidak bisa hapus sebelum.")
            return

        sekarang = self.kepala
        while sekarang is not None and sekarang.data != nilai:
            sekarang = sekarang.next

        if sekarang is None or sekarang.prev is None:
            print("Tidak ada data sebelum", nilai)
            return

        hapus = sekarang.prev
        print(f"Menghapus data sebelum {nilai}, yaitu {hapus.data}")

        if hapus.prev is not None:
            hapus.prev.next = sekarang
            sekarang.prev = hapus.prev
        else:
            self.kepala = sekarang
            sekarang.prev = None

    # Hapus data setelah data tertentu
    def hapus_setelah(self, nilai):
        if self.kepala is None:
            print("List kosong.")
            return

        sekarang = self.kepala
        while sekarang is not None and sekarang.data != nilai:
            sekarang = sekarang.next

        if sekarang is None or sekarang.next is None:
            print("Tidak ada data setelah", nilai)
            return

        hapus = sekarang.next
        print(f"Menghapus data setelah {nilai}, yaitu {hapus.data}")

        if hapus.next is not None:
            hapus.next.prev = sekarang
            sekarang.next = hapus.next
        else:
            sekarang.next = None

    # Tambah data di tengah list
    def tambah_di_tengah(self, data):
        simpul_baru = Node(data)

        if self.kepala is None:
            self.kepala = simpul_baru
            return

        # Hitung panjang list
        panjang = 0
        sekarang = self.kepala
        while sekarang is not None:
            panjang += 1
            sekarang = sekarang.next

        tengah = panjang // 2  # posisi tengah
        sekarang = self.kepala
        for i in range(tengah - 1):  # berhenti di node sebelum tengah
            sekarang = sekarang.next

        simpul_baru.next = sekarang.next
        if sekarang.next is not None:
            sekarang.next.prev = simpul_baru
        sekarang.next = simpul_baru
        simpul_baru.prev = sekarang

    # Tampilkan isi list
    def tampilkan(self):
        sekarang = self.kepala
        while sekarang:
            print(sekarang.data, end=" <-> ")
            sekarang = sekarang.next
        print("None")


# ================================
# Bagian Utama
# ================================

dll = DoubleLinkedList()

# Ubah NIM menjadi list angka
nim = "240705008"
data_nim = [int(i) for i in nim]

# Masukkan ke dalam Double Linked List
for angka in data_nim:
    dll.tambah_data(angka)

print("Data awal (NIM teman kamu):")
dll.tampilkan()

# Contoh 1: Hapus data sebelum angka 7
print("\nHapus data sebelum 7:")
dll.hapus_sebelum(7)
dll.tampilkan()

# Contoh 2: Hapus data setelah angka 0
print("\nHapus data setelah 0:")
dll.hapus_setelah(0)
dll.tampilkan()

# Contoh 3: Tambah angka 9 di tengah
print("\nTambah data 9 di tengah:")
dll.tambah_di_tengah(9)
dll.tampilkan()
