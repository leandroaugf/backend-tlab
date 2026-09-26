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

path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/'
camadas = open_vector_layers(path, '.shp')
for i in camadas['piaui_dissolve'].getFeatures():
    print (i.attributes());
    
    
