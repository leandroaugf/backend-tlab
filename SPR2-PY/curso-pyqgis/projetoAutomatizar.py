import sys
sys.path.insert(0, 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/curso-pyqgis/')
from functions import list_files, open_vector_layers,newAttribute,reproject
    
def applyFilter(layer, field, param):
    return layer.setSubsetString(f"{field} = '{param}'")

def alertaAero(layer, param, path):
    if param == 'seco':
        buffer = 200
    elif param == 'chuva':
        buffer = 1000
    else: # tempestade
        buffer = 3000
        
    processing.run("native:buffer", 
                  {'INPUT': layer,
                  'DISTANCE':buffer,
                  'SEGMENTS':5,
                  'END_CAP_STYLE':0,
                  'JOIN_STYLE':0,
                  'MITER_LIMIT':2,
                  'DISSOLVE':True,
                  'SEPARATE_DISJOINT':False,
                  'OUTPUT': path+'buffer.shp'})

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
print(list_files(path, '.shp'))

reproject(path, 31981)
camadas = open_vector_layers(path+'reproject/', '.shp')

newAttribute(camadas['aeroportos'], 'teste2', 1)

applyFilter(camadas['31981_aeroportos'], 'uf', 'MG')

alertaAero(camadas['31981_aeroportos'], 'seco', path+'reproject/')