
#num = float (input ("Digite um número: "))

#if (num >= 0):
    #print ("Número positivo.")
#else:
    #print ("Número negativo.")
#------------------------------------------------

#n1 = float (input("Digite sua primeira nota: "))
#n2 = float (input("Digite sua segunda nota: "))
#n3 = float (input("Digite sua terceira nota: "))

#media = ((n1 + n2 + n3)/3)

#if (media >= 5):
   # print ("Sua média é: ",media, "Parabéns, voçe está aprovado!")
#else:
   # print ("Sua média é: ",media, "Sinto muito, nao foi dessa vez.")


#num1 = int (input("Digite um número: "))

#while (num1 != 0):
 #   print (num1)
  #  num1 = int (input("Digite um número: "))
#print ("Programa encerrado.")


#senha = input ("Digite a senha: ")


#while (senha != "naodigo"):
   # print ("Digite senha correta: ")
    #senha = input ("Digite a senha: ")
#print ("Seja bem vindo.")
#_______________________________________________________________________________
#n = float (input("Digite um número: "))
#c = 0

#while (n !=0):
 #   if (n == 2):
   #     c = c+1
   # n = float (input("Digite um número: "))
#print ("Voce digitou ", c ,"x")

#___________________________________________________________________

   
#idades = []
#maior = 0

#for i in range (3):
  #  idade = int(input("Digite sua idade: "))
 #   idades.append(idade)


#print (maior)

#___________________________________________________________________

#sexos = []

#fem = 0
#mas = 0

#for i in range (3):
 #    sexos.append(input("Digite seu sexo (M ou F): "))


 
#for sexo in sexos:
 #   if sexo == "M":
  #      mas = mas +1
   # elif sexo == "F":
    #    fem = fem +1
    #else:
     #   print ("Sexo invalido!")

#print ("Quantidade de homens:", mas, "\nQuantidade de mulheres:", fem)
#___________________________________________________________________


                    #!!!!!!!!
#notas = []

#otimo = 0
#bom = 0
#regular = 0

#for i in range (5):
 #   notas.append(int(input("Digite sua nota (1 - REGULAR; 2 - BOM; 3 - OTIMO): ")))
    
#for nota in notas:
 #   if nota == 1:
     #   regular = regular +1
    #elif nota == 2:
     #   bom = bom +1
    #elif nota == 3:
   #     otimo = otimo +1
  #  else:
 #       print ("Nota digitada inválda!")

#print (otimo,"notas Otimas. \n", bom ,"notas Boas. \n",regular,"notas Regular.")

#___________________________________________________________________


                   #!!!!!!!!
#positivos = []
#negativos = []

#soma = 0

#for i in range (4):
 #   num = float(input("Digite um número: "))
  #  if num >= 0:
   #     positivos.append(num)
    #elif num < 0:
     #   negativos.append(num)

#for num in positivos:
 #   soma = soma+num
    
        
#print("Números negativos: ", negativos)
#print("Soma dos números positivos: ", soma)
    

#_______________________________________________________________________________

#numeros = []
#maior = 0

#for linha in range (2):
 #   linhaAtual = []
  #  for coluna in range (2):
   #     linhaAtual.append(int(input("Digite um número; ")))
    #    if linhaAtual[coluna] > maior:
     #       maior = linhaAtual[coluna]
    #numeros.append(linhaAtual)

#print (numeros)        
#print ("O maior número digitado foi: ",maior)

#_______________________________________________________________________________

#alturas = []

#maior = 0

#for linha in range (2):
 #   novaLinha = []
  #  for coluna in range(2):
   #     novaLinha.append(float(input("Digite sua altura: ")))
    #    if novaLinha[coluna] >= 1.50:
     #       maior = maior+1
    #alturas.append(novaLinha)
#print (alturas)
#print ("As alturas maiores que 1.50 são: ", maior)

      
#______________________________________________________________________________

print ("Questáo 01 - PROVA.\n")
print("Faça um programa que lê 6 números reais em uma matriz 3x2, calcula e exiba:\n")
print("A média dos números positivos;")
print("A soma dos números negativos;")
print("O maior número positivo;")
print("O maior número positivo da 2ª linha.\n")

numeros = []

numerosPositivos = []
somaPosi = 0
media = 0
maiorPositivo = 0
maiorMaior = 0

numerosNegativos = []
somaNega = 0

for linha in range (3):
    novaLinha = []
    for coluna in range (2):
        num = float(input("Digite um número: "))
        novaLinha.append(num)
        if num >= 0:
            numerosPositivos.append(num)
        if num < 0:
            numerosNegativos.append(num)
        
    numeros.append(novaLinha)
