def dni(numero):
  resultado=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
  return (resultado[numero%23])
print("Este programa calcula la letra del DNI.")
numero=int(input("Introduce tu número de DNI: "))
print("Tu letra de DNI es la {}.".format(dni(numero)))