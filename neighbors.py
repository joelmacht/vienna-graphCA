import geopandas
import matplotlib.pyplot as plt
import pickle

import common


def buffer_parcel(parcel, distance):
	buffered_geometry = parcel["geometry"] \
		.to_crs(epsg=3395) \
		.buffer(distance, resolution=16)
	buffered_parcel = parcel.copy()
	buffered_parcel["geometry"] = buffered_geometry.to_crs(parcel.crs)
	return buffered_parcel

# def get_neighbors_in_buffer(parcels, parcel, origin_epsg, projection_epsg, distance):
# 	buffered_parcel = buffer_parcel(parcel, origin_epsg, projection_epsg, distance)
# 	neighbor_parcels = parcels[parcels.to_crs(projection_epsg).overlaps(buffered_parcel)]
# 	return neighbor_parcels

# data = geopandas.read_file(
# 	"data/original/geojson/{}.geojson".format(common.featureTypes[0]), 
# 	driver="GeoJSON"
# )
# with open("data/processed/neighbors.pickle", "wb") as f:
# 	for index, row in data.iterrows():
# 		neighbors = data[data["geometry"].touches(row["geometry"])].OBJECTID.tolist()
# 		neighbors = [ID for ID in neighbors if row.OBJECTID != ID ]
# 		pickle.dump({"id": data.iloc[index].OBJECTID, "neighbors": neighbors}, f)

if __name__ == "__main__":
	parcels = geopandas.read_file(
		"data/original/geojson/{}.geojson".format(common.featureTypes[0]), 
		driver="GeoJSON",
	)
	parcels_subset = parcels[parcels["BEZ"]=="01"]

	parcel = parcels_subset.iloc[[2]]
	buffered_parcel = buffer_parcel(parcel, 150)
	print(buffered_parcel)
	# neigbor_parcels = get_neighbors_in_buffer(parcels_subset, parcel, 4326, 3395, 200)

	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot()

	parcels_subset.plot(ax=ax, color="lightgrey")
	buffered_parcel.plot(ax=ax, color="darkgrey", alpha=0.5)
	parcel.plot(ax=ax, color="crimson")
	# neigbor_parcels.to_crs(epsg=3395).plot(ax=ax)

	plt.axis("off")
	plt.savefig("images/debugging/buffer.png")