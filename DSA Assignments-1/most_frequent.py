arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

most_frequent = max(frequency, key=frequency.get)

print("Most Frequent Element:", most_frequent)
print("Frequency:", frequency[most_frequent])