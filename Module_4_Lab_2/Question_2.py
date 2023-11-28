import sys
def egyptian_fraction(n, d):
    if n == 0 or d == 0:
        return

    if d % n == 0:
        print(d//n)
        return

    if n % d == 0:
        print(n//d)
        return

    if n > d:
        print(n//d)
        egyptian_fraction(n % d, d)
        return

    x = d // n + 1
    print(x)
    egyptian_fraction(n * x - d, d * x)


"""Main"""
if __name__ == "__main__":
    numerator = int(input())
    denominator = int(input())
    egyptian_fraction(numerator, denominator)
                                                                                                                            