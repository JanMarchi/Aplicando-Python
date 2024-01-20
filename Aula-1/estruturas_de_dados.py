#estruturas_condicionais

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")

#estrutura_repeticao_while
    
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

#estrutura_repeticao_for
    
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")


#estrutura_repeticao_break
    
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
    

#estrutura_condicional_ternaria
    
saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

#estrutura_condicional_aninhada

conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")