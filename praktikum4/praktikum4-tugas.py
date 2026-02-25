#================================================================
#Nama   : Najla Septian Putri
#NIM    : J0403251010
#Kelas  : B/P1
#================================================================

#================================================================
#Tugas Hands-On: Sistem Antrian Bengkel Motor
#================================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None

class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, no, nama, servis):
        # Membuat node baru
        baru = Node(no, nama, servis)
        # Jika antrian kosong, front dan rear menunjuk ke node baru
        if self.is_empty():
            self.front = baru
            self.rear = baru
        else:
            # Sambungkan rear lama ke node baru, lalu pindahkan rear
            self.rear.next = baru
            self.rear = baru
        print(f"Pelanggan {nama} berhasil ditambahkan.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong! Tidak ada pelanggan yang dilayani.")
            return
        
        # Simpan data yang akan dilayani (data paling depan)
        dilayani = self.front
        print(f"Melayani pelanggan: [{dilayani.no}] {dilayani.nama} - {dilayani.servis}")
        
        # Geser front ke node berikutnya
        self.front = self.front.next
        
        # Jika setelah digeser front jadi None, maka rear juga harus None
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        if self.is_empty():
            print("Antrian saat ini kosong.")
            return
        
        print("\n--- Daftar Antrian Bengkel ---")
        curr = self.front
        while curr:
            print(f"No: {curr.no} | Nama: {curr.nama} | Layanan: {curr.servis}")
            curr = curr.next
        print("------------------------------")

# Indentasi def main disejajarkan ke kiri (paling luar)
def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("Terima kasih!")
            break
            
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
