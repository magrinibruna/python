#Listas
print("Listas")
lista = [1, 2, 3, 4, 5] #delimitada por colchetes
print(lista)
print(type(lista))
print("Itens da lista: ", lista[0])
print("Somando itens da lista: ", lista[0]+lista[1])

listaCaracteres = ["A", "B", "C", "D"]
print("Concatenando itens da lista:", listaCaracteres[0] + listaCaracteres[1])

listaMista = ["Loueny", 42, [1, 6, 2018]]
print("Lista mista:", listaMista)
print("Lista dentro de lista(matriz):", listaMista[2][1])

#Tem como parametro um objeto interável para que ele seja transformado em lista
listaV2 = list("Loueny")
print(listaV2)
listaV3 = list((1,2,3,4))
print(listaV3)
listaV4 = list(("Loueny",))
print(listaV4)

#Métodos que todos os tipos de lista possuem
print("Tamanho da lista:", len(listaMista)) #Retorna quantos elementos uma lista possui
#Como a indexação de lista começa no 0 e na contagem, o 0 não é utilizado, para acessar o
#útlimo valor de uma lista pode-se usar
print("Ultimo valor da lista:", lista[len(lista)-1])
#Outra abordagem é que o Python utiliza a contagem negativa para ter o inverso da lista, ou seja
# Positiva | Negativa | Valor
#    0         -3       Bruna
#    1         -2       Loueny
#    2         -1       Stefany
#é a mesma coisa que lista = ["Bruna", "Loueny", "Stefany"]
print("Ultimo valor da lista:",lista[-1])
print("------------------")
#Tuplas
print("Tuplas")
a = (5) #É numérico ou uma tupla? Para o python saber que é uma tupla, coloca-se uma virgula (,) no final
b = (5,) #Neste caso, é uma tupla, não um valor numérico
print(type(a))
print(type(b))
