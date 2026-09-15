arr = [10, 20, 30, 40, 50]

result = []

for i in range(len(arr) - 1, -1, -1):
    result.append(arr[i])

print(result)