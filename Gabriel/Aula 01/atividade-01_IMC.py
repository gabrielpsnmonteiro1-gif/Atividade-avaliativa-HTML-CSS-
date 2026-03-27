Nome = str(input("\ndigite seu nome: "))
Idade = int(input("\ndigite sua idade: "))
Peso = float(input("\ndigite seu peso: "))
Altura = float(input("\ndigite sua altura: "))

imc = Peso/(Altura**2)

if imc < 18.5:
  classificação = "abaixo do peso"
elif 18.5 <= imc < 25:
  classificação = "peso comum"
elif 25 <= imc < 30:
  classificação = "acima do peso"
elif 30 <= imc < 35:
  classificação = "obesidade grau 1"
elif 35 <= imc < 40:
  classificação = "obesidade grau 2"
else:
  classificação = "obesidade grau 3"

  print("\n======Resultado======")
  print("Nome", Nome)
  print("Idade", Idade)
  print("Peso", Peso)
  print("Altura", Altura)