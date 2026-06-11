import os
from PIL import Image

pasta = "/storage/emulated/0/DCIM/Camera" #Diretório onde a pasta onde a imagem que se quer comprimir está
foto = "NOME DA FOTO.jpg"
caminho_original = os.path.join(pasta, foto) #Endereço de onde a foto está, seleciona a foto que se deseja comprimir
caminho_saida = os.path.join(pasta, foto + " comprimida.jpg") #Endereço de onda a foto comprimida estará salva e também adicionando a palavra comprimida no fim do nome
img = Image.open(caminho_original) #Abre e carrega a foto
img.save(caminho_saida, "JPEG", quality = 20, optimize = True) #Salva a imagem no formato JPEG, otimiza ela e ajusta o balanço de qualidade (alterea seu bel prazer, o recomendado é 75)

print("Concluído")