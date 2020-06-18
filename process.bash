featureTypes=("REALNUT200708OGD" "REALNUT2009OGD" "REALNUT2012OGD" "REALNUT2016GOGD"	"REALNUT2014OGD" "REALNUT2018OGD")
outputFolder="data/processed"
if [ ! -d "${outputFolder}" ]; then
  mkdir ${outputFolder}
fi
for featureType in ${featureTypes[@]}
do
	echo "Converting $featureType"
	$(ogr2ogr -f GeoJSON $outputFolder/$featureType.json data/original/$featureType.xml)
done