#Stwórz słownik dziesięciu słówek angielskich, indeksowany
# odpowiadającymi imsłówkami polskimi. Napisz program,
# który poprosi użytkownika o podanie słowapolskiego i
# wypisze tłumaczenie ze słownika.

def main():
    slownik = {"pies": "dog", "kot" : "cat", "mleko" : "milk",
               "miebieski": "blue", "czerwony": "red", "ptak": "bird",
               "czesc": "part", "twarz": "face", "kochanie": "love",
               "taniec":"dance"}

    slowo = input("Podaj slowo: ")
    print(slownik[slowo])

if __name__ == '__main__':
    main()