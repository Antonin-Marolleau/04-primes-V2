''' Ce code utilise le code de @Antonin-Marolleau dans son intégralité
# et est soumis aux restrictions du
# plagiat sur @Antonin-Marolleau dans son intégralité ainsi
# que du copyright ©2024-2025 pour son
# auteur @Antonin-Marolleau
 Il suit le modèle de @Daniel-Courivaud
'''

from math import sqrt

#### Fonction secondaire


def isprime(p):
    '''
    return if the parameter @param p is a prime number
    '''
    if p<2:
        return False
    for i in range(2, int(sqrt(p))+1):
        if p%i == 0:
            return False
    return True

#### Fonction principale


def main():
    '''
    main
    '''
    # vos appels à la fonction secondaire ici

    print(169, isprime(169))
    print(5555, isprime(5555))
    print(3, isprime(3))

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
