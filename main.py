import sqlite3


def create_database():
    conn = sqlite3.connect('viesbutis.db')
    c = conn.cursor()


    c.execute('''CREATE TABLE IF NOT EXISTS klientai
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 vardas TEXT NOT NULL,
                 pavarde TEXT NOT NULL,
                 rezervacijos_id INTEGER,
                 FOREIGN KEY (rezervacijos_id) REFERENCES rezervacijos(id))''')


    c.execute('''CREATE TABLE IF NOT EXISTS rezervacijos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 kambario_numeris INT,
                 rezervacijo_kaina REAL NOT NULL,
                 sveciu_skaicius INTEGER NOT NULL)''')


    conn.commit()
    conn.close()


def insert_record(lentele):
    conn = sqlite3.connect('viesbutis.db')
    c = conn.cursor()

    if lentele == 'klientai':
        vardas = input("kliento vardas: ")
        pavarde = input("kliento pavarde: ")
        rezervacijos_id = input("rezervacijos numeris:")

        c.execute("INSERT INTO klientai (vardas, pavarde, rezervacijos_id) VALUES (?, ?, ?)", (vardas, pavarde, rezervacijos_id))
    elif lentele == 'rezervacijos':
        kambario_numeris = input("kambario numeris: ")
        rezervacijo_kaina = float(input("kaina: "))
        sveciu_skaicius = int(input("sveciu skaicius: "))
        c.execute("INSERT INTO rezervacijos (kambario_numeris, rezervacijo_kaina, sveciu_skaicius) VALUES (?, ?, ?)", (kambario_numeris, rezervacijo_kaina, sveciu_skaicius))

    conn.commit()
    conn.close()
    print("irasas ikeltas")


def read_records(lentele):
    conn = sqlite3.connect('viesbutis.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM {lentele}")
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()


def update_record(lentele):
    conn = sqlite3.connect('viebutis.db')
    c = conn.cursor()

    record_id = int(input("pasirinkite irasa"))

    if lentele == 'klientai':
        vardas = input("vardas: ")
        pavarde = input("pavarde: ")

        c.execute("UPDATE klientai SET vardas=?, pavarde=?, WHERE id=?", (vardas, pavarde, record_id))

    elif lentele == 'rezervacijos':
        kambario_numeris = input("kambario numeris: ")
        rezervacijo_kaina = float(input("kaina: "))
        sveciu_skaicius = int(input("sveciu skaicius: "))
        c.execute("UPDATE rezervacijos SET kambario_numeris=?, rezervacijo_kaina=?, sveciu_skaicius=? WHERE id=?", (kambario_numeris, rezervacijo_kaina, sveciu_skaicius, record_id))

    conn.commit()
    conn.close()
    print("irasas atnaujintas")


def delete_record(lentele):
    conn = sqlite3.connect('viesbutis.db')
    c = conn.cursor()

    record_id = int(input("kurį įrašą ištrinti"))

    c.execute(f"DELETE FROM {lentele} WHERE id=?", (record_id,))

    conn.commit()
    conn.close()
    print("istrinta irasas", record_id)


def main():
    create_database()

    while True:
        print("1. ideti irasa")
        print("2. rodyti irasus")
        print("3. keisti irasa")
        print("4. istrinti irasa")
        print("5. iseiti")
        choice = input("pasirinkite veiksma (1-5): ")

        if choice == '1':
            lentele = input("iveskite lenteles pavadinima (klientai/rezervacijos): ")
            insert_record(lentele)
        elif choice == '2':
            lentele = input("iveskite lenteles pavadinima (klientai/rezervacijos): ")
            read_records(lentele)
        elif choice == '3':
            lentele = input("iveskite lenteles pavadinima (klientai/rezervacjios): ")
            update_record(lentele)
        elif choice == '4':
            lentele = input("iveskite lenteles pavadinima (klientai/rezervacijos): ")
            delete_record(lentele)
        elif choice == '5':
            break
        else:
            print("bandykite vėl")


if __name__ == '__main__':
    main()