for i in range(10):
    print(i)
    if i == 5:
        break

i = 0
while(i < 10):
    print(i)
    i += 1
    if i == 5:
        break

print("-------------------------")

#não termina e execução do laço
for i in range(10):
    if i == 5:
        print("Valor escolhido")
        continue
    print(i)
