raster = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/merge.tif';
rlayer = QgsRasterLayer(raster, "dem");

fcn = QgsColorRampShader()
fcn.setColorRampType(QgsColorRampShader.Interpolated)
lst = [
    QgsColorRampShader.ColorRampItem(0, QColor(255, 0, 0)),
    QgsColorRampShader.ColorRampItem(300, QColor(255, 153, 0)),
    QgsColorRampShader.ColorRampItem(900, QColor(255, 255, 102)),
    QgsColorRampShader.ColorRampItem(1200, QColor(153, 255, 102)),
    QgsColorRampShader.ColorRampItem(1600, QColor(0, 51, 0)),
]

fcn.setColorRampItemList(lst)
shader = QgsRasterShader()
shader.setRasterShaderFunction(fcn)
renderer = QgsSingleBandPseudoColorRenderer(rlayer.dataProvider(), 1, shader)
rlayer.setRenderer(renderer)
rlayer.triggerRepaint()
QgsProject.instance().addMapLayer(rlayer)

