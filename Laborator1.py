import random
import csv

# Liste de prenume și nume de familie (exemplu simplificat)
prenume = ["Ion", "Maria", "Andrei", "Ana", "George", "Elena"]
nume_familie = ["Popescu", "Ionescu", "Georgescu", "Vasilescu", "Dumitru", "Stan"]


# Funcție pentru generarea unui CNP valid
def genereaza_cnp():
    sex = random.choice(["1", "2"])  # 1 - bărbat, 2 - femeie
    an = str(random.randint(1900, 2022))[-2:]  # Anul nașterii (ultimele două cifre)
    luna = str(random.randint(1, 12)).zfill(2)  # Luna nașterii
    zi = str(random.randint(1, 31)).zfill(2)  # Ziua nașterii
    judet = str(random.randint(1, 52)).zfill(2)  # Județul
    nr_secvential = str(random.randint(1, 999)).zfill(3)  # Număr secvențial
    control = str(random.randint(0, 9))  # Cifra de control
    return sex + an + luna + zi + judet + nr_secvential + control


# Generarea fișierului CSV
def genereaza_csv(numar_linii=1000000):
    with open('cnp_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['CNP', 'Prenume', 'Nume'])
        for _ in range(numar_linii):
            cnp = genereaza_cnp()
            prenume_random = random.choice(prenume)
            nume_random = random.choice(nume_familie)
            writer.writerow([cnp, prenume_random, nume_random])


# Dimensiunea tabelului de hash
TABLE_SIZE = 1000003  # o dimensiune primă mare


# Funcția de hash
def hash_function(key):
    # Funcție simplă de hash bazată pe suma cifrelor CNP-ului
    return sum(int(digit) for digit in key) % TABLE_SIZE


# Funcția de inserare a unui element în tabelul de hash
def insert_hash_table(table, cnp, nume):
    index = hash_function(cnp)
    if table[index] is None:
        table[index] = [(cnp, nume)]
    else:
        table[index].append((cnp, nume))


# Funcția de căutare a unui element în tabelul de hash
def search_hash_table(table, cnp):
    index = hash_function(cnp)
    if table[index] is not None:
        for entry in table[index]:
            if entry[0] == cnp:
                return entry[1]  # returnează numele asociat CNP-ului
    return None  # Dacă nu găsește CNP-ul


# Funcția de inițializare a tabelului de hash
def initialize_hash_table():
    return [None] * TABLE_SIZE


# Funcția de populare a tabelului de hash cu datele din CSV
def populare_hash_table(filename='cnp_data.csv'):
    hash_table = initialize_hash_table()
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Sarim peste antet
        for row in reader:
            cnp, prenume, nume = row
            insert_hash_table(hash_table, cnp, f"{prenume} {nume}")
    return hash_table


# Selectăm aleatoriu 1000 de CNP-uri și le căutăm în tabelul de hash
def analiza_performantei(hash_table, numar_cautari=1000):
    with open('cnp_data.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Sarim peste antet
        cnpuri = [row[0] for row in reader]

    selectate = random.sample(cnpuri, numar_cautari)
    iterații_totale = 0

    for cnp in selectate:
        # Căutăm CNP-ul în tabelul de hash și numărăm iterațiile
        index = hash_function(cnp)
        iterații = 0
        if hash_table[index] is not None:
            for entry in hash_table[index]:
                iterații += 1
                if entry[0] == cnp:
                    break
        iterații_totale += iterații

    medie_iteratii = iterații_totale / numar_cautari
    print(f"Numărul mediu de iterații pentru căutări: {medie_iteratii:.2f}")


# Generarea CNP-urilor și salvarea în CSV
print("Generăm fișierul CSV cu 1.000.000 de CNP-uri...")
genereaza_csv()

# Populăm tabelul de hash
print("Populăm tabelul de hash cu datele din fișierul CSV...")
hash_table = populare_hash_table()

# Analizăm performanța căutărilor
print("Analizăm performanța căutărilor...")
analiza_performantei(hash_table)