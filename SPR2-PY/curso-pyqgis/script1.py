#   QGIS Project

project = QgsProject.instance()

project.read('C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/dados_sig.qgs')
print(project.fileName());

print(project.crs());

