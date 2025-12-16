primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor =  input("digite o segundo valor: ")
if primeiro_valor > segundo_valor:
    print (f'O {primeiro_valor=} é maior que o segundo')
elif primeiro_valor < segundo_valor:
    print(f"O {segundo_valor=} é maior que o primeiro")
else:
    print("Os valores são iguais")