def fibonacci(n):
    """
    Função que calcula a sequência de Fibonacci até o n-ésimo termo.
    """
    fib = [0, 1]  # Inicia a lista com os dois primeiros termos
    while fib[-1] < n:  # Continua adicionando termos até ultrapassar o número informado
        fib.append(fib[-1] + fib[-2])
    return fib

# Solicita ao usuário que informe um número
num = int(input("Informe um número inteiro: "))

# Calcula a sequência de Fibonacci até o número informado
fibonacci_seq = fibonacci(num)

# Verifica se o número informado pertence à sequência de Fibonacci
if num in fibonacci_seq:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
