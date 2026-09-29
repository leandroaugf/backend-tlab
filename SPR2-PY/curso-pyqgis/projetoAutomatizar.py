import os
import sys
sys.path.insert(0, 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/curso-pyqgis/')
from functions import list_files, open_vector_layers, newAttribute, reproject, alertaAero
###########################    

def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return
    
def applyFilter(layer, field, param):
    return layer.setSubsetString(f"{field} = '{param}'")

def toGeopackage(layer, filename, outpath):
    options = QgsVectorFileWriter.SaveVectorOptions()
    transformContext = QgsProject.instance().transformContext()
    QgsVectorFileWriter.writeAsVectorFormatV2(layer, outpath, transformContext, options)
    return
    
def fixGeometries(path, camadas):
    output_folder = path + 'fixed/'
    createFolder(output_folder)

    for camada in camadas:
        input_path = path + camada + '.shp'
        output_path = output_folder + camada + '.shp'

        processing.run(
            "native:fixgeometries",
            {
                'INPUT': input_path,
                'OUTPUT': output_path
            }
        )
    

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
reproject(path,31981)
camadas = open_vector_layers(path+'reproject/', '.shp')
alertaAero(camadas['31981_aeroportos'], 'tempestade', path+'reproject/', 'uf', 'PR')

####################################

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/reproject/'
camadas = open_vector_layers(path, '.shp')
fixGeometries(path, camadas)

for i in camadas['31981_municipios'].uniqueValues(4):
    outpath = path + 'results/' + i
    createFolder(outpath)
    applyFilter(camadas['31981_municipios'], 'uf', i)
    filename = i
    outpath2 = outpath + '/' + i
    toGeopackage(camadas['31981_municipios'], filename, outpath2)
    camadas['31981_municipios'].setSubsetString("")


