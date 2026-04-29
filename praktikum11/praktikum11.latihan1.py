#=============================================================
# Nama   : Najla Septian Putri
# NIM    : J0403251010
# Kelas  : B/P1
# Latihan 1 (Studi Kasus BFS - Jaringan Pertemanan)
#=============================================================

from collections import deque 

# Graph merepresentasikan hubungan antar lokasi
graph = { 
    'Rumah': ['Sekolah', 'Toko'], 
    'Sekolah': ['Perpustakaan'], 
    'Toko': ['Pasar'], 
    'Perpustakaan': [], 
    'Pasar': [] 
} 

def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 

    visited.add(start) 
    
    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 
        
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 

print("BFS dari Rumah:") 
bfs(graph, 'Rumah') 
print("\n")


# ======================================================================
# PENJELASAN
# ======================================================================
# 1. Node mana yang dikunjungi pertama?
# Jawaban: 
# Node yang dikunjungi pertama kali adalah 'Rumah' karena 'Rumah' 
# dideklarasikan sebagai titik awal (start node) penelusuran. Setelah itu, 
# node yang dikunjungi selanjutnya adalah tetangga terdekat level 1 dari 
# 'Rumah', yaitu 'Sekolah' kemudian 'Toko'.

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# Jawaban: 
# BFS (Breadth-First Search) sangat cocok mencari jalur terdekat (pada graph 
# tidak berbobot/unweighted) karena algoritma ini menelusuri node secara 
# melebar level demi level. BFS akan memeriksa semua node yang berjarak 1 
# langkah sebelum mengecek node yang berjarak 2 langkah, dan seterusnya. 
# Oleh karena itu, lokasi/node target yang pertama kali ditemukan dipastikan 
# merupakan rute dengan jarak langkah terpendek.

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
# Jawaban: 
# Urutan kunjungan sangat bergantung pada struktur ketetanggaan (adjacency list). 
# Jika urutan tetangga diubah, misalnya graph['Rumah'] = ['Toko', 'Sekolah'], 
# maka 'Toko' akan masuk Queue (antrean) lebih dulu dan dicetak sebelum 'Sekolah'.
# Jika struktur graphnya diubah (misal ada tambahan jalur baru langsung dari 
# 'Rumah' ke 'Perpustakaan'), maka 'Perpustakaan' akan dieksplorasi lebih awal 
# di level pertama bersama dengan 'Sekolah' dan 'Toko'.