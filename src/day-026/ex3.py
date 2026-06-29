with open("file1.txt") as file1:
  file1_data = [line.strip() for line in file1.readlines()]
with open("file2.txt") as file2:
  file2_data = [line.strip() for line in file2.readlines()]

print(file1_data)
print(file2_data)


result = [int(num) for num in file1_data if num in file2_data]
print(result)