def loop():
    for i in range(1, 101):
        print(i)
loop()

def div():
    numbers = []
    for i in range(1, 1001):
        if i % 2 == 0:
            numbers.append(i)
    print(numbers)
    print(f"There are {len(numbers)} numbers between 1 and 1000 are divisible by 2.")
div ()