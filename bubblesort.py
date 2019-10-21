def bubble(list):
    for x in range(len(list) - 1, 0, -1):
        for i in range(x):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
list = [10, 30, 15, 20, 27, 20]
bubble(list)
print(list)