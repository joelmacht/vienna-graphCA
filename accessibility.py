import geopandas
import matplotlib.pyplot as plt
import numpy
import pandas
import time

import common


epsg = common.projection_epsg

def distance_to_road(polygon):
	return polygon.distance(common.road_network)

def get_accessibility(parcels):
	polygons = parcels.to_crs(epsg=epsg).geometry.values.to_numpy()
	accessibility = numpy.zeros(polygons.size)
	i = 0
	for i in range(polygons.size):
		print(i)
		accessibility[i] = distance_to_road(polygons[i])
	return accessibility

if __name__ == "__main__":
	mask = (common.initial_data["BEZ"]=="19") & (common.initial_data["NUTZUNG_LEVEL1"]!="Verkehr")
	parcels_subset = common.initial_data[mask].copy()
	print(parcels_subset.shape)
	
	parcels_subset["accessibility"] = get_accessibility(parcels_subset)

	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot()
	plt.axis("off")

	common.road_network.plot(ax=ax, color="black")
	parcels_subset.plot(ax=ax, column="accessibility", cmap="autumn_r")

	plt.savefig("images/debugging/distance.pdf")