numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


# Список без пропущенного элемента
valid_numbers = numbers[:4] + numbers[4 + 1:]

average = round(sum(valid_numbers) / len(numbers),2)
numbers[4] = average

print("Измененный список:", numbers)
