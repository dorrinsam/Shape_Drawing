Input = [8,
         [[2, 0], [3, 0]],
         [[0, 2], [1, 1]],
         [[4, 1], [5, 2]],
         [[0, 4], [0, 3]],
         [[5, 3], [5, 4]],
         [[1, 6], [0, 5]],
         [[2, 7], [3, 7]],
         [[4, 6], [5, 5]]
         ]

result = ""
flag = True
for v in Input[1:]:
    if (v[0][1] == v[1][1]):
        for i in range(v[0][0]):
            result = result + " "
        result = result + "-"
        result = result + "-"
        print(result)
    elif (v[0][0] == v[1][0]):
        if (flag == False): continue
        print("|" + "    " + "|")
        print("|" + "    " + "|")
        flag = False

    else:
        if (v[0][0] < v[1][0] and v[0][1] > v[1][1]):
            print(" /  \ ")
            print("/    \ ")

        if (v[0][0] > v[1][0] and v[0][1] > v[1][1]):
            print("\    /")
            print(" \  /")
            break
print(result)
















































