import geopandas
import matplotlib.pyplot as plt
import pandas
import time

import common


epsg = common.projection_epsg
road_network = common.road_network.to_crs(epsg=epsg).geometry

def distance_to_road(parcel_geometry):
	print(i)
	i += 1
	distances = road_network.distance(parcel_geometry)
	return distances.min()

def get_accessibility(parcels):
	return parcels.to_crs(epsg=epsg).geometry.apply(distance_to_road)

if __name__ == "__main__":
	mask = (common.initial_data["BEZ"]=="19") & (common.initial_data["NUTZUNG_LEVEL1"]!="Verkehr")
	parcels_subset = common.initial_data[mask].copy()
	print(parcels_subset.shape)
	
	i=0
	parcels_subset["accessibility"] = get_accessibility(parcels_subset)

	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot()
	plt.axis("off")

	common.road_network.plot(ax=ax, color="black")
	parcels_subset.plot(ax=ax, column="accessibility", cmap="autumn_r")

	plt.savefig("images/debugging/distance.pdf")