# Execute este script da raiz do projeto.
# Ele espera um argumento que é o caminho para a pasta com os casos de teste.
# Exemplo: python3 run.py casos_de_teste/
# Salvar automaticamente na pasta "/temp/".
import sys, os

path = sys.argv[1].strip()

for file in os.listdir(path):
    if file.endswith(".txt"):
        os.system(f"python3 compilador/Main.py {os.path.join(path,file)} temp/{file}")