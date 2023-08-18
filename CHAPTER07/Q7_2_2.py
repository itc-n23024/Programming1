def square(x):
    if isinstance(x, (int, float)):
        return x**2
    else:
        raise ValueError("square", x)


print(square(8))
print(square("a"))
