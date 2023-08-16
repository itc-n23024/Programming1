from random import sample

n = []
while True:
    m = sample([chr(i) for i in range(97, 123)], 2)
    n.append(m)
    if m == ["n", "r"]:
        print(n)
        break
