def FF(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results


numbers = [1, 2, 3, 4]
print(FF(*numbers))
