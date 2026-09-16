#RM568263_EX02

while True:
        preço_do_carro = float(input("Digite o preço do carro: "))
        if preço_do_carro > 0:
            break
        else:
            print("O preço deve ser um valor positivo.")

preço_a_vista = preço_do_carro * 0.80
print(f"O preço final à vista com desconto de 20% é: R${preço_a_vista:.2f}")

for num_parcelas in range(6, 61, 6):
    percentual = 0.03 * (num_parcelas / 6)
    preco_total_parcelado = preço_do_carro * (1 + percentual)
    valor_parcela = preco_total_parcelado / num_parcelas

    print(f"O preço final parcelado em {num_parcelas} X é de R$ {preco_total_parcelado:.2f} com parcelas de R$ {valor_parcela:.2f}")
