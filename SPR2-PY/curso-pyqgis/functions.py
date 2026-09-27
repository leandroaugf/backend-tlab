import os
import processing
from qgis.core import *
from qgis.utils import iface
from PyQt5.QtCore import QVariant

def list_files(path, tipo):
    lst = []
    for root, directory, files in os.walk(path):
        for file in files:
            if file.endswith(tipo):
                lst.append(file)
    return lst;

def open_vector_layers(path, type):
    vectors = {}
    files = list_files(path,type)
    
    for file in files:
        filename = file.split('.')[0];
        vector = iface.addVectorLayer(path+file, filename, "ogr")
        vectors.update({filename: vector})
    
    return vectors

def newAttribute(layer, fieldName, type):
    if type == 1:
        fieldType = QVariant.String
    elif type == 2:
        fieldType = QVariant.Int
    else:
        fieldType = QVariant.Double
        
    layer.startEditing()
    layer.addAttribute(QgsField(fieldName , fieldType))
    layer.commitChanges()
    
    return
    
def createFolder(inputpath):
    if not os.path.exists(inputpath + 'reproject'):
        os.makedirs(inputpath+'reproject')
    
    
def reproject(path, epsg):
    createFolder(path)
    for shape in list_files(path, '.shp'):
        inputpath = path+shape
        outpath = path + '/reproject/' + str(epsg) + '_' + shape 
        processing.run("native:reprojectlayer", 
                   {'INPUT' : inputpath, 
                    'TARGET_CRS' : QgsCoordinateReferenceSystem(f'EPSG:{epsg}'),
                    'OUTPUT' : outpath })
    
    return

def applyFilter(layer, field, param):
    return layer.setSubsetString(f"{field} = '{param}'")

def alertaAero(layer, param, path, field, state):
    applyFilter(layer, 'uf', state)
    
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
    
    iface.addVectorLayer(path+'buffer.shp', "análise buffer", "ogr")
    return

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
camadas = open_vector_layers(path, '.shp')

print(camadas)
newAttribute(camadas['municipios'], 'descricao', 1)
    
    
