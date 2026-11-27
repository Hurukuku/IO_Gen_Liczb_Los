def blum_blum_shub(p1: int, p2: int, seed: int, iter: int):
    n = p1 * p2
    numbers = []
    for i in range(iter):
        seed = (seed**2) % n
        if seed in numbers:
            print("loop")
            return numbers
        numbers.append(seed)
    return numbers

print(blum_blum_shub(5801, 6521, 7, 100))