print ("\nA matriz é: ",numeros,"\n")

for num in numerosPositivos:
    somaPosi = somaPosi + num
    media = somaPosi/len(numerosPositivos)
    if num > maiorPositivo:
        maiorPositivo = num
print ("Os números positivos são: ",numerosPositivos, "\nA média dos números positivos é: ", media)


for num in numerosNegativos:
    somaNega = somaNega + num
print ("Os números negativos são: ",numerosNegativos, "\nA soma dos numéros negativos é: ", somaNega)
print ("O maior número positivo é: ", maiorPositivo)

x = numeros[1][0]
y = numeros[1][1]

if x < 0 and y < 0:
    print ("Não existe nenhum número positivo na segunda linha.")
elif x > y:
    print("O maior número positivo da segunda linha é: ",x)
elif y > x:
    print("O maior número positivo da segunda linha é: ",y)

#_____________________________________________________________________________

print("Questão 02 - PROVA.\n")
print("Faça um programa que receba o preço de cinco produtos em uma lista, calcula e exiba:\n")
print("A quantidade de produtos com preço inferior a R$ 50,00;")
print("A quantidade de produtos com preço entre R$ 50,00 e 80,00;")
print("A média de preço;")
print("O preço mais baixo.\n")

precos = []
precosInf = []
inferior = 0
precosEntre = []
entre = 0
menor = 50

soma = 0
media = 0

for i in range (5):
    preco = float(input("Digite o preço do produto: R$ "))
    precos.append(preco)
    if preco < 50:
        precosInf.append(preco)
        inferior = inferior + 1
    if preco >= 50 and preco <= 80:
        precosEntre.append(preco)
        entre = entre + 1
   
for num in precos:
    soma = soma + num
    media = soma/5

for num in precosInf:
    if num < menor:
        menor = num
        
print ("Os preços cadastrados foram: \n",precos)
print ("A quantidade de produtos com preço inferior a R$ 50,00 é: ",inferior, "\ne são: ",precosInf)
print ("A quantidade de produtos com preço entre R$ 50,00 e R$ 80,00 é: ",entre, "\ne são: ",precosEntre)
print ("A média de preços recebidos é: ",media)
print ("O menor preço digitado foi: ", menor)

#_____________________________________________________________________________

print("Questão 03 - PROVA.\n")
print("Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação.\n")

print ("|----------------------------------|")
print ("| TABELA 1 - PERCENTUAL DE AUMENTO |")
print ("| PEÇO                          %  |")
print ("| Até R$ 50,00                  5  |")
print ("| Entre R$ 50,00 e R$ 100,00   10  |")
print ("| Acima de R$ 100,00           15  |")
print ("|__________________________________|")
print ("|--------------------------------------------------------|")
print ("|          TABELA 2 - CLASSIFICAÇÃO                      |")
print ("| NOVO PEÇO                               CLASSIFICAÇÃO  |")
print ("| Até R$ 80,00                                Barato     |")
print ("| Entre R$ 80,00 e R$ 120,00 (inclusive)      Normal     |")
print ("| Entre R$ 120,00 e R$ 200,00(inclusive)      Caro       |")
print ("| Maior que R$ 200,00                         Muito caro |")
print ("|________________________________________________________|")

preco = float(input("DIgite o valor do produto: R$ "))
percentual = 0

if preco < 50:
    percentual = (preco * 1.05)
    print("\nO percentual de aumento foi de 5% e o valor final é: ", percentual)
    if percentual < 80:
        print ("Classificação: Barato.")
elif preco >= 50 and preco <= 100:
    percentual = (preco * 1.10)
    print("\nO percentual de aumento foi de 10% e o valor final é: ", percentual)
    if percentual < 80:
        print ("Classificação: Barato.")
    elif percentual >= 80 and percentual <= 120:
        print ("Classificação: Normal.")
elif preco > 100:
    percentual = (preco * 1.15)
    print("\nO percentual de aumento foi de 15% e o valor final é: ", percentual)
    if percentual >= 80 and percentual <= 120:
        print ("Classificação: Normal.")
    elif percentual > 120 and percentual <= 200:
        print ("Classificação: Caro.")
    elif percentual > 200:
        print ("Classificação: Muito caro.")
        
#_____________________________________________________________________________
#n = 0


#while (n <=100):
  #  print (n)
   # n=n+1
#_______________________________________________________________________________

#ida = int (input ("Digite sua idade: "))
#a =0
#b =0

#while (ida >= 0):
 #   if (ida <=15):
 #       a = a+1
 #   elif (ida >15):
 #      b = b+1
  #  ida = int (input ("Digite sua idade: "))
