#=============================================================
# Nama   : Najla Septian Putri
# NIM    : J0403251010
# Kelas  : B/P1
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
#=============================================================

# Graph merepresentasikan jalur eksplorasi
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 

def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 
    
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 

visited = set() 

print("DFS dari A:") 
dfs(graph, 'A', visited) 
print("\n")


# ======================================================================
# PENJELASAN
# ======================================================================
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# Jawaban: 
# Algoritma DFS (Depth-First Search) menggunakan pendekatan rekursi, di mana 
# di belakang layar ia memanfaatkan struktur data Stack (Tumpukan) yang 
# bersifat LIFO (Last In, First Out) pada "Call Stack" memori komputer. 
# Ketika DFS mengunjungi tetangga pertama, ia langsung memanggil dirinya 
# sendiri (rekursif) untuk masuk ke anak dari tetangga tersebut, dan terus 
# menelusuri cabang itu hingga mencapai ujung (node yang tidak punya tetangga 
# lagi). Setelah mentok, barulah ia mundur (backtrack) untuk mengeksplorasi 
# cabang lain.

# 2. Apa yang terjadi jika urutan neighbor diubah?
# Jawaban: 
# Arah penelusuran cabang terdalam akan berubah. DFS akan memprioritaskan 
# elemen pertama dalam daftar (list) tetangga. Misalnya, jika urutan pada node 
# 'A' diubah menjadi graph['A'] = ['C', 'B'] (node C di awal), maka DFS akan 
# menelusuri cabang C sampai habis (A -> C -> F), baru kemudian mundur untuk 
# mengeksplorasi cabang B (B -> D -> E).

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
# Jawaban: 
# - BFS (Breadth-First Search) menelusuri graph secara melebar (per level/tingkat).
#   Hasil BFS pada graph ini: A, B, C, D, E, F. Pendekatan ini melihat 
#   seluruh node yang dekat dengan titik awal terlebih dahulu.
# - DFS (Depth-First Search) menelusuri graph secara mendalam (per cabang).
#   Hasil DFS pada graph ini: A, B, D, E, C, F. Pendekatan ini menyisir 
#   satu jalur sampai tuntas terlebih dahulu sebelum pindah ke jalur sebelahnya.
