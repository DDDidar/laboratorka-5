string = str(input('Введите строку, в которой будем искать: \n'))

search = str(input('Введите что искать: \n'))

count = 0

for i in range(len(string)):

   if string[i: i + len(search)] == search:

       count += 1

print(count)
