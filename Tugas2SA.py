import time

def sequential_search(arr, x):
    start = time.perf_counter_ns()
    for i in range(len(arr)):
        if arr[i] == x:
            end = time.perf_counter_ns()
            return i, end-start
    end = time.perf_counter_ns()
    return -1, end-start

arr1 = [i for i in range(10)]
arr2 = [i for i in range(100)]
arr3 = [i for i in range(1000)]
arr4 = [i for i in range(10000)]
arr5 = [i for i in range(100000)]
arr6 = [i for i in range(1000000)]

x1 = 9
x2 = 99
x3 = 999
x4 = 9999
x5 = 99999
x6 = 999999

result1 = sequential_search(arr1, x1)
result2 = sequential_search(arr2, x2)
result3 = sequential_search(arr3, x3)
result4 = sequential_search(arr4, x4)
result5 = sequential_search(arr5, x5)
result6 = sequential_search(arr6, x6)

print("Waktu pencarian angka 9 dari array 10 adalah", result1[1], "ns.")
print("Waktu pencarian angka 999 dari array 1000 adalah", result3[1], "ns.")
print("Waktu pencarian angka 9999 dari array 10000 adalah", result4[1], "ns.")
print("Waktu pencarian angka 99999 dari array 100000 adalah", result5[1], "ns.")
print("Waktu pencarian angka 999999 dari array 1000000 adalah", result6[1], "ns.")