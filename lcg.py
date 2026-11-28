def lcg(seed, modulus=10000, a=43, c=7, count=80):
    results = [seed]
    for i in range(1, count):
        results.append(((results[i-1] * a) + c) % modulus)

    return results[count-1]

print(lcg(50))
