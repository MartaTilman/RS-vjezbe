def isPrime(broj):
  if broj <= 1:
    return False
  for i in range(2, int(broj**0.5) + 1):
    if broj % i == 0:
      return False
  return True


print("Funkcija isPrime:")
print(isPrime(7))
print(isPrime(10))

def primes_in_range(start, end):
  prosti_brojevi = []
  for broj in range(start, end + 1): 
      if isPrime(broj):  
          prosti_brojevi.append(broj) 
  return prosti_brojevi

start = 10
end = 30
rezultat = primes_in_range(start, end)
print("Funkcija primes_in_range:",rezultat)  

input("Pritisnite Enter za izlaz...")
