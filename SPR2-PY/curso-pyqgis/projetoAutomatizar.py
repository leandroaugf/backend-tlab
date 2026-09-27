import os
import sys
sys.path.insert(0, 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/curso-pyqgis/')
from functions import list_files, open_vector_layers, newAttribute, reproject, alertaAero
###########################    

def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    
def applyFilter(layer, field, param):
    return layer.setSubsetString(f"{field} = '{param}'")

def toGeopackage(layer, filename, outpath):
    options = QgsVectorFileWriter.SaveVectorOptions()
    transformContext = QgsProject.instance().transformContext()
    QgsVectorFileWriter.writeAsVectorFormatV2(layer, outpath, transformContext, options)
    return

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
reproject(path, 31981)

alertaAero(camadas['31981_aeroportos'], 'tempestade', path, 'uf', 'PR')
###########################

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/reproject/'
camadas = open_vector_layers(path, '.shp')

for i in camadas['31981_municipios'].uniqueValues(4):
    outpath = path + 'results/' + i
    createFolder(outpath)
    applyFilter(camadas['31981_municipios'], 'uf', i)
    filename = i
    outpath2 = outpath + '/' + i
    toGeopackage(camadas['31981_municipios'], filename, outpath2)
    camadas['31981_municipios'].setSubsetString("")


