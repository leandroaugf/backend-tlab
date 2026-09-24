# dados vetoriais

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados'

# Abrindo uma camada vetorial
path_layer = path + '/aeroportos.shp'

layer = QgsVectorLayer(path_layer, "Aeroportos", "ogr");
print(layer)

# Adicionando camadas ao canvas
QgsProject.instance().addMapLayer(layer);

# método 2: adicionando camadas
layer = iface.addVectorLayer(path_layer, "Aeroportos")

