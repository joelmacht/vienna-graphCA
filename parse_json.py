import json
import geopandas

import common


file_name = common.featureTypes[0]
data = geopandas.read_file("data/original/geojson/{}.geojson".format(file_name), driver="GeoJSON")

data.drop_duplicates(subset="NUTZUNG_CODE", inplace=True)
usage_mapping = dict(zip(data["NUTZUNG_CODE"].values.tolist(), data["NUTZUNG_LEVEL3"].values))

print(usage_mapping)

with open("data/processed/usage_mapping.json", "w", encoding="utf-8") as f:
	json.dump(usage_mapping, f, sort_keys=True, ensure_ascii=False, indent=4)