arr = [1, 2, 3, 5, 6, 7]

n = 7

total = n * (n + 1) // 2

for num in arr:
    total = total - num

print("Missing Number:", total)