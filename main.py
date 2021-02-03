import psutil 
import platform
import time

# imprimindo a memoria total
mem = psutil.virtual_memory()
print("A memoria principal é: ", mem.total)
print("A memoria disponível é: ", mem.available)
capacidade = round(mem.total/(1024*1024*1024), 2)
print("A memoria principal em giga:", capacidade, "GB" )

#Informação do Processador 

#conhecer o nome da plataforma
#conhecer o nome do processador
print(platform.processor())

#nome do computador na rede
print(platform.node())

#Mais detalhes da plataforma
print(platform.platform())

#Informações do sistema operational
print(platform.system())

#percentual do processador
processa = psutil.cpu_percent()
print("processador em psutil é:", processa)

for i in range(0, 10):
  print(psutil.cpu_percent())
  time.sleep(1)

