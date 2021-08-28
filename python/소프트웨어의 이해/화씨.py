fahr = 0


while fahr < 101:
    celsius = 5*(fahr-32)/9
    fahr += 10
    print('%d F = %.1f C'%(fahr, celsius))
