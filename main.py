def find_formula(n):
    if n == 1:
        return '1'
    if n % 2 == 0:
        return '2 * ' + find_formula(n // 2)
    for i in range(3, n + 1, 2):
        if n % i == 0:
            return str(i) + ' * ' + find_formula(n // i)
    return find_formula(n)

def reduce(func, args):
    if len(args) == 1:
        return args[0]
    return func(args[0], reduce(func, args[1:]))

def lcm(args):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a b // gcd(a, b)
    return reduce(lcm, args)

def gcd(args):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return reduce(gcd, args)

args = [int(x) for x in input().split()]
print('lcm =', lcm(args))
gcd = gcd(args)
print('lcm formula =', find_formula(lcm(args)))
