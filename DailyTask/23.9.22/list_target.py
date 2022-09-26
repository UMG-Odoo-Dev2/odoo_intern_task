def twoSumList(list, target):
    for i in range(len(list)):
            for j in range(i + 1, len(list)):
                if list[i] + list[j] == target:
                    # print(list[i], list[j])
                    return [i, j]

print(twoSumList([1,2,3,4], 6))