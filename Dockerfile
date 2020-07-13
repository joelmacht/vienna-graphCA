FROM python:3
WORKDIR /usr/src/vienna-graphCA
RUN git config --global user.email "joel.macht@student.kit.edu"
RUN git config --global user.name "Joel Macht"
RUN apt-get -y install libspatialindex-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt