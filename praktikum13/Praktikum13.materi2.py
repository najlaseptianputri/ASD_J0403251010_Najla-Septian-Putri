#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Materi 2  : Graph III: Spanning Tree
#-------------------------------------------------------

import heapq

# Representasi weighted graph menggunakan dictionary 
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Set untuk mencatat node yang sudah dikunjungi (masuk ke dalam tree)
    visited = set([start])
    edges = []
    
    # Memasukkan semua tetangga dari node awal ke dalam priority queue (heap)
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    # Terus berjalan selama masih ada edge yang bisa dieksplorasi 
    while edges:
        # Mengambil edge dengan bobot terkecil 
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan belum dikunjungi, tambahkan ke MST untuk menghindari cycle 
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Tambahkan semua edge dari node baru yang baru saja dikunjungi ke heap 
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan algoritma Prim mulai dari node 'A' 
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree (Prim):")
for edge in mst:
    print(edge)
print("Total bobot =", total)

#-------------------------------------------------------------------------------
#PENJELASAN MATERI 2 (ALGORITMA PRIM):
#Algoritma Prim menggunakan pendekatan 'Greedy' secara lokal atau berbasis titik. 
#Berbeda dengan Kruskal yang langsung melihat semua jalur, Prim harus dimulai 
#dari satu titik awal (pada kode ini dimulai dari node 'A'). 
#Dari titik awal tersebut, algoritma akan 'tumbuh' dengan mencari tetangga 
#terdekat yang memiliki bobot kabel/jalan paling kecil. Begitu seterusnya 
#sampai semua titik terhubung. Prim sangat efisien jika graph memiliki 
#banyak jalur yang saling bersilangan (dense graph).
#-------------------------------------------------------------------------------
