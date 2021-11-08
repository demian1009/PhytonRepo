# Beispiel für die Berechnung des Schnittpunktes 2-er Geraden mittels Itaration
def generatePrimeNumbers(fromNumber, toNumber):

    print("Generating prime numbers...")

    x = fromNumber
    for x in range(fromNumber, toNumber):
        if isPrime(x):
            print("{} is a prime number".format(x))


def isPrime(number):
    if number >= 1 and number <= 3:
        return True
    for x in range(2, number - 1):
        if number % x == 0:
            return False
    return True


print("\n1. example:")
generatePrimeNumbers(1, 1000)
