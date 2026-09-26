# dados vetoriais
path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados'

# Abrindo uma camada vetorial
path_layer = path + '/aeroportos.shp'
layer = QgsVectorLayer(path_layer, "Aeroportos", "ogr");

# camada no canvas
QgsProject.instance().addMapLayer(layer)

print(layer.id())
print(layer.extent())

# Criar novos atributos
layer.startEditing();
layer.addAttribute(QgsField('campoTest', QVariant.String));
layer.commitChanges();

# Obter info de um campo
print(layer.fields().names()[3])

# delete
layer.startEditing()
layer.deleteAttribute(15)
layer.commitChanges();

count = 0
for feature in layer.getFeatures():
    while (count < 5):
        print(feature.attributes()[3])
        count += 1
    
# alterando e update nos campos    
layer.startEditing()
layer.deleteAttribute(13)
layer.commitChanges()

# update
layer.startEditing()
layer.addAttribute(QgsField('y', QVariant.Double))
layer.commitChanges()

layer.startEditing()

for feature in layer.getFeatures():
    id = feature.id()
    y = feature.geometry().asPoint()[1]

    attr_value = {15: y}
    layer.changeAttributeValues(id, attr_value)

layer.commitChanges()

# seleção por expressão
layer.selectByExpression("TipoAero = 'Nacional'", QgsVectorLayer.SetSelection)

# inversão da seleção
layer.invertSelection()

# adição à seleção
layer.selectByExpression("nome ilike 'N%'", QgsVectorLayer.AddToSelection)

# remover da seleção
layer.selectByExpression("nome ilike 'N%'", QgsVectorLayer.RemoveFromSelection)

# criar um objeto com a seleção
selection = layer.selectedFeatures()
for feature in selection:
    print(feature.attributes())
    
# deletar campos
layer.startEditing()
#layer.deleteAttributes([14, 15])
layer.deleteAttributes([13])
layer.commitChanges()

# criando uma nova coluna tipo text
layer.startEditing()
layer.addAttribute(QgsField('newColumn', QVariant.String, 'text', 255))
layer.commitChanges()

# update valores na tabela em selecionados
layer.startEditing()
for feature in selection:
    id = feature.id()
    layer.changeAttributeValue(id, 13, 'newvar')

layer.commitChanges()



