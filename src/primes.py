#   a single module(file) in a package(directory)

from factors import getFactors

def isPrime(n, foundPrimes=None):
    return len(getFactors(n))==2


def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

print(f'primes.py module name is {__name__}')

if __name__ == '__main__':
    print('this is a module, plz import using newline')