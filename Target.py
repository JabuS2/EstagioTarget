"""1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);



Ao final do processamento, qual será o valor da variável SOMA?

"""
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

""" O Valor da variavel SOMA é de 91 !"""



"""======================================================================="""



"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""

def pertence_fibonacci(n):
    a, b = 0, 1
    if n == a or n == b:
        return True
    while b < n:
        a, b = b, a + b
        if b == n:
            return True
    return False

num = int(input("Informe um número: "))

if pertence_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

"""Utilizei if/else para definir as opções que o programa poderia mostrar, tambem utilizei DEF para definir uma função"""



"""===================================================================="""



"""3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, 9

b) 2, 4, 8, 16, 32, 64, 128

c) 0, 1, 4, 9, 16, 25, 36, 49

d) 4, 16, 36, 64, 81

e) 1, 1, 2, 3, 5, 8, 13

f) 2,10, 12, 16, 17, 18, 19, 20?

"""



"""=================================================================="""



"""4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

RESPOSTA: O problema descrito deu a entender que cada lampada esta em uma sala, se for isso, não teriamos uma resposta,agora se as lampadas estiverem na mesma sala,entrei na linha de raciocinio que, eu precisaria ir atrás de algum "rastro" de  luz acessa, como a luz não deixa tantos rastro, imaginei que a emissão de calor faria com que eu conseguisse sabe qual lampanda foi acesa. Então eu deixaria uma lampada ligada por um tempo, apagaria, depois ligaria outra lampada.
Na sala das lampadas a lampada acesa seria o interruptor que eu deixei ligado, o interruptor que eu apaguei seria a lampada quente, e o frio, o interruptor que restou

"""



"""================================================================"""



"""5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

"""

def inverter_string(s):
    string_invertida = ''  
    for i in range(len(s) - 1, -1, -1):  
        string_invertida += s[i]  
    return string_invertida


texto = "Exemplo de inversão de string"
texto_invertido = inverter_string(texto)
print(f"String original: {texto}")
print(f"String invertida: {texto_invertido}")
