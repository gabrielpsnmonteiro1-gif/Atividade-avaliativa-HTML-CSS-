
xp = 1
start = True
while start:
  match xp:
    case 1:
      try:
         nome = str(input("digite seu nome:"))
         xp += 1
      except:
        print("valor inválido")
    case 2:
      try:
        idade = int(input("digite sua idade:"))
        xp += 1
      except:
        print ("inválido")
    case 3:
      try:
        peso = float(input("digite seu peso:").replace(",","."))
        start = False
      except:
        print ("inválido")
else:
  print ("Seu nome é", nome, "voçê tem", idade,"anos e pesa", peso, "kgs")