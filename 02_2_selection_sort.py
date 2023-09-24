numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    min_index = i
    for current_index in range(i + 1, len(numbers)):
        if numbers[current_index] < numbers[min_index]:
            min_index = current_index
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(*numbers)


