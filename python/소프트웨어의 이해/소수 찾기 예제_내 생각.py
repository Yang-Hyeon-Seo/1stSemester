n=4
prime_number=[]
while n < 100:
    for i in range(2, n):
        not_prime=[]
        if n%i == 0:
            not_prime.append(n)
        if not_prime == False:
            prime_number.append(n)
            
    n +=1

print(prime_number)
