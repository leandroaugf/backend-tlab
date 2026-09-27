import os
import sys
sys.path.insert(0, 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/curso-pyqgis/')
from functions import list_files, open_vector_layers, newAttribute, reproject, alertaAero
###########################    

def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
reproject(path, 31981)

alertaAero(camadas['31981_aeroportos'], 'tempestade', path, 'uf', 'PR')
###########################

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/reproject/'
camadas = open_vector_layers(path, '.shp')

for i in camadas['31981_municipios'].uniqueValues(4):
    outpath = path + 'results/' + i
    createFolder(outpath)


