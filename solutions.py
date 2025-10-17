print("Hello World!")

def swap(a, b):
    return b, a

c = 5
d = 10
c, d = swap(c, d)
print("Swapped values:", c, d)

def avg(a, b, c):
    return (a + b + c) / 3;

print("Average of 4, 8, 12 is:", avg(4, 8, 12))