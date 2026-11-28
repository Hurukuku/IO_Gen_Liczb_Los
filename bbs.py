def blum_blum_shub(seed: int, iter: int, p1 = 5801, p2 = 6521):
    n = p1 * p2
    numbers = []
    for i in range(iter):
        seed = (seed**2) % n
        if seed in numbers:
            print("loop")
            return numbers
        numbers.append(seed)
    return numbers

print(blum_blum_shub(7, 100))