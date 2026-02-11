class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Fungsi pembantu untuk menambah data agar bisa ditest
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # --- LATIHAN 1: SOLUSI DELETE NODE ---
    def delete_node(self, key):
        temp = self.head
        
        # 1. Jika list kosong
        if temp is None:
            print("List kosong, tidak ada yang dihapus.")
            return

        # 2. Jika node yang mau dihapus adalah HEAD (paling depan)
        if temp is not None and temp.data == key:
            self.head = temp.next  # Geser head ke orang di belakangnya
            temp = None            # Buang node lama dari memori
            print(f"Node {key} berhasil dihapus (posisi di Head).")
            return

        # 3. Mencari node yang akan dihapus (sambil mencatat node sebelumnya)
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # 4. Jika datanya tidak ditemukan sampai akhir list
        if temp is None:
            print(f"Node {key} tidak ditemukan di dalam list.")
            return

        # 5. Proses "pemutusan tali": Hubungkan node sebelum ke node sesudah
        prev.next = temp.next
        temp = None
        print(f"Node {key} berhasil dihapus.")

    # --- FUNGSI DISPLAY (Agar output tidak muncul alamat memori) ---
    def display(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data)) # Ambil .data-nya, bukan objek nodenya
            temp = temp.next
        print(" -> ".join(nodes) + " -> None")

# --- CARA TEST AGAR OUTPUT SESUAI ---
print("---Latihan 1---")
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)

print("List sebelum dihapus:")
llist.display()

# Tes hapus angka 20
llist.delete_node(2)

print("List sesudah dihapus:")
llist.display() 