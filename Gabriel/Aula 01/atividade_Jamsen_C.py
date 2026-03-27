while True:
  try:
    num1 = float(input("\ndigite o primeiro número: "))
    num2 = float(input("\ndigite o segundo número: "))
    break
  except ValueError:
    print ("\ndigite apenas números: ")

operacao = input("\nEscolha uma operação: +, -, *, /):")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
      if num2 == 0:
        resultado = "\nerro: divisão por zero"
      else:
        resultado = num1 / num2
else:
  resultado = "\noperação inválida"
print (resultado)
  