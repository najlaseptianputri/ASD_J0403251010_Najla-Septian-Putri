class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # --- LATIHAN 4: MENGGABUNGKAN DUA LIST ---
    def merge_list(self, other_list):
        # 1. Jika list utama (self) kosong, ambil head dari list lain
        if not self.head:
            self.head = other_list.head
            return

        # 2. Jika list lain kosong, tidak ada yang perlu digabung
        if not other_list.head:
            return

        # 3. Cari node terakhir di list utama
        temp = self.head
        while temp.next:
            temp = temp.next
        
        # 4. "Tali" terakhir disambungkan ke kepala list kedua
        temp.next = other_list.head
        print("Sistem: Penggabungan berhasil dilakukan.")

    # Fungsi untuk menampilkan hasil
    def display(self, nama_list):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
        print(f"{nama_list}: {' -> '.join(nodes)} -> None")

# --- BAGIAN EKSEKUSI (WAJIB ADA AGAR OUTPUT KELUAR) ---
print("---Latihan 4---")
# 1. Buat List Pertama (L1)
L1 = LinkedList()
L1.insert_at_end(1)
L1.insert_at_end(3)
L1.insert_at_end(5)
L1.insert_at_end(7)
L1.display("List 1")

# 2. Buat List Kedua (L2)
L2 = LinkedList()
L2.insert_at_end(2)
L2.insert_at_end(4)
L2.insert_at_end(6)
L2.insert_at_end(8)
L2.display("List 2")

print("-" * 30)

# 3. Panggil fungsi Merge (Menggabungkan L2 ke dalam L1)
L1.merge_list(L2)

# 4. Tampilkan hasilnya (L1 sekarang berisi data L2 juga)
L1.display("Hasil Gabungan (L1 + L2)") 