import csv

ARQUIVO = "data/gastos.csv"

def registrar_gasto():
    data = input("Data (AAAA-MM-DD): ")
    categoria = input("Categoria: ")
    descricao = input("Descrição: ")
    valor = input("Valor: ")

    with open(ARQUIVO, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([data, categoria, descricao, valor])

    print("Gasto registrado com sucesso!")

def listar_gastos():
    print("\n=== LISTA DE GASTOS ===")
    try:
        with open(ARQUIVO, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Data: {row[0]}, Categoria: {row[1]}, Descrição: {row[2]}, Valor: {row[3]}")
    except FileNotFoundError:
        print("Nenhum gasto registrado ainda.")
