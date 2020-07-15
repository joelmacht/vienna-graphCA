import geopandas
import matplotlib.patches as patches
import matplotlib.pyplot as plt


namespaces = {
	"ogdwien" : "http://www.wien.gv.at/ogdwien"
}

featureTypes = [
	"REALNUT200708OGD",
	"REALNUT2009OGD",
	"REALNUT2012OGD",
	"REALNUT2014OGD",
	"REALNUT2016GOGD",
	"REALNUT2018OGD",
]

attributes = {
	"code" : "NUTZUNG_CODE",
	"LoD1" : "NUTZUNG_LEVEL1",
	"LoD2" : "NUTZUNG_LEVEL2",
	"LoD3" : "NUTZUNG_LEVEL3",
	"area" : "FLAECHE",
	"district" : "BEZ",
}

values = {
	"NUTZUNG_CODE" : [str(i) for i in range(1, 33)],
	"NUTZUNG_LEVEL1" : ["Baulandnutzung", "Verkehr", "Grünlandnutzung"],
	"NUTZUNG_LEVEL3" : ["Bahnhöfe und Bahnanlagen",],
	"BEZ" : ["0"+str(i) for i in range(1, 10)]+[str(i) for i in range(10, 24)],
}

projection_epsg = 3395

initial_data = geopandas.read_file(
	"data/original/geojson/{}.geojson".format(featureTypes[0]), 
	driver="GeoJSON"
)

is_road = initial_data["NUTZUNG_CODE"].apply(lambda x: x in [19, 20, 22])
road_network = initial_data[is_road]

if __name__ == "__main__":
	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot()
	plt.axis("off")

	road_network.plot(ax=ax, color="black")

	x1, y1, x2, y2 = initial_data[initial_data["BEZ"]=="19"].total_bounds
	rectangle = patches.Rectangle(
		(x1, y1), 
		x2-x1, 
		y2-y1,
		linewidth=1,
		edgecolor="red",
		facecolor="none"
	)
	ax.add_patch(rectangle)

	plt.savefig("images/debugging/road_network.pdf")