#print (" As pessoas com idade menor ou igual a 15 foram:" ,a,"\n As pessoas com idade superior a 15 anos foram:", b)

#_______________________________________________________________________________

#s = 0
#n = 0

#for c in range (15):
    #pergunta = int(input("Voce gosta de beterraba? digite (1), se nao (2)."))
    #if pergunta == 1:
        #s = s+1
    #elif pergunta == 2:
        #n = n+1
#print ("A quantidade de pessoas que gostam de beterraba sao: ",s,
       #"A quantidade de pessoas que nao gostam sao: ", n)

#_______________________________________________________________________________

#maior = 0
#produto = float(input("Digite o valor do produto."))
#maior = produto
#for c in range (1,11):
 #   produto1 = float(input("Digite o valor do produto."))
  #  if (produto1 > maior):
   #     maior = produto1
#print ("O maior produto cadastrado foi: ", maior)
    
#_______________________________________________________________________________    
    
#b = 0
#o = 0
#r = 0

#for c in range (5):
 #   print ("Seja bem vindo ao Cine Unipe! Sua avaliaçao é muito importante para nós. Digite (1) para regular, (2) para bom e (3) (1) para ótimo.")
  #  n = int(input ())
   # if n == 1:
    #    r = r+1
    #if n == 2:
     #   b = b+1
    #if n == 3:
     #   o = o+1
#print(o,"pessoas acharam o filme ótimo,",b, "pessoas acharam bom e ",r,"pessoas acharam regular.")


#_______________________________________________________________________________













#num1 = float (input("Digite um número: "))
#operacao = str (input("Digite a operacao desejada: "))
#num2 = float (input("Digite um número: "))



#if (operacao == "+"):
 #   print ("O resutado é: ", (num1+num2))
#if (operacao == "-"):
 #   print ("O resutado é: ", (num1-num2))
#if (operacao == "*"):
 #   print ("O resutado é: ", (num1*num2))
#if (operacao == "/"):
 #print ("O resutado é: ", (num1/num2))


#n1= int (input("Digite o número 1: "))
#n2= int (input("Digite o número 2: "))
#n3= int (input("Digite o número 3: "))

#if (n1 > n2 and n1 >n3):
 #   print ("O primeiro número é maior.", n1)
#if (n2 > n1 and n2 >n3):
#    print ("O segundo número é maior.", n2)
#if (n3 > n1 and n3 >n2):
 #   print ("O terceiro número é maior.", n3)
 
#estado = str (input("Digite seu estado com letra maiúscula: "))


#if (estado == "PE" or estado == "PB"):
 #   print ("Sua regiao é nordeste.")
#if (estado == "SP" or estado == "RJ"):
 #   print ("Sua regiao é sudeste.")

#idade = int(input("Digite sua idade: "))

#if (idade >= 5 and idade <= 10):
 #   print ("Sua categoria é: Infanto juvenil.")
#if (idade >= 11 and idade <= 15):
 #   print ("Sua categoria é: Juvenil.")
#if (idade >= 16 and idade <= 20):
 #   print ("Sua categoria é: Junior.")
#if (idade >= 21 and idade <= 25):
 #   print ("Sua categoria é: Profissinal.")
#if (idade > 25):
 #   print ("Sua categria nao está definida.")

#op = int(input("Digite o código do produto: "))

#if (op == 1):
 #   print ("Pizza!")
#elif (op == 2):
 #   print ("Hamburguer")
#elif (op == 3):
 #   print ("Refri")
#else:
 #   print ("Nenhuma opçao é válida.")


#salario = float (input("Digite seu salario: "))


#if (salario < 300):
  #  print ("Seu salário novo é: ", (salario * 1.45))
#elif (salario >= 300 and salario <= 600):
   # print ("Seu salário novo é: ", (salario * 1.25))
#else:
   # print ("Seu salário novo é: ", (salario * 1.15))

















#preco = 3.50
#print ("O produto custa: ",preco)
#quant = int (input ("Digite a quantidade do produto: "))


#print ("O valor total da compra é: ", preco * quant)


#------------------------------------------------

#anoAt = int (input ("Digite o ano atual: "))
#anoNas = int (input ("Digite o ano do seu nascimento: "))

#print ("Sua idade é: ", anoAt - anoNas)
#print ("Sua idade em 2025 será: ", 2025 - anoNas)



#------------------------------------------------

#idade = int (input ("Digite sua idade: "))


#if (idade >= 18):
    #print ("Voçê está apto a dirigir.")

#else:
        #print ("Voçê ainda nao pode dirigir.")


#------------------------------------------------
