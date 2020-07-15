import geopandas
import matplotlib.pyplot as plt

import common


def distance_to_road(parcel):
	distances = road_network_subset["geometry"].distance(parcel["geometry"])
	return distances.min()

def add_accessibility(parcels):
	parcels["accessibility"] = parcels.apply(distance_to_road, axis=1)

if __name__ == "__main__":
	initial_data = common.initial_data
	road_network = common.road_network
	parcels_subset = initial_data[initial_data["BEZ"]=="19"].copy()
	
	road_network_subset = road_network[road_network["BEZ"]=="19"].copy()

	add_accessibility(parcels_subset)

	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot()
	plt.axis("off")

	road_network_subset.plot(ax=ax, color="pink")
	parcels_subset.plot(ax=ax, column="accessibility", cmap="hot")

	plt.savefig("images/debugging/distance.pdf")