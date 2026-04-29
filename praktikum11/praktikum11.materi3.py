#=============================================================
# Nama   : Najla Septian Putri
# NIM    : J0403251010
# Kelas  : B/P1
# Implementasi DFS
#=============================================================


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

def dfs(graph,node,visited):
# Fungsi untuk melakukan penelusuran menggunakan DFS
# Graph : disctionary yang menyimpan graph
# Node : menyimpan node yang sedang dikunjungi
# Visited : menyimpan node yang sudah dikunjungi

    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    # Tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # Lakukan dfs secara rekursi  ke tetangga tersebut
            dfs(graph,neighbor,visited)

# Set visited
visited = set()

# Menjalankan dfs dari A
dfs(graph,"A",visited)

# ======================================================================
# PENJELASAN
# ======================================================================
# DFS (Depth-First Search) adalah algoritma penelusuran graph yang mengunjungi node sedalam mungkin sebelum kembali dan melanjutkan ke node berikutnya.
# DFS menggunakan pendekatan rekursif atau menggunakan stack untuk menyimpan node yang akan dikunjungi berikutnya.
# Dalam contoh di atas, kita menggunakan pendekatan rekursif untuk melakukan DFS.
# Output dari kode di atas akan menampilkan urutan node yang dikunjungi selama penelusuran DFS dimulai dari node A.