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

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
camadas = open_vector_layers(path, '.shp')

print(camadas)
newAttribute(camadas['municipios'], 'descricao', 1)
    
    
