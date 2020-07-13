Datenquelle: Stadt Wien – data.wien.gv.at
https://digitales.wien.gv.at/site/open-data/ogd-nutzungsbedingungen/

# in project root with Dockerfile
docker build -t joelmacht/python-dev:vienna-graph-ca .
# to run container
docker run -it --mount type=bind,source=$(pwd),target=/usr/src/vienna-graphCA joelmacht/python-dev:vienna-graph-ca bash
# to run container with gdal lib
docker run -it --mount type=bind,source=$(pwd),target=/usr/src/vienna-graphCA osgeo/gdal:ubuntu-small-latest bash