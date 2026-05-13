#-------------------------------------------------------
# Nama      : Najla Septian Putri
# NIM       : J0403251010 
# Kelas     : B/P1
# Materi 1  : Implementasi Kruskal
#-------------------------------------------------------

# Menyiapkan daftar edge dalam format: (bobot, node1, node2)
# Data diambil dari contoh graph pada modul 
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Langkah 1: Mengurutkan seluruh edge berdasarkan bobot terkecil 
edges.sort()

mst = []
total_weight = 0

# Set sederhana untuk melacak node yang sudah terhubung (mencegah cycle sederhana)
connected = set()

# Langkah 2-6: Iterasi pemilihan edge 
for weight, u, v in edges:
    # Memilih edge jika setidaknya salah satu node belum ada di set 'connected'
    # Ini adalah logika sederhana untuk menghindari pembentukan cycle 
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Output hasil pembentukan Minimum Spanning Tree (MST) 
print("Minimum Spanning Tree (Kruskal):")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

#-------------------------------------------------------------------------------
#PENJELASAN MATERI 1 (ALGORITMA KRUSKAL):
#Algoritma Kruskal menggunakan pendekatan 'Greedy' secara global. 
#Cara kerjanya adalah dengan melihat seluruh jalur (edge) yang ada di graph, 
#lalu mengurutkannya dari yang termurah ke yang termahal. 
#Program akan mengambil jalur terkecil satu per satu selama jalur tersebut 
#menghubungkan titik baru dan tidak membentuk 'cycle' (jalan memutar yang kembali 
#ke titik asal). Kruskal sangat cocok digunakan ketika kita ingin membangun 
#jaringan dengan biaya total paling minimum dari daftar aset yang sudah ada.
#-------------------------------------------------------------------------------
