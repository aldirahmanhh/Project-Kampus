import re

filename = "inputan.txt" # Nama File 

with open(filename, "r") as f:
    ukuran_input_pertama = f.readline().rstrip().split()
    n = int(ukuran_input_pertama[0])
    m = int(ukuran_input_pertama[1])

    matriks = [f.readline().rstrip() for _ in range(n)]

hasil_dekode = ""
for i in range(m):
    for j in range(n):
        try:
            hasil_dekode += matriks[j][i]
        except IndexError:
            pass
# Aldi Rahman Hermawan
# 41822010004
pola = r'(?<=[\w])[^\w]+(?=[\w])'
cocokan = re.findall(pola, hasil_dekode)

for x in cocokan:
    hasil_dekode = hasil_dekode.replace(x, ' ', 1)

hasil_file = open("hasil.txt", "w")
hasil_file.write(hasil_dekode)
hasil_file.close()

print("File Hasil sudah dibuat silahkan dicek!")
print("Nama File: hasil.txt")
print("Hasil:", hasil_dekode)
