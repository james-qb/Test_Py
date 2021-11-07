import urllib.parse

data = "中国"
quo_data = urllib.parse.quote(data)
print(quo_data)

a_list = [1, 2], [2, 3], [3, 4], [4, 5]
print(*a_list)
print(list(zip(*a_list)))

a = [1, 2, 3, 4, 5, 6]
# print(list(zip(*a)))
for i in range(10):
    for j in range(10):
        if i + j > 5:
            print(i, j)
            break

for i in range(5):
    b = b + 1
    print(b)
