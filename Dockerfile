FROM python:3
WORKDIR /usr/src/vienna-graphCA
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN git config --global user.email "joel.macht@student.kit.edu"
RUN git config --global user.name "Joel Macht"
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs