import re
import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom

service_url = "https://data.wien.gv.at/daten/geo"
get_base = service_url + "?service=WFS&version=1.1.0"
namespaces = {
	"ogdwien" : "http://www.wien.gv.at/ogdwien"
}
featureTypes = [
	"REALNUT2001OGD",
	"REALNUT2003OGD",
	"REALNUT2005OGD",
	"REALNUT200708OGD",
	"REALNUT2009OGD",
	"REALNUT2012OGD",
	"REALNUT2016GOGD",
	"REALNUT2014OGD",
	"REALNUT2018OGD",
]

def operation_string(base, request, featureType):
	base += "&"
	base += "request=" + request
	base += "&"
	base += "typeNames=" + featureType
	return base

def describe_feature_type_string(base, featureType):
	return operation_string(base, "DescribeFeatureType", featureType)

def get_feature_string(base, featureType, count):
	return operation_string(base, "GetFeature", featureType) + "&maxFeatures=" + str(count)

def get_feature_string(base, featureType):
	return operation_string(base, "GetFeature", featureType)

def get_request(get_string):
	print(get_string)
	r = requests.get(get_string)
	return r

count = 2
ns = "ogdwien"
featureType = "GENFLWIDMUNGOGD"

r = get_request(get_feature_string(get_base, ns+":"+featureType))
with open("data/original/"+featureType+".xml", "w") as f:
	xml_data = xml.dom.minidom.parseString(r.text)
	pretty_xml_str = xml_data.toprettyxml()
	f.write(pretty_xml_str)
root = ET.fromstring(r.text)
_, tag = re.split(r"\{*\}", root[0][0].tag)
features = root[0].findall(ns+":"+tag, namespaces)