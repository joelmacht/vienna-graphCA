import geopandas
import matplotlib.pyplot as plt
import pandas

import common


def distance_to_road(parcel, road_network):
	projected_road = road_network["geometry"].to_crs(epsg=3395)
	projected_parcel = parcel["geometry"].to_crs(epsg=3395)
	distances = projected_road.distance(projected_parcel.item())
	return distances.min()

def get_accessibility(parcels):
	accessibility = []
	for i in range(parcels.shape[0]):
		parcel = parcels.iloc[[i]]
		distance = distance_to_road(parcel, common.road_network)
		accessibility.append(distance)
	return accessibility

if __name__ == "__main__":
	mask = (common.initial_data["BEZ"]=="19") & (common.initial_data["NUTZUNG_LEVEL1"]!="Verkehr")
	parcels_subset = common.initial_data[mask].copy()
	
	parcel = parcels_subset.iloc[[0]]
	distance = distance_to_road(parcel, common.road_network)
	print(distance)

	parcels_subset["accessibility"] = get_accessibility(parcels_subset)

	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot()
	plt.axis("off")

	common.road_network.plot(ax=ax, color="black")
	parcels_subset.plot(ax=ax, column="accessibility", cmap="autumn_r")
	# parcels_subset.plot(ax=ax, color="red")

	plt.savefig("images/debugging/distance.pdf")