from time import time

def parsing(filename):
    with open(filename) as fd:
        r = fd.read().split(",")
        r = [i.split("-") for i in r]
    return r

def digits(n):
    answ = 0
    while n > 0:
        answ += 1
        n //= 10
    return answ

def part1(filename):
    r = parsing(filename)
    def do1(ran):
        n = int(ran[0])
        m = int(ran[1])
        l1 = len(ran[0])
        l2 = len(ran[1])
        answ = 0
        if (l1 == l2 and l1 % 2):
            return (0)
        for i in range(n, m + 1):
            d = digits(i)
            if (d % 2):
                continue
            d = 10**(d//2)
            answ += i if i % d == i // d else 0
        return answ
    return sum(map(do1, r))


def part2(filename):
    r = parsing(filename)
    def do1(ran):
        n = int(ran[0])
        m = int(ran[1])
        answ = 0
        for i in range(n, m + 1):
            s = str(i)
            l = len(s)
            for size in range(1, l//2 + 1 if not l % 2 else l // 3 + 1):
                if l % size == 0 and all(s[0:size] == s[j:j + size] for j in range(0, l, size)):
                    answ += i
                    break
        return answ
    return sum(map(do1, r))

start = time()
print(part1("input/d2"))
print(f"time: {1000 *(time() - start)}ms")

start = time()
print(part2("input/d2"))
print(f"time: {1000 *(time() - start)}ms")
