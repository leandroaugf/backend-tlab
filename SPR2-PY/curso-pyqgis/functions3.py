import sys
from PyQt5.QtCore import QVariant
sys.path.insert(0, 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/curso-pyqgis/')
from functions2 import list_files, open_vector_layers, newAttribute


path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
print(list_files(path, '.shp'))
camadas = open_vector_layers(path, '.shp')
newAttribute(camadas['municipios'], 'descricao', 1)
    
    
