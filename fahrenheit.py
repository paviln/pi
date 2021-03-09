def fahr_to_celcius(temp):
    return ((temp-32) * 5/9)

def celcius_to_fahr(temp):
    return ((temp * 9/5) + 32)

print(fahr_to_celcius(30))
print(celcius_to_fahr(30))