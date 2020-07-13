import geopandas
import pickle

import common


data = geopandas.read_file(
	"data/original/geojson/{}.geojson".format(common.featureTypes[0]), 
	driver="GeoJSON"
)
with open("data/processed/neighbors.pickle", "wb") as f:
	for index, row in data.iterrows():
		neighbors = data[data["geometry"].touches(row["geometry"])].OBJECTID.tolist()
		neighbors = [ID for ID in neighbors if row.OBJECTID != ID ]
		pickle.dump({"id": data.iloc[index].OBJECTID, "neighbors": neighbors}, f)