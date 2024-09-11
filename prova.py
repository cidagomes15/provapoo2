1
numero = int(input("Digite um número: "))


if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


2

print("Escolha a conversão desejada:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")


escolha = input("Digite 1 ou 2: ")

if escolha == '1':
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
elif escolha == '2':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
else:
    print("Escolha inválida. Por favor, digite 1 ou 2.")


3

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3) / 3


print("media:",media)

4

n = int(input("Digite um número inteiro positivo: "))


if n < 0:
    print("O fatorial não está definido para números negativos.")
elif n == 0:
    print("O fatorial de 0 é 1.")
else:

    fatorial = 1

    for i in range(1, n + 1):
        fatorial *= i

    print(f"O fatorial de {n} é {fatorial}.")


5


def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    try:
        n = int(input("Digite o número de termos da sequência de Fibonacci que você deseja gerar: "))
        if n <= 0:
            raise ValueError("O número de termos deve ser um inteiro positivo.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return
    result = fibonacci(n)
    print("Sequência de Fibonacci:")
    print(result)

if __name__ == "__main__":
    main()


6


import cmath
def calcular_raizes_quadratica(a, b, c):
    delta = b**2 - 4*a*c
    raiz1 = (-b + cmath.sqrt(delta)) / (2*a)
    raiz2 = (-b - cmath.sqrt(delta)) / (2*a)
    return (raiz1, raiz2)

def main():
    try:
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        if a == 0:
            raise ValueError("O coeficiente 'a' não pode ser zero.")
    except ValueError as e:
        print(f"Erro: {e}")
        return

    raizes = calcular_raizes_quadratica(a, b, c)

    if raizes[0].imag == 0 and raizes[1].imag == 0:
        print(f"As raízes reais são: {raizes[0].real} e {raizes[1].real}")
    else:
        print(f"As raízes são: {raizes[0]} e {raizes[1]}")

if __name__ == "__main__":
    main()


7


nome = "cida"
idade = 19

print(f"Nome: {nome}, Tipo de dado: {type(nome)}")
print(f"Idade: {idade}, Tipo de dado: {type(idade)}")


8


numero1 = 10
numero2 = 5


if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}.")
else:
    print(f"{numero1} não é maior que {numero2}.")



9

nome = input("Digite seu nome: ")


try:
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Por favor, insira uma idade válida.")
else:
    print(f"Olá, {nome}, você tem {idade} anos!")

10


try:
    numero = float(input("Digite um número: "))


    if numero > 0:
        print(f"O número {numero} é positivo.")
    elif numero < 0:
        print(f"O número {numero} é negativo.")
    else:
        print(f"O número {numero} é zero.")

except ValueError:
    print("Por favor, insira um número válido.")


11

variavel1 = True
variavel2 = False

if variavel1 and variavel2:
    print("Ambas as variáveis são verdadeiras.")
else:
    print("Ambas as variáveis não são verdadeiras.")


12


for i in range(1, 11):
    print(i)


13

frutas = ["maçã", "banana", "laranja", "uva", "manga"]
print(frutas[2])


14

def somar_dois_numeros(numero1, numero2):
    return numero1 + numero2

numero1 = 5
numero2 = 7
resultado = somar_dois_numeros(numero1, numero2)


print("A soma de", numero1, "e", numero2, "é", resultado)

15


idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você está apto a votar e dirigir.")
elif idade >= 16:
    print("Você está apto a votar, mas não dirigir.")
else:
    print("Você não está apto a votar nem a dirigir.")

16


resposta = input("Você gosta de estudar programação? (responda 'sim' ou 'não'): ").strip().lower()

if resposta == "sim":
    print("Que bom!")
elif resposta == "não":
    print("Que pena!")
else:
    print("Resposta inválida. Por favor, responda 'sim' ou 'não'.")


17


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

opcao = input("Escolha a operação (1: soma, 2: subtração, 3: multiplicação, 4: divisão): ")

