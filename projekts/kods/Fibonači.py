fibonacci = [0, 1]

for i in range(2, 100):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for num in reversed(fibonacci):
    print(num)
