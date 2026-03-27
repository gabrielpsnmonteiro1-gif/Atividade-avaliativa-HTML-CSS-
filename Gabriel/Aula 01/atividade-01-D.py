Nome_de_usuário = "Gabriel"
Senha = 1234

log_Nome= str(input("\ndigite seu Nome:"))
log_senha = int(input("\ndigite sua senha:"))

if log_Nome == Nome_de_usuário and log_senha == Senha:
  print("Usuário encontrado")
else:
  print ("Usuário Não encontrado")
  