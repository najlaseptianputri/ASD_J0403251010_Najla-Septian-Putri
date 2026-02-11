class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    # Fungsi untuk menambah data (agar bisa ditest)
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head # Menunjuk ke diri sendiri (Circular)
            return
        
        temp = self.head
        while temp.next != self.head: # Berhenti sebelum balik ke head
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head # Node terakhir menunjuk ke head

    # --- LATIHAN 2: FUNGSI PENCARIAN ---
    def search(self, key):
        if self.head is None:
            print("Output: List Kosong!")
            return False

        temp = self.head
        found = False
        
        # Menggunakan perulangan untuk mengecek setiap node
        while True:
            if temp.data == key:
                found = True
                break
            temp = temp.next
            # Berhenti jika sudah kembali ke awal (Head)
            if temp == self.head:
                break
        
        if found:
            print(f"Output: Elemen {key} DITEMUKAN dalam list.")
        else:
            print(f"Output: Elemen {key} TIDAK DITEMUKAN.")
        return found

# --- BAGIAN EKSEKUSI (WAJIB ADA AGAR OUTPUT MUNCUL) ---
csll = CircularSinglyLinkedList()

# 1. Tambahkan data
csll.insert_at_end(3)
csll.insert_at_end(7)
csll.insert_at_end(12)
csll.insert_at_end(19)
csll.insert_at_end(25)

print("---Latihan 2---")
# 2. Panggil fungsi search (Ini yang membuat output muncul)
csll.search(12)  # Harusnya ditemukan
csll.search(10) # Harusnya tidak ditemukan 