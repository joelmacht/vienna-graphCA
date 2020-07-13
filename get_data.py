import re
import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom

import common


service_url = "https://data.wien.gv.at/daten/geo"
get_base = service_url + "?service=WFS&version=1.1.0"

def operation_string(base, request, featureType):
	base += "&request=" + request
	base += "&typeNames=" + featureType
	if (request == "GetFeature"):
		base += "&srsName=EPSG:4326"
	return base

def describe_feature_type_string(base, featureType):
	return operation_string(base, "DescribeFeatureType", featureType)

def get_feature_string(base, featureType):
	return operation_string(base, "GetFeature", featureType)

def get_feature_string_by_count(base, featureType, count):
	return get_feature_string(base, featureType) + "&maxFeatures=" + str(count)

def get_feature_string_by_type(base, featureType, outputFormat):
	return get_feature_string(base, featureType) + "&outputFormat=" + outputFormat

def get_feature_string(base, featureType):
	return operation_string(base, "GetFeature", featureType)

def get_request(get_string):
	print(get_string)
	r = requests.get(get_string)
	return r

count = 2
ns = "ogdwien"

# featureType = "FMZKVERKEHR2OGD"
# for featureType in common.featureTypes:
# 	r = get_request(get_feature_string(get_base, ns+":"+featureType))
# 	with open("data/original/xml/"+featureType+".xml", "w") as f:
# 		xml_data = xml.dom.minidom.parseString(r.text)
# 		pretty_xml_str = xml_data.toprettyxml()
# 		f.write(pretty_xml_str)

for featureType in common.featureTypes:
	r = get_request(get_feature_string_by_type(get_base, ns+":"+featureType, "json"))
	with open("data/original/json/"+featureType+".json", "w") as f:
		f.write(r.text)