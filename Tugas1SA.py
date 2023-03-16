import time

# fungsi untuk menghitung rata-rata
def hitung_rata_rata(bilangan):
    total = sum(bilangan)
    rata_rata = total / len(bilangan)
    return rata_rata

# mengambil input bilangan dari pengguna
bilangan = []
n = int(input("Masukkan jumlah bilangan: "))
for i in range(n):
    bilangan.append(float(input("Masukkan bilangan ke-{}: ".format(i+1))))

# menghitung rata-rata dan mengukur waktu yang diperlukan
start_time = time.time()
rata_rata = hitung_rata_rata(bilangan)
end_time = time.time()

# mencetak hasil
print("Rata-rata dari bilangan tersebut adalah: {:.2f}".format(rata_rata))
print("Waktu yang dibutuhkan untuk menghitung adalah: {:.6f} detik".format(end_time - start_time))5