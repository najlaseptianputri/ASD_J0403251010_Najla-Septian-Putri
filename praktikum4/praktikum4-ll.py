#================================================================
#Nama   : Najla Septian Putri
#NIM    : J0403251010
#Kelas  : B/P1
#================================================================

#================================================================
#Implementasi Dasar: Node pada Linked List
#================================================================

#Membuat class node(merupakan unit dasar dari linked list)
class Node : #class implementasi stack
    def __init__ (self,data): #konstruktor 
        self.data = data #menyimpan nilai atau data
        self.next = None #pointer ke note berikutnya

#1. Membuat node satu per satu dengan cara memanggil konstruktor atau fungsi
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2. Menghubungkan node : A -> B -> C -> None
nodeA.next = nodeB #node B letaknya setelah pointer next A
nodeB.next = nodeC
#nodeC.next = None

#3. Menentukan node pertama (head)
head = nodeA

#4. Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)     #menampilkan data pada node saat ini
    current = current.next  #setelah current head berati current next/ pindah ke node berikutnya

#================================================================
#Implementasi Dasar: Linked List + Insert awal
#================================================================

class LinkedList: 
    def __init__(self):
        self.head = None #awalnya kosong 

    def insert_awal(self,data):
        #1. buat node baru
        nodeBaru = Node(data) #panggil class node

        #2. node baru mneunjuk ke head lama 
        nodeBaru.next = self.head

        #3. head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #menggeser head ke node brikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah : ", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("====list baru====")
ll = LinkedList() #instantiati objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()


