# Написать функцию, принимающую на вход число 3<n<1000 и возвращающее все простые числа из диапазона [1,n].

def filter_primes(n):
    ...


if __name__ == '__main__':
    # Simple tests:
    print(filter_primes(4))  # [2,3]
    print(filter_primes(10))  # [2,3,5,7]
    print(filter_primes(-1))  # None
    print(filter_primes(3.5))  # [2,3]
