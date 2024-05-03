n = int(input("Masukkan nilai n: "))

print("Part A:")
for i in range(n):
    print(i ** 2)

print("\nPart B Ganjil Genap:")
for i in range(n):
    if i % 2 != 0:
        print(i ** 2)
