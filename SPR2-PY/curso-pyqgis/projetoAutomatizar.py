import sys
sys.path.insert(0, 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/curso-pyqgis/')
from functions import list_files, open_vector_layers,newAttribute,reproject
    


path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
reproject(path, 31981)
camadas = open_vector_layers(path+'reproject/', '.shp')

alertaAero(camadas['31981_aeroportos'], 'tempestade', path+'reproject/', 'uf', 'PR')


