path = "C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados"

for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.shp'):
            path_vector = os.path.join(path, file)
            layer = QgsVectorLayer(path_vector, file[0:-4], "ogr")
            QgsProject.instance().addMapLayer(layer);

municipios = QgsProject.instance().mapLayersByName("municipios")[0]
print(municipios.featureCount())

# filtrando apenas os municípios de MG
municipios.setSubsetString("uf = 'MG'")
print(municipios.featureCount())

municipios.setSubsetString("")
