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