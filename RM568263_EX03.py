#RM568263_EX03

while True:
    valor_da_divida = float(input("Digite o valor da dívida: "))
    if valor_da_divida > 0:
        break
    else:
        print("Valor da divida deve ser maior que 0!")

print(f"Total:R$ {valor_da_divida:.2f} Juros: R$ 0.00 Número de parcelas:1 Valor da parcela:R$ {valor_da_divida:.2f}")

for numero_de_parcela in range(3,13,3):
    percentual = 0.05 + (0.05 * (numero_de_parcela / 3))
    juros = valor_da_divida * percentual
    preco_total_parcelado = valor_da_divida * (1 + percentual)
    valor_parcela = preco_total_parcelado/numero_de_parcela

    print(f"Total:R$ {preco_total_parcelado:.2f} Juros: R$ {juros:.2f} Número de parcelas:{numero_de_parcela} Valor da parcela:R$ {valor_parcela:.2f}")

