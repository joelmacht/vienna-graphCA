import geopandas
import matplotlib.pyplot as plt
import pickle

import common


def buffer_parcel(parcel, distance):
	buffered_geometry = parcel["geometry"] \
		.to_crs(epsg=3395) \
		.buffer(distance, resolution=20)
	buffered_parcel = parcel.copy()
	buffered_parcel["geometry"] = buffered_geometry.to_crs(parcel.crs)
	return buffered_parcel

def get_neighbors(parcels, parcel):
	mask = parcels["geometry"].intersects(parcel["geometry"].item())
	neighbor_parcels = parcels[mask].copy()
	neighbor_parcels.drop(index=parcel.index, inplace=True) # remove parcel itself
	return neighbor_parcels

if __name__ == "__main__":
	parcels = geopandas.read_file(
		"data/original/geojson/{}.geojson".format(common.featureTypes[0]), 
		driver="GeoJSON",
	)
	parcels_subset = parcels[parcels["BEZ"]=="01"]

	parcel = parcels_subset.iloc[[2]]
	buffered_parcel = buffer_parcel(parcel, 200)
	neigbor_parcels_unbuffered = get_neighbors(parcels_subset, parcel)
	neigbor_parcels_buffered = get_neighbors(parcels_subset, buffered_parcel)

	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot()
	plt.axis("off")

	parcels_subset.boundary.plot(ax=ax, color="black", linewidth=.5)
	buffered_parcel.boundary.plot(ax=ax, color="black", linestyle="dashed")
	parcel.plot(ax=ax, color="darkgrey")

	plt.savefig("images/debugging/buffer.pdf")

	neigbor_parcels_buffered.plot(ax=ax, color="lightgrey")
	
	plt.savefig("images/debugging/neighborhood.pdf")