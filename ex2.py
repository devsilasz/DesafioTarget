def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return f"Sim, {numero} pertence à sequência de Fibonacci."
    else:
        return f"Não, {numero} não pertence à sequencia de Fibonacci."

numero = int(input("Agora digite um número para verificar se pertence à sequencia de Fibonacci: "))

result = verifica_fibonacci(numero)

print(result)