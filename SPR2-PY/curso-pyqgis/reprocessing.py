path = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/rodovias.shp'
outpath = 'C:/Users/leand/Desktop/backend-tlab/SPR2-PY/dados/rodovias31982.shp'

# reproject
processing.run("native:reprojectlayer", 
                {
                'INPUT' : path, 
                'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:31982'),
                'OUTPUT' : outpath })
