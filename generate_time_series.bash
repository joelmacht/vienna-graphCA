featureTypes=("REALNUT200708OGD" "REALNUT2009OGD" "REALNUT2012OGD" "REALNUT2014OGD" "REALNUT2016GOGD" "REALNUT2018OGD")
outputFolder="images/json"
if [ ! -d "${outputFolder}" ]; then
  mkdir ${outputFolder}
fi
for featureType in ${featureTypes[@]}
do
	echo "Rasterizing $featureType"
	# base setup with three channels, initialize to black
	echo $(gdal_rasterize -burn 0 -burn 0 -burn 0 -l $featureType -ot Byte -ts 588 455 data/processed/$featureType.json $outputFolder/$featureType.tif)
	# echo $(gdal_rasterize -b 1 -i -b 2 -i -b 3 -i -burn 255 -l $featureType data/processed/$featureType.json test.tif)
	# echo $(gdal_rasterize -burn 0 -burn 0 -burn 0 -l $featureType data/processed/$featureType.json test.tif)
	# set colors real estate usage category
	echo $(gdal_rasterize -b 1 -burn 255 -l $featureType -where "NUTZUNG_LEVEL1='Verkehr'" data/processed/$featureType.json $outputFolder/$featureType.tif)
	echo $(gdal_rasterize -b 2 -burn 255 -l $featureType -where "NUTZUNG_LEVEL1='Grünlandnutzung'" data/processed/$featureType.json $outputFolder/$featureType.tif)
	echo $(gdal_rasterize -b 3 -burn 255 -l $featureType -where "NUTZUNG_LEVEL1='Baulandnutzung'" data/processed/$featureType.json $outputFolder/$featureType.tif)
done