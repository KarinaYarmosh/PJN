#Sierżant Thomson postanowił cenzurować listy,
# które otrzymują jego żołnierze.
# Zkażdego listu postanowił skreślić co trzecią linijkę,
# oraz dodatkowo skreślać te, którezawierają słowo "kocham"
# (obojętnie, czy pisane wielką, czy małą literą).
# Pomóżsierżantowi w tym zadaniu. Napisz program, który czyta
# list z jednego pliku, a w innympliku zapisuje jego ocenzurowaną wersję.
# Ocenzurowane linie powinny być zastąpioneciągiem znaków '*****'

def main():
    with open("zad4.txt", "r") as start_file:
        with open("zad4_2.txt", "w") as end_file:
            for i, line in enumerate(start_file):
                if i%3==2:
                    end_file.write("*********\n")
                else:
                    end_file.write(line.replace("kocham", "*****") and line.replace("Kocham", "*****"))
if __name__ == '__main__':
    main()