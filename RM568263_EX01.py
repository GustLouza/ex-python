#RM568263_EX01

DIAS = ("segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira")
segunda_feira = 0
terça_feira = 0
quarta_feira = 0
quinta_feira = 0
sexta_feira = 0

while True:
    qtd_colaboradores = int(input("Informe o número de colaboradores:"))
    if qtd_colaboradores > 0:
        break
    else:
        print("Digite um número inteiro maior que zero")

for i in range(qtd_colaboradores):
    while True:
        voto = input(f"Informe o dia da sua preferência para a live {DIAS}: ").lower()

        if voto == "segunda-feira":
            segunda_feira += 1
            break
        elif voto == "terça-feira":
            terça_feira += 1
            break
        elif voto == "quarta-feira":
            quarta_feira += 1
            break
        elif voto == "quinta-feira":
            quinta_feira += 1
            break
        elif voto == "sexta-feira":
            sexta_feira += 1
            break
        else:
            print("Voto inválido, tente novamente")

if segunda_feira > terça_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
     print(f"O dia escolhido pelos colaboradores é: segunda-feira com {segunda_feira} votos.")
elif terça_feira > segunda_feira and terça_feira > quarta_feira and terça_feira > quinta_feira and terça_feira > sexta_feira:
     print(f"O dia escolhido pelos colaboradores é: terça-feira com {terça_feira} votos.")
elif quarta_feira > segunda_feira and quarta_feira > terça_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira:
     print(f"O dia escolhido pelos colaboradores é: quarta-feira com {quarta_feira} votos.")
elif quinta_feira > segunda_feira and quinta_feira > terça_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira:
     print(f"O dia escolhido pelos colaboradores é: quinta feira com {quinta_feira} votos.")
elif sexta_feira > segunda_feira and sexta_feira > terça_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira:
     print(f"O dia escolhido pelos colaboradores é: sexta-feira com {sexta_feira} votos.")
else:
    print("Houve empate, importante q seja feita uma nova votação.")



