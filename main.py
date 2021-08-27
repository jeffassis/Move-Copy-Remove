import os
import shutil

caminho_original = r'D:\Projetos\Move-Copy-Remove\serie'
caminho_novo = r'D:\Projetos\Move-Copy-Remove\serie2'

# Criado uma excessão para tratamento do feddback do novo caminho criado
try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

# Metodo mover
def file_move(file):
    if '.txt' in file:
        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso')

# Metodo copiar
def file_copy(file):
    if '.txt' in file:
        shutil.copy(old_file_path, new_file_path)
        print(f'Arquivo {file} copiado com sucesso')

# Metodo remover
def file_remove(file):
    if '.txt' in file:
        os.remove(new_file_path)

# Obs: Somente a chamada do metodo remover que deve 
# trocar o caminho original pelo caminho novo
for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        # Aqui chamamos o metodo que devemos utilizar
        file_move(file)
