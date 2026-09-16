#RM568263_EX04

print("Escolha o tipo de investimento: ")
print("1. CDB")
print("2. LCI")
print("3. LCA")

while True:
    try:
        tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))
        if tipo in [1, 2, 3]:
            break
        else:
            print("O número do tipo de investimento deve ser 1, 2 ou 3. Tente novamente.")

    except ValueError:
        print("Tente novamente, mas dessa vez com números inteiros (1, 2 ou 3).")

while True:
    try:
        resgate = float(input("Digite o valor a ser resgatado: "))
        dias = int(input("Digite o número de dias que o valor permaneceu investido: "))
        break
    except ValueError:
        print("Digite números válidos para o valor e os dias.")

if tipo == 2 or tipo == 3:
    valor_imposto = 0.0
    print(f"O investimento (LCI/LCA) é isento de IR.")

else:
    aliquota = 0.0

    if dias > 720:
        aliquota = 0.15
    elif dias > 360:
        aliquota = 0.175
    elif dias > 180:
        aliquota = 0.20
    else:
        aliquota = 0.225

    valor_imposto = resgate * aliquota
    print(f"Alíquota aplicada: {aliquota * 100:.1f}%")

print(f"O valor do imposto de renda a ser pago é: R$ {valor_imposto:.2f}")


