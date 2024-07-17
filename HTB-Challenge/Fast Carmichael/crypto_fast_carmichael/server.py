#!/usr/bin/env python3

import sys
import random
from sympy import isprime, primerange, lcm, mod_inverse
from sympy.ntheory.residue_ntheory import crt


def kronecker_symbol(a, n):
    if n == 0:
        return 1 if abs(a) == 1 else 0
    if n == -1:
        return -1 if a < 0 else 1
    if n == 2:
        if a % 2 == 0:
            return 0
        elif a % 8 in [1, 7]:
            return 1
        else:
            return -1
    if n < 0:
        return kronecker_symbol(a, -1) * kronecker_symbol(a, -n)
    
    t = 1
    if a < 0:
        a = -a
        if n % 4 == 3:
            t = -t

    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                t = -t
        a, n = n, a  # Law of quadratic reciprocity
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n

    return t if n == 1 else 0


def miller_rabin(bases, n):
    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for b in bases:
        x = pow(b, s, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def search_pseudoprime(bases, coeffs, rlen, iters, verbose=False):
    modules = [4 * b for b in bases]

    residues = {}
    for b, m in zip(bases, modules):
        residues[b] = set()
        for p in primerange(3, 1024 * max(bases)):
            if kronecker_symbol(b, p) == -1:
                residues[b].add(p % m)

    sets = {}
    for b, m in zip(bases, modules):
        s = []
        for c in coeffs:
            s.append({(mod_inverse(c, m) * (r + c - 1)) % m for r in residues[b]})
        sets[b] = list(set.intersection(*s))

    assert len(coeffs) == 3

    coeffs_inv = [
        1,
        coeffs[1] - mod_inverse(coeffs[2], coeffs[1]),
        coeffs[2] - mod_inverse(coeffs[1], coeffs[2])
    ]

    mod = lcm(*modules, *coeffs)

    while True:
        choices = [random.choice(sets[b]) for b in bases]

        rem = crt(choices + coeffs_inv, bases + coeffs)[0]

        if verbose:
            print(f'[*] Searching pseudoprime...', file=sys.stderr)

        for i in range(iters):
            if verbose and i % 10000 == 0:
                print(f'{i}...')

            p1 = random.getrandbits(rlen) * mod + rem
            p2 = (p1 - 1) * coeffs[1] + 1
            p3 = (p1 - 1) * coeffs[2] + 1

            pprime = p1 * p2 * p3

            if miller_rabin(bases, pprime):
                break
        else:
            if verbose:
                print(f'[-] Failed to find pseudoprime, trying with another choices...', file=sys.stderr)
            continue

        if verbose:
            print(f'[+] Found pseudoprime!', file=sys.stderr)
            print(f'[+] P = {pprime}', file=sys.stderr)

        return pprime, [p1, p2, p3]


if __name__ == '__main__':
    rlen = 256
    iters = 30000
    verbose = True

    bases = list(primerange(2, 300))
    coeffs = [1, 313, 353]

    pprime, divisors = search_pseudoprime(bases, coeffs, rlen, iters, verbose)

    assert not isprime(pprime) and miller_rabin(bases, pprime)
