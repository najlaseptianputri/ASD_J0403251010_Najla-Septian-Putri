#================================================================
#Nama   : Najla Septian Putri
#NIM    : J0403251010
#Kelas  : B/P1
#================================================================

#================================================================
#Implementasi Dasar: Queue berbasis NLinked List
#================================================================

class Node :
    def __init__ (self,data): #konstruktor 
        self.data = data #menyimpan nilai atau data
        self.next = None #pointer ke note berikutnya

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def enqueue(self,data):
        #menambah data di belakang (rear)
        nodeBaru = Node(data)

        

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear yang menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #Jika queue tidak kosong:
        #Rear lama menunnuk ke node baru
        self.rear.next = nodeBaru #setelah ekor yang lama
        #rear pindah ke node baru
        self.rear = nodeBaru

    def dequeue(self):
        #menghapus data dari depan


        #1. lihat data yang paling depan
        data_terhapus = self.front.data

        #2. geser front ke node berikutnya
        self.front = self.front.next

        #3. jika setelah geser frontmenjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None
        
        return data_terhapus
    
    def tampilkan(self):
        #menamilkan isis queue dari front ke rear
        current = self.front
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")

#Instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()