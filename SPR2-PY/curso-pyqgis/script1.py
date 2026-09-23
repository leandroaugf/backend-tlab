#   QGIS Project

project = QgsProject.instance()

project.read('C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/dados_sig_teste.qgs')
print(project.fileName());

print(project.crs());

project.write('C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/dados_sig_teste.qgs');
project.setBackgroundColor(QColor(51, 153, 255))
project.setBackgroundColor(QColor(220, 220, 220))

project.count