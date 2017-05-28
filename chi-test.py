actual = [12, 8, 8, 77, 28, 20]
expected = [16.28758, 6.58824, 5.12418, 72.71242, 29.41176, 22.87582]

total = 0

for index, value in enumerate(actual):
    print(index)
    actual_value = float(value)
    expected_value = float(expected[index])
    compontent = ((actual_value - expected_value)**2)/expected_value
    print(compontent)
    total = total + compontent
    
print(total)