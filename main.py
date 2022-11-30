import pandas

planilha = pandas.read_excel('./planilha.xlsx', usecols=[0, 1, 3])
values = planilha.values

arquivo = open("teste.txt", "a")


def parse(data):
    for d in data:
        first = f'  {d[0]}'.ljust(15)
        second = d[1].ljust(100)
        last = d[2]
        arquivo.write(f"{first}{second}{last}" + "\n")


parse(values)
