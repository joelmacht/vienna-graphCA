import geopandas

import accessibility
import common
import visualize


# visualize.plot_map(
# 	common.initial_data,
# 	"state",
# 	[0, 1, 2],
# 	"RdBu",
# 	"maps",
# 	"initial_data"
# )

# mask = common.initial_data["NUTZUNG_LEVEL1"]!="Verkehr"
# non_traffic_data = common.initial_data[mask].copy()
# non_traffic_data["accessibility"] = accessibility.get_accessibility(
# 	non_traffic_data,
# 	common.road_network
# )
non_traffic_data = geopandas.read_file(
	"data/maps/accessibility.geojson",
	driver="GeoJSON"
)
visualize.plot_accessibility(
	non_traffic_data,
	"maps",
	"accessibility"
)
