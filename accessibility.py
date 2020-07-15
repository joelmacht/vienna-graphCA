import geopandas
import matplotlib.pyplot as plt

import common


def distance_to_road(parcel, road_network):
	projected_road = road_network["geometry"].to_crs(epsg=3395)
	projected_parcel = parcel["geometry"].to_crs(epsg=3395)
	distances = projected_road.distance(projected_parcel.item())
	return distances.min()

def add_accessibility(parcels, road_network):
	parcels["accessibility"] = parcels.apply(distance_to_road, axis=1, args=road_network)

if __name__ == "__main__":
	initial_data = common.initial_data
	road_network = common.road_network

	mask = (initial_data["BEZ"]=="19") & (["NUTZUNG_LEVEL1"]!="Verkehr")
	parcels_subset = initial_data[mask].copy()
	
	road_network_subset = road_network[road_network["BEZ"]=="19"].copy()

	print(distance_to_road(parcels_subset.iloc[[1]], road_network_subset))

	# add_accessibility(parcels_subset, road_network_subset)

	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot()
	plt.axis("off")

	road_network_subset.plot(ax=ax, color="black")
	parcels_subset.iloc[[1]].plot(ax=ax, color="red")

	# plt.savefig("images/debugging/roadsubset.pdf")

	plt.savefig("images/debugging/distance.pdf")