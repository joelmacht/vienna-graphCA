import geopandas

import common


for featureType in common.featureTypes:
	url = "https://data.wien.gv.at/daten/geo?service=WFS&request=GetFeature&version=1.1.0&srsName=EPSG:4326&outputFormat=json&typeName=ogdwien:{}".format(featureType)
	data = geopandas.read_file(url, driver="GeoJSON")
	data.to_file("data/original/geojson/{}.geojson".format(featureType), driver="GeoJSON")
