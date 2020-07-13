import lxml.etree as ET

import common

def add_namespace(namespace, tag):
	tag = "{}:{}".format(
		namespace, 
		tag
	)
	return tag

def get_features_by_attribute_value(featureCollection, featureTag, attributeTag, value):
	xpath = "./{}[{}='{}']".format(featureTag, attributeTag, value)
	print(xpath)
	return featureCollection.xpath(xpath, namespaces=common.namespaces)

def get_attribute_values(featureCollection, featureTag, attributeTag):
	xpath = "./{}/{}".format(featureTag, attributeTag)
	attributes = featureCollection.findall(xpath)
	unique = [attributes[0].text]
	for attribute in attributes:
		if attribute.text not in unique:
			unique.append(attribute.text)
	return unique

def get_features_by_attribute_values(featureCollection, featureTag, attributeTagValuePairs):
	pairs = [
		"{}='{}'".format(*attributeTagValuePair) 
			for attributeTagValuePair in attributeTagValuePairs
	]
	condition = " and ".join(pairs)
	xpath = "./{}[{}]".format(featureTag, condition)
	return featureCollection.xpath(xpath, namespaces=common.namespaces)

featureType = common.featureTypes[-3]
featureTag = add_namespace("ogdwien", featureType)
attributeTag = add_namespace("ogdwien", common.attributes["LoD1"])
pairs = []
pairs.append((attributeTag, "Verkehr"))
attributeTag = add_namespace("ogdwien", common.attributes["district"])
pairs.append((attributeTag, "01"))
featureCollection = ET.parse("data/original/{}.xml".format(featureType)).getroot()[0]
print(featureType, len(get_features_by_attribute_values(featureCollection, featureTag, pairs)))

featureType = common.featureTypes[-2]
featureTag = add_namespace("ogdwien", featureType)
attributeTag = add_namespace("ogdwien", common.attributes["LoD3"])
pairs = []
# pairs.append((attributeTag, "Bahnhöfe und Bahnanlagen"))
attributeTag = add_namespace("ogdwien", common.attributes["district"])
pairs.append((attributeTag, "21"))
featureCollection = ET.parse("data/original/{}.xml".format(featureType)).getroot()[0]
features = get_features_by_attribute_values(featureCollection, featureTag, pairs)
# features_all = []
# for featureType in common.featureTypes:
# 	featureTag = "{{{0}}}{1}".format(common.namespaces["ogdwien"], featureType)
# 	attributeTag = "{{{0}}}{1}".format(
# 		common.namespaces["ogdwien"], 
# 		common.attributes["LoD1"]
# 	)
# 	root = ET.parse("data/original/{}.xml".format(featureType)).getroot()
# 	featureCollection = root[0]
# 	features = get_features_by_attribute_value(
# 		featureCollection,
# 		featureTag,
# 		attributeTag,
# 		common.values[common.attributes["LoD1"]][1],
# 	)
# 	print(featureType, len(features))
# 	features_all.append(features)

# # query for possible attribute values
# featureType = common.featureTypes[-3]
# featureTag = "{{{0}}}{1}".format(
# 	common.namespaces["ogdwien"], 
# 	featureType
# )
# attributeTag = "{{{0}}}{1}".format(
# 	common.namespaces["ogdwien"], 
# 	common.attributes["district"]
# )
# root = ET.parse("data/original/{}.xml".format(featureType)).getroot()
# featureCollection = root[0]
# print(sorted(get_attribute_values(featureCollection, featureTag, attributeTag)))
