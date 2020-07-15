import geopandas


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

initial_data = geopandas.read_file(
	"data/original/geojson/{}.geojson".format(featureTypes[0]), 
	driver="GeoJSON"
)

is_road = initial_data["NUTZUNG_CODE"].apply(lambda x: x in [19, 20, 22])
road_network = initial_data[is_road]