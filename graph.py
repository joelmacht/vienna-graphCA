import geopandas
import math
import matplotlib.pyplot as plt
import networkx
import numpy
import pickle
import time

import common


data = geopandas.read_file(
	"data/original/geojson/{}.geojson".format(common.featureTypes[0]), 
	driver="GeoJSON"
)
data = data.to_crs(epsg=3395) # Mercator, avoid warnings when using Platte Carre
print("Dataset used for initialization:", common.featureTypes[0])
print("CRS:", data.crs)

graph = networkx.DiGraph()

nodelist = []
edgelist = []
pos = {}
node_size = []

figure = plt.figure(figsize=(20, 20))
axis = figure.add_subplot()
with open("data/processed/neighbors.pickle", "rb") as f:
	for i in range(5000):
		node = pickle.load(f)
		
		parcel = data[data["OBJECTID"]==node["id"]]
		
		# filter by usage
		usage = parcel["NUTZUNG_CODE"].values[0]
		if usage not in [1, 2, 3]:
			continue

		# filter out streets
		cleaned_neighbors = []
		for neighbor in node["neighbors"]:
			neighbor_parcel = data[data["OBJECTID"]==neighbor]
			usage_LoD1 = neighbor_parcel["NUTZUNG_LEVEL1"].values[0]
			if usage_LoD1 != "Verkehr":
				cleaned_neighbors.append(neighbor)

		graph.add_node(node["id"])

		edges = zip(
			[node["id"]]*len(cleaned_neighbors),
			cleaned_neighbors
		)
		graph.add_edges_from(edges)

		nodelist.append(node["id"])

		centroid = parcel["geometry"].centroid.values[0]
		pos[node["id"]] = [centroid.x, centroid.y]

		radius = math.sqrt(parcel["FLAECHE"]/math.pi)
		node_size.append(radius)

		for neighbor in cleaned_neighbors:
			neighbor_parcel = data[data["OBJECTID"]==neighbor]
			nodelist.append(neighbor)
			centroid = neighbor_parcel["geometry"].centroid.values[0]
			pos[neighbor] = [centroid.x, centroid.y]

			radius = math.sqrt(neighbor_parcel["FLAECHE"]/math.pi)
			node_size.append(radius)
			neighbor_parcel.plot(ax=axis, facecolor="lightgrey")

		edgelist.append(edges)

		parcel.plot(ax=axis, facecolor="lightgrey")

		print("Number of nodes:", len(graph.nodes))

networkx.draw(
	graph, 
	ax=axis, 
	pos=pos, 
	arrowsize=0.5, 
	nodelist=nodelist, 
	node_size=node_size, 
	node_color=[(0.5, 0.5, 0.5, 0.5)],
	width=0.05
)

plt.savefig(
	"maps/graph/{}.pdf".format(
		time.strftime(
			"%Y-%m-%d-%H%M%S", 
			time.localtime()
		)
	)
)
