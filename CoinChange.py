def greedy_coin_change(X, arr=[1, 2, 5, 10]):
    arr.sort(reverse=True)  # Mengurutkan array dari besar ke kecil
    coin_count = {}  # Dictionary untuk menyimpan berapa banyak setiap nilai koin yang digunakan
    
    for coin in arr:
        if X >= coin:
            count = X // coin  # Banyaknya koin yang digunakan
            X -= coin * count  # Mengurangi nilai X
            coin_count[coin] = count  # Simpan jumlah koin
        
        # Jika sudah X = 0, keluar dari loop
        if X == 0:
            break

    return coin_count

# Meminta input dari user
while True:
    X = int(input("Masukkan jumlah uang (harus lebih dari 0): "))
    if X > 0:
        break
    else:
        print("Error: Jumlah uang harus lebih dari 0. Silakan coba lagi.")

# Memanggil fungsi dan mencetak hasilnya
result = greedy_coin_change(X)

print(f"Hasil untuk jumlah uang {X}:")
for coin, count in result.items():
    print(f"Koin {coin}: {count} kali")
