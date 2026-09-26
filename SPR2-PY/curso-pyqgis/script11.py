def soma(a, b):
    return a+b

def list_files(path, tipo):
    lst = []
    for root, directory, files in os.walk(path):
        for file in files:
            if file.endswith(tipo):
                print(file)
    return lst;

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados'

list = list_files(path, '.shp')
print (list)