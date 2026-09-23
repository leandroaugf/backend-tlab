# dados vetoriais

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados'

# Abrindo uma camada vetorial
path_layer = path + '/aeroportos.shp'

layer = QgsVectorLayer(path_layer, "Aeroportos", "ogr");
print(layer)

QgsProject.instance().addMapLayer(layer);

