import geopandas

import common
import visualize


file_name = common.featureTypes[0]
initial_data = geopandas.read_file(
	"data/processed/{}.processed.geojson".format(file_name), 
	driver="GeoJSON"
)
visualize.plot_map(
	initial_data,
	"state",
	[0, 1, 2],
	"RdBu",
	"maps",
	"initial_data"
)