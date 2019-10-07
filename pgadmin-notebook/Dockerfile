# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=mphanaenvacr.azurecr.io/base-notebook:latest
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# Install Tensorflow
USER root    
RUN apt-get update && apt-get install -y \
	build-essential \
	libssl-dev \
	libffi-dev \
	libgmp3-dev \
	virtualenv \
	python-pip \
	libpq-dev \
	python-dev && \
	
RUN mkdir pgAdmin4 && \
	cd pgAdmin4 && \
	virtualenv pgAdmin4 && \
	cd pgAdmin4
    source bin/activate
	wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v2.1/pip/pgadmin4-2.1-py2.py3-none-any.whl && \
	pip install pgadmin4-2.1-py2.py3-none-any.whl && \
	
