digit = [6, 8, 2, 4, 1]
digit1 = [11, 12]
digit2 = [13, 14]

print("sorting digit : ", digit.sort(), digit)
print("sorting digit : ", digit.reverse(), digit)

digit.extend(digit1)
digit.extend(digit2)
print("extend digit : ", digit)

digit.insert(1, [15, 16])
digit.insert(2, (15, 16))
print("insert digit : ", digit)