if opcao == "1":
    print(f"A soma de {numero1} e {numero2} é {numero1 + numero2}")
elif opcao == "2":
    print(f"A subtração de {numero1} e {numero2} é {numero1 - numero2}")
elif opcao == "3":
    print(f"A multiplicação de {numero1} e {numero2} é {numero1 * numero2}")
elif opcao == "4":
    if numero2 != 0:
        print(f"A divisão de {numero1} por {numero2} é {numero1 / numero2}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Opção inválida. Escolha 1, 2, 3 ou 4.")

18



nota = float(input("Digite uma nota de 0 a 10: "))

if nota >= 7:
    print("Aprovado")
elif 5 <= nota < 7:
    print("Recuperação")
elif nota < 5:
    print("Reprovado")
else:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")


19


#QUESTÃO_19
soma = 0
numero = 0

while numero >= 0:
    numero = float(input("Digite um número (negativo para encerrar): "))
    if numero >= 0:
        soma += numero

# Exibe a soma dos números digitados
print("A soma dos números digitados é:", soma)





#QUESTÃO_20
frase = "Olá, mundo! Este é um exemplo de frase."


numero_de_caracteres = len(frase)
print("A frase possui", numero_de_caracteres, "caracteres.")





#QUETÃO_21
numeros = [10, 15, 22, 33, 44, 55, 66]


for numero in numeros:
    if numero % 2 == 0:
        print(numero)




#QUESTÃO_22
def calcular_media(numeros):
    if len(numeros) == 0:
        return "Array vazio. Não é possível calcular a média."

    soma = sum(numeros)


    media = soma / len(numeros)

    return media

array_numeros = [7, 22, 40, 5, 15]
resultado = calcular_media(array_numeros)
print("A média dos números é:", resultado)




#QUESTÃO_23
booleano1 = False
booleano2 = True
booleano3 = False


se_alguma_verdadeira = booleano1 or booleano2 or booleano3

if se_alguma_verdadeira:
    print("Pelo menos uma das variáveis é verdadeira.")
else:
    print("Nenhuma das variáveis é verdadeira.")





#QUESTÃO_24
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


print(verificar_par_ou_impar(10))
print(verificar_par_ou_impar(7))





#QUESTÃO_25
def imprimir_tabela_multiplicacao():
    print("Tabela de Multiplicação (1 a 10)")
    print("-" * 30)

    print("     ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print()

    print("    " + "-" * 40)


    for i in range(1, 11):
        print(f"{i:2} |", end="")
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()
imprimir_tabela_multiplicacao()




#QUESTÃO_26
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]


valor = matriz[1][2]


print(f"O valor na posição [1][2] é: {valor}")





#QUESTÃO_27
a = 10
b = 5
c = 3
d = 8


if a > b and c < d:
    print("O primeiro número é maior que o segundo e o terceiro número é menor que o quarto.")
else:
    print("Pelo menos uma das condições não é satisfeita.")





#QUESTÃO_28
numeros = []
for i in range(5):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

print("Números em ordem inversa:")
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])






#QUESTÃO_29
pares = []
impares = []

for i in range(15):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número: "))
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


contagem_pares = len(pares)
contagem_impares = len(impares)

print(f"Quantidade de números pares: {contagem_pares}")
print(f"Quantidade de números ímpares: {contagem_impares}")




#QUESTÃO_30
def tamanho_maior_string(strings):
    if not strings:
        return 0

    maior_string = max(strings, key=len)
    return len(maior_string)


strings = ["apple", "banana", "cherry", "date"]
print(f"O tamanho da maior string é: {tamanho_maior_string(strings)}")

#34
def verificar_pelo_menos_um_par(*numeros):
    """
    Verifica se pelo menos um número na lista é par.
    """
    for numero in numeros:
        if numero % 2 == 0:
            return True
    return False

# Exemplo de uso
resultado = verificar_pelo_menos_um_par(1, 3, 4)
print(f"Pelo menos um número é par: {resultado}")  # Saída esperada: True


