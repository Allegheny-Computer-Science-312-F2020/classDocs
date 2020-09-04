FROM ubuntu

# RUN apt-get update

RUN \
	apt-get update &&\
	apt-get install -y git &&\
	apt-get install -y htop &&\
	apt-get install -y vim &&\
#	apt-get install -y python &&\
	apt-get install -y python3 &&\
	apt-get install -y python3-pip &&\
  apt-get install -y sqlite


RUN useradd dbdev
RUN mkdir /home/dbdev
RUN export HOME=/home/dbdev

WORKDIR /home/dbdev

# Define default command.
CMD ["bash"]



# BUILD: docker build -t dbdev .
# RUN: docker run -it dbdev
# MOUNT AND RUN: # mount a directory and then get to bash to do some work.
# docker run -it --mount type=bind,source=$PWD,target=/home/dbdev dbdev

# Alden Hall: running this docker at Alden must have a different source directory due to network configuration
# docker run -it --mount type=bind,source=/tmp/dbdev,target=/home/dbdev dbdev
