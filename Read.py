names = open('names.txt', 'r')
for x in range(5):
    x += 1
    for name in names.readlines(x):
        print(name)
names.close()
