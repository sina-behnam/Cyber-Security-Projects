import random

def is_prime(n):
    """
    Returns True if n is prime.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def module_inverse(a, m):
	"""
	Returns the modular inverse of a % m.
	"""
	if a < 0 or m <= a:
		a = a % m
	if a == 0:
		return 0
	if a == 1:
		return 1
	# Calculate using the Extended Euclidean Algorithm:
	lm, hm = 1, 0
	low, high = a, m
	while low > 1:
		r = high//low
		nm, new = hm-lm*r, high-low*r
		lm, low, hm, high = nm, new, lm, low
	return lm % m

def module_power(a, n, m):
    """
    Returns a^n % m.
    """
    if n == 0:
        return 1
    if n == 1:
        return a % m
    if n % 2 == 0:
        return module_power(a**2 % m, n//2, m)
    else:
        return a * module_power(a**2 % m, (n-1)//2, m) % m

def get_all_prime_factors(n):
    """
    Returns a list of all prime factors of n.
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def generate_n_digit_prime_number(n):
    """
    Generates a prime number of n digits.
    """
    while True:
        number = random.randint(10**(n-1), 10**n)
        if is_prime(number):
            return number

