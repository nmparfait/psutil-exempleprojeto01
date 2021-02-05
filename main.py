import psutil 
import platform
import pygame
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

#conhecendo o disco 

disco = psutil.disk_usage('.')

print("Total:", disco.total, "B")
print("Em uso:", disco.used, "B")
print("Livre:", disco.free, "B")

print("Total:", round(disco.total/(1024*1024*1024),2),"GB" )
print("Em uso:", round(disco.used/(1024*1024*1024),2),"GB")
print("Livre:", round(disco.free/(1024*1024*1024),2),"GB")

print("Percentual de disco usado: ", disco.percent)

#Capturando informações básicas da rede. 

dic_interfaces = psutil.net_if_addrs()
print(dic_interfaces)


#Usando o modulo PyGames

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode(largura_tela, altura_tela)

pygame.display.set_caption("Uso de memória")
pygame.display.init()

#criar relogio

clock = pygame.time.Clock()

terminou = False
while not terminou:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      terminou = True
  
  pygame.display.update()

  #60 frames por segundo
  clock.tick(60)

#finaliza a janela
pygame.display.quit()


