path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados'

for root, directory, files in os.walk(path):
    for file in files:
        if (file.endswith('.shp')):
            path_vector = os.path.join(path, file)
            layer = QgsVectorLayer(path_vector, file[0:-4], "ogr")
            QgsProject.instance().addMapLayer(layer)
            
        
QgsProject.instance().mapLayers()

aeroportos = QgsProject.instance().mapLayersByName('aeroportos')[0]
municipios = QgsProject.instance().mapLayersByName('municipios')[0]
rodovias = QgsProject.instance().mapLayersByName('rodovias')[0]

# dados métricos
d = QgsDistanceArea()
d.setEllipsoid("WGS84")

count = 0;
for feature in municipios.getFeatures():
    if count < 5:
        municipio = feature["municipio"]
        geom = feature.geometry()
        area = d.measureArea(geom) # m²
        areakm2 = d.convertAreaMeasurement(area, QgsUnitTypes.AreaSquareKilometers) # m² -> km²
        perimeter = d.measurePerimeter(geom) # m

        
        print(municipio);
        print("área(m²): ", area)
        print("área(km²): ", areakm2)

        print("perímetro(m): ", perimeter)
        count += 1
        
    else:
        break;
    
# Distância entre dois pontos (no caso, dois aeroportos)
aeroportos.selectByExpression("FID_1 in (2411,2425)", QgsVectorLayer.SetSelection)
selected = aeroportos.selectedFeatures();
print(selected)

d = QgsDistanceArea()
d.setEllipsoid("WGS84")

pontos = []
for feature in selected:
    municipio = feature["nm_municip"]
    geom = feature.geometry()
    pontos.append([municipio, geom.asPoint()])

print(pontos)

distancia = d.measureLine(pontos[0][1], pontos[1][1])
print(f'distância entre {pontos[0][0]} e {pontos[1][0]}: {distancia} metros');
    