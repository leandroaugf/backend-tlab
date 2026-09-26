path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/cbers.tif'
rlayer = QgsRasterLayer(path, "cbers")
QgsProject.instance().addMapLayer(rlayer);
#iface.addRasterLayer(path, "cbers")

rlayer.htmlMetadata()
print(rlayer.width(), rlayer.height())
print(rlayer.extent().toString())
print(rlayer.rasterType())
print(rlayer.bandCount())