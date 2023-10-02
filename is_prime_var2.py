num = int(input("Enter a number to check: "))
nums_range = range(2, num + 1) 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for num in nums_range:
  if is_prime == True:
    primes.append(num)
print(primes)