#35
def fibonacci(n):
    """
    Função recursiva para calcular o n-ésimo número da sequência de Fibonacci.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 10
print(f"O {n}-ésimo número da sequência de Fibonacci é: {fibonacci(n)}") 
#36
def segundo_maior(array):
    """
    Função que recebe um array de números inteiros e retorna o segundo maior número.
    """
    if len(array) < 2:
        return None  

    primeiro_maior = segundo_maior = float('-inf')

    for num in array:
        if num > primeiro_maior:
            segundo_maior = primeiro_maior
            primeiro_maior = num
        elif primeiro_maior > num > segundo_maior:
            segundo_maior = num

    if segundo_maior == float('-inf'):
        return None  
    return segundo_maior

# Exemplo de uso
array = [10, 5, 20, 20, 15]
print(f"O segundo maior número é: {segundo_maior(array)}")
#37
def soma_matrizes(matriz1, matriz2):
    """
    Função que soma duas matrizes 3x3.
    """
    matriz_resultante = []
    for i in range(len(matriz1)):
        linha_resultante = []
        for j in range(len(matriz1[i])):
            linha_resultante.append(matriz1[i][j] + matriz2[i][j])
        matriz_resultante.append(linha_resultante)
    return matriz_resultante

# Declaração das duas matrizes 3x3
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Calculando a soma das duas matrizes
matriz_soma = soma_matrizes(matriz1, matriz2)

# Exibindo a matriz resultante da soma
print("Matriz 1:")
for linha in matriz1:
    print(linha)

print("\nMatriz 2:")
for linha in matriz2:
    print(linha)

print("\nMatriz Soma:")
for linha in matriz_soma:
    print(linha)

#38
def exibir_triangulo(n):
    """
    Função que exibe um triângulo de números com n linhas.
    """
    for i in range(1, n + 1):
        # Para cada linha i, imprime números de 1 até i
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Para pular para a próxima linha

# Solicitando o número de linhas ao usuário
n = int(input("Digite o número de linhas para o triângulo: "))

# Exibindo o triângulo de números
exibir_triangulo(n) 

#39
def exibir_em_ordem_crescente():
    """
    Função que solicita três números ao usuário e os exibe em ordem crescente.
    """
    # Solicita três números ao usuário
    numeros = []
    for i in range(1, 4):
        num = float(input(f"Digite o número {i}: "))
        numeros.append(num)
    
    # Ordena a lista de números
    numeros.sort()
    
    # Exibe os números em ordem crescente
    print("Números em ordem crescente:")
    for numero in numeros:
        print(numero)

# Chama a função para executar o programa
exibir_em_ordem_crescente()

#40
def verificar_condicoes(a, b, c, d, e):
    """
    Função que verifica as seguintes condições:
    1. Se o primeiro número (a) é maior que o segundo número (b).
    2. Se o terceiro número (c) é diferente do quarto número (d) e menor que o quinto número (e).
    """
    # Verifica se o primeiro número é maior que o segundo
    condicao1 = a > b
    
    # Verifica se o terceiro número é diferente do quarto e menor que o quinto
    condicao2 = (c != d) and (c < e)
    
    # Exibe os resultados das verificações
    print(f"O primeiro número ({a}) é maior que o segundo ({b})? {'Sim' if condicao1 else 'Não'}")
    print(f"O terceiro número ({c}) é diferente do quarto ({d}) e menor que o quinto ({e})? {'Sim' if condicao2 else 'Não'}")

# Declaração das cinco variáveis
numero1 = 10
numero2 = 5
numero3 = 7
numero4 = 8
numero5 = 12

# Chama a função para verificar as condições
verificar_condicoes(numero1, numero2, numero3, numero4, numero5) 

#41
def contar_multiplos_de_2_e_5(array):
    """
    Função que conta quantos números no array são múltiplos de 2 e de 5 ao mesmo tempo.
    """
    contador = 0
    
    for numero in array:
        if numero % 2 == 0 and numero % 5 == 0:
            contador += 1
    
    return contador

# Declaração do array com 10 elementos
array = [10, 20, 30, 15, 25, 40, 50, 55, 60, 70]

# Contando quantos números são múltiplos de 2 e de 5
resultado = contar_multiplos_de_2_e_5(array)

# Exibindo o resultado
print(f"Quantidade de números que são múltiplos de 2 e de 5: {resultado}") 

#42
def e_palindromo(palavra):
    """
    Função recursiva que verifica se uma palavra é um palíndromo.
    """
    # Remove espaços e converte para minúsculas para uma verificação mais robusta
    palavra = palavra.replace(" ", "").lower()
    
    # Caso base: Se a palavra tem 0 ou 1 caractere, é um palíndromo
    if len(palavra) <= 1:
        return True
    
    # Verifica se o primeiro e o último caractere são iguais
    if palavra[0] != palavra[-1]:
        return False
    
    # Chama a função recursivamente para a substring sem o primeiro e o último caractere
    return e_palindromo(palavra[1:-1])

# Exemplos de uso
palavra1 = "Radar"
palavra2 = "Hello"

print(f'"{palavra1}" é um palíndromo? {"Sim" if e_palindromo(palavra1) else "Não"}')
print(f'"{palavra2}" é um palíndromo? {"Sim" if e_palindromo(palavra2) else "Não"}')

#43
def maior_valor_matriz(matriz):
    """
    Função que recebe uma matriz 5x5 e retorna o maior valor presente na matriz.
    """
    maior_valor = matriz[0][0]  # Inicializa o maior valor com o primeiro elemento da matriz

    for linha in matriz:
        for valor in linha:
            if valor > maior_valor:
                maior_valor = valor

    return maior_valor

# Declaração de uma matriz 5x5 com números inteiros
matriz_5x5 = [
    [3, 5, 7, 2, 4],
    [8, 1, 6, 9, 3],
    [4, 2, 11, 5, 7],
    [1, 8, 13, 0, 6],
    [9, 4, 2, 5, 10]
]

# Encontrando o maior valor na matriz
resultado = maior_valor_matriz(matriz_5x5)

# Exibindo o maior valor
print(f"O maior valor da matriz é: {resultado}") 

#44
def soma_linhas_matriz(matriz):
    """
    Função que percorre uma matriz 4x4 e exibe a soma dos elementos de cada linha.
    """
    for i, linha in enumerate(matriz):
        soma = sum(linha)
        print(f"Soma dos elementos da linha {i + 1}: {soma}")

# Declaração da matriz 4x4 com números inteiros
matriz_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Chamando a função para exibir a soma dos elementos de cada linha
soma_linhas_matriz(matriz_4x4) 


#45
def soma_linhas(matriz):
    """
    Função que recebe uma matriz e retorna um array com a soma de cada linha.
    """
    # Inicializa uma lista para armazenar as somas das linhas
    somas = []
    
    # Percorre cada linha da matriz
    for linha in matriz:
        # Calcula a soma dos elementos da linha e adiciona à lista de somas
        soma = sum(linha)
        somas.append(soma)
    
    return somas

# Exemplo de uso da função
matriz_exemplo = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Obtém o array com a soma de cada linha
resultado = soma_linhas(matriz_exemplo)

# Exibe o resultado
print("Somas de cada linha:", resultado)

#46
def remover_negativos(array):
    """
    Função que remove todos os números negativos de um array.
    """
    # Cria um novo array contendo apenas números não negativos
    array_filtrado = [num for num in array if num >= 0]
    return array_filtrado

def main():
    """
    Função principal do programa.
    """
    # Solicita ao usuário para inserir 10 números
    numeros = []
    print("Digite 10 números:")
    for i in range(10):
        while True:
            try:
                num = float(input(f"Número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    
    # Remove os números negativos do array
    numeros_sem_negativos = remover_negativos(numeros)
    
    # Exibe o resultado
    print("Array original:", numeros)
    print("Array sem números negativos:", numeros_sem_negativos)

# Executa a função principal
main()

#47
def verificar_ordem_crescente(vetor):
    """
    Função que verifica se um vetor está em ordem crescente.
    """
    # Percorre o vetor e verifica se cada elemento é menor ou igual ao próximo
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True

def main():
    """
    Função principal do programa.
    """
    # Solicita ao usuário para inserir o número de elementos do vetor
    while True:
        try:
            n = int(input("Digite o número de elementos do vetor: "))
            if n <= 0:
                raise ValueError("O número de elementos deve ser positivo.")
            break
        except ValueError as e:
            print(e)
            print("Por favor, insira um número inteiro válido.")

    # Solicita ao usuário para inserir os elementos do vetor
    vetor = []
    print(f"Digite os {n} elementos do vetor:")
    for i in range(n):
        while True:
            try:
                num = float(input(f"Elemento {i + 1}: "))
                vetor.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

    # Verifica se o vetor está em ordem crescente
    if verificar_ordem_crescente(vetor):
        print("O vetor está em ordem crescente.")
    else:
        print("O vetor não está em ordem crescente.")

# Executa a função principal
main()

#48
def remover_duplicados(vetor):
    """
    Função que remove todos os elementos duplicados de um vetor.
    """
    # Usa um conjunto para remover duplicados e depois converte de volta para uma lista
    return list(set(vetor))

def main():
    """
    Função principal do programa.
    """
    # Solicita ao usuário para inserir o número de elementos do vetor
    while True:
        try:
            n = int(input("Digite o número de elementos do vetor: "))
            if n <= 0:
                raise ValueError("O número de elementos deve ser positivo.")
            break
        except ValueError as e:
            print(e)
            print("Por favor, insira um número inteiro válido.")

    # Solicita ao usuário para inserir os elementos do vetor
    vetor = []
    print(f"Digite os {n} elementos do vetor:")
    for i in range(n):
        while True:
            try:
                num = float(input(f"Elemento {i + 1}: "))
                vetor.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

    # Remove os elementos duplicados do vetor
    vetor_sem_duplicados = remover_duplicados(vetor)
    
    # Exibe o resultado
    print("Vetor original:", vetor)
    print("Vetor sem duplicados:", vetor_sem_duplicados)

# Executa a função principal
main()

#49
def buscar_numero_matriz(matriz, numero):
    """
    Função que verifica se um número está presente em uma matriz m x n,
    onde cada linha e cada coluna são ordenadas em ordem crescente.
    """
    if not matriz or not matriz[0]:
        return False
    
    m = len(matriz)      # Número de linhas
    n = len(matriz[0])   # Número de colunas
    
    # Inicia no canto superior direito
    linha = 0
    coluna = n - 1
    
    while linha < m and coluna >= 0:
        valor_atual = matriz[linha][coluna]
        
        if valor_atual == numero:
            return True
        elif valor_atual < numero:
            linha += 1
        else:
            coluna -= 1
    
    return False

# Exemplo de uso da função
matriz_exemplo = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

numero_procurado = 5
resultado = buscar_numero_matriz(matriz_exemplo, numero_procurado)

print(f"O número {numero_procurado} {'está' if resultado else 'não está'} presente na matriz.")

#50
def soma_diagonais(matriz):
    """
    Função que recebe uma matriz quadrada nxn e retorna a soma dos elementos da diagonal principal
    e da diagonal secundária.
    """
    n = len(matriz)
    
    soma_diagonal_principal = 0
    soma_diagonal_secundaria = 0
    
    for i in range(n):
        soma_diagonal_principal += matriz[i][i]
        soma_diagonal_secundaria += matriz[i][n - 1 - i]
    
    return soma_diagonal_principal, soma_diagonal_secundaria

# Exemplo de uso da função
matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_diag_principal, soma_diag_secundaria = soma_diagonais(matriz_exemplo)

print(f"Soma da diagonal principal: {soma_diag_principal}")
print(f"Soma da diagonal secundária: {soma_diag_secundaria}")



