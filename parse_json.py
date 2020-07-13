import json
import geopandas

import common


file_name = common.featureTypes[0]
data = geopandas.read_file(
	"data/original/geojson/{}.geojson".format(file_name), 
	driver="GeoJSON"
)
unique_entries = data.drop_duplicates(subset="NUTZUNG_CODE")
usage_mapping = dict(
	zip(
		unique_entries["NUTZUNG_CODE"].values.tolist(), 
		unique_entries["NUTZUNG_LEVEL3"].values
	)
)
print(usage_mapping)
with open("data/processed/usage_mapping.json", "w", encoding="utf-8") as f:
	json.dump(usage_mapping, f, sort_keys=True, ensure_ascii=False, indent=4)

def encode_state(usage_code):
	if usage_code in [18, 27, 30, 31]:
		return 1
	if usage_code in range(1, 4+1):
		return 0
	if usage_code in range(5, 17+1):
		return 2
	else:
		return None
non_traffic_data = data[data["NUTZUNG_LEVEL1"]!="Verkehr"]
non_traffic_data["state"] = non_traffic_data["NUTZUNG_CODE"].apply(encode_state)
non_traffic_data.dropna(axis=0, subset=["state"], inplace=True)
non_traffic_data = non_traffic_data.astype({"state": "int"})
states = non_traffic_data[["OBJECTID", "state", "geometry"]]
states.to_file(
	"data/processed/{}.processed.geojson".format(file_name),
	driver="GeoJSON"
)