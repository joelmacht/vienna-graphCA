import json
import geopandas
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

import common


def conv(x): 
	if x == 'Verkehr': 
		return 1
	if x == 'Baulandnutzung': 
		return 2
	if x == 'Grünlandnutzung': 
		return 3

def plot_map(data, column, values, colormap_name, output_folder, file_name):
	cmap = plt.cm.get_cmap(colormap_name, len(values))
	figure = plt.figure()
	axis = figure.add_subplot()
	data.boundary.plot(ax=axis, edgecolor="black", linewidth=0.1)
	for value in values:
		data[data[column]==value].plot(ax=axis, facecolor=cmap(value), label=value)
	axis.axis("off")
	axis.legend()
	figure.savefig("{}/{}.pdf".format(output_folder, file_name))

def plot_accessibility(parcels, output_folder, file_name):
	figure = plt.figure()
	axes = figure.add_subplot()
	axes.axis("off")

	common.road_network.plot(ax=axes, color="black")
	parcels.boundary.plot(ax=axes, column="accessibility", cmap="autumn_r")

	figure.savefig("{}/{}.pdf".format(output_folder, file_name))

# with open("data/processed/usage_mapping.json", "r") as f:
# 	usage_mapping = json.load(f)
# usage_mapping = {int(key): value for key, value in usage_mapping.items()}

# cmap = plt.cm.get_cmap('viridis', len(usage_mapping.keys()))

# handles = [mpatches.Patch(color=cmap(key), label=usage_mapping[key]) for key in usage_mapping.keys()]

# figure, axes = plt.subplots(len(common.featureTypes)//2, 2)
# titles = [
# 	"2007/08",
# 	"2009",
# 	"2012",
# 	"2014",
# 	"2016",
# 	"2018"
# ]
# for axis, featureType, title in zip(axes.reshape(-1), common.featureTypes, titles):
# 	print(featureType)
# 	data = geopandas.read_file("data/original/geojson/{}.geojson".format(featureType), driver="GeoJSON")
# 	for key in usage_mapping.keys():
# 		data[data["NUTZUNG_CODE"]==key].plot(ax=axes, facecolor=cmap(key))
# 	axis.axis("off")
# 	axis.set_title(title, fontsize=8, family="sans-serif", color="darkgrey")
# plt.subplots_adjust(left=0.25,
#                     bottom=0.1, 
#                     right=0.75, 
#                     top=0.9, 
#                     wspace=0.2, 
#                     hspace=0.35)
# plt.savefig("maps/ground-truth/all.pdf")