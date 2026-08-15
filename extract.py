even_num = int(input('provide number between 1 to 100 '))
result = []
for i in range(1, even_num + 1):
    if i % 2 == 0:
        result.append(i)
print(result)