import sys
sys.path.insert(0, 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/curso-pyqgis/')

from functions import list_files, open_vector_layers,newAttribute,reproject
    
path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
print(list_files(path, '.shp'))

camadas = open_vector_layers(path, '.shp')

newAttribute(camadas['aeroportos'], 'teste2', 1)
reproject(path, 5880)
