path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados'

for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.shp'):
            path_vector = nome_arquivo;
            layer = QgsVectorLayer(path_vector, file[0:-4], "ogr")
            QgsProject.instance().addMapLayer(layer);
            
    
            
