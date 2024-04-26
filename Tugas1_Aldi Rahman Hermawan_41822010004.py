print("Selamat Datang di Aplikasi Perhitungan Nilai Mahasiswa")

tugas = float(input("Masukkan Nilai Tugas : "))
uts = float(input("Masukkan Nilai UTS : "))
uas = float(input("Masukkan Nilai UAS : "))

na = (0.25 * tugas) + (0.35 * uts) + (0.4 * uas)

if na > 85:
    nh = 'A'
elif na >= 80 and na <= 84:
    nh = 'A-'
elif na >= 75 and na <= 79:
    nh = 'B+'
elif na >= 70 and na <= 74:
    nh = 'B'
elif na >= 65 and na <= 69:
    nh = 'B-'
elif na >= 60 and na <= 64:
    nh = 'C+'
elif na >= 55 and na <= 59:
    nh = 'C'
elif na >= 50 and na <= 54:
    nh = 'C-'
elif na >= 30 and na <= 49:
    nh = 'D'
else:
    nh = 'E'
print("Nilai Akhir : ", na)
print("Nilai Dalam Huruf : ", nh)

## Aldi Rahman Hermawan
## 41822010004