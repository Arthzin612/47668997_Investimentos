import datetime
from dateutil.relativedelta import relativedelta

def calcular_montante(capital, taxa_juros, meses):
    return capital * (1 + taxa_juros / 100) ** meses

try:
    tipo = input("Tipo de investimento (CDB ou LCI): ")
    capital = float(input("Capital inicial: "))
    taxa = float(input("Taxa de juros mensal (%): "))
    meses = int(input("Número de meses: "))
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números válidos.")
    exit()

data_aplicacao = datetime.date.today()
data_vencimento = data_aplicacao + relativedelta(months=meses)
montante = calcular_montante(capital, taxa, meses)

print(f"Tipo de investimento: {tipo}")
print(f"Capital inicial: R$ {capital:.2f}")
print(f"Taxa de juros: {taxa:.2f}%")
print(f"Prazo: {meses} meses")
print(f"Montante final: R$ {montante:.2f}")
print(f"Data da aplicação: {data_aplicacao.strftime('%d/%m/%Y')}")
print(f"Data de vencimento: {data_vencimento.strftime('%d/%m/%Y')}")
