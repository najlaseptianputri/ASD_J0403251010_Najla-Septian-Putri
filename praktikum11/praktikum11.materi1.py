#=============================================================
# Nama   : Najla Septian Putri
# NIM    : J0403251010
# Kelas  : B/P1
# Implementasi Dasar Graph
#=============================================================

graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','B'],
    'D':['B','C']

}

for node in graph:
    print(node,"=>", graph[node])