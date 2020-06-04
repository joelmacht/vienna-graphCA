# in project root with Dockerfile
docker build -t vienna-graph-ca .
# to run container
docker run -it --mount type=bind,source=$(pwd),target=/usr/src/vienna-graphCA joelmacht/python-dev:vienna-graph-ca bash