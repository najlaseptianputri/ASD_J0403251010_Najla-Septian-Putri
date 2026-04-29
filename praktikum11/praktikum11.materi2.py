#=============================================================
# Nama   : Najla Septian Putri
# NIM    : J0403251010
# Kelas  : B/P1
# Implementasi BFS
#=============================================================

# Struktur data untuk membuat antrian, kita gunakan dar library collection bawaan Phyton
from collections import deque

# Representasi graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

def bfs(graph,start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # Graph adalah dictionary yang menyimpan struktur dari data graph yang akan diolah
    # Start adalah node awal untuk melakukan penelusuran

    # Queue untuk menyimpan node yang akan diproses/dibaca
    queue = deque()
    
    # Variabel untuk menyimpan node yang sudha diproses/dibaca
    visited = set()

    # Masukkan node awal ke queue
    queue.append(start)

    # Tandai node awal sebagai node yang sudah dihubungi
    visited.add(start)

    while queue:
        # Mengambil node paling depan dari queue
        node = queue.popleft()

        # Tampilkan node yang sedang dikunjungi
        print(node,end=" ")

        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # Jika tetangga belum dikunjungi
            if neighbor not in visited:
                # Tandai sebagaai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan tetangga ke queue untuk diproses
                queue.append(neighbor)

# Menjalankan BFS dari node A
bfs(graph,'A')

# ======================================================================
# PENJELASAN
# ======================================================================
# BFS (Breadth-First Search) adalah algoritma penelusuran graph yang mengunjungi semua node pada level yang sama sebelum melanjutkan ke level berikutnya.
# Dalam implementasi di atas, kita menggunakan queue untuk menyimpan node yang akan diproses. Kita juga menggunakan set untuk menyimpan node yang sudah dikunjungi agar tidak terjadi pengulangan.
# Algoritma BFS dimulai dengan memasukkan node awal ke dalam queue dan menandainya sebagai sudah dikunjungi. Kemudian, selama queue tidak kosong, kita mengambil node paling depan dari queue, menampilkannya, dan memeriksa semua tetangganya.
# Jika tetangga belum dikunjungi, kita menandainya sebagai sudah dikunjungi dan memasukkannya ke dalam queue untuk diproses nanti.
# Output dari kode di atas akan menampilkan urutan node yang dikunjungi selama penelusuran BFS, dimulai dari node A.