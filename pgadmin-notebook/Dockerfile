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
	python-dev

USER $NB_USER 	
RUN cd $CONDA_DIR && \
	mkdir pgadmin4 && \
	cd pgadmin4 && \
	wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.9/pip/pgadmin4-4.9-py2.py3-none-any.whl && \
	pip install pgadmin4-4.9-py2.py3-none-any.whl
	
ADD config_local.py /opt/conda/lib/python3.7/site-packages/pgadmin4
COPY jupyter-pgadmin-proxy /opt/conda/pdadmin4/jupyter-pgadmin-proxy
COPY pgAdmin4.py /opt/conda/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py

USER root
RUN chown -R jovyan:users /opt/conda/pdadmin4/jupyter-pgadmin-proxy && \
	chown -R jovyan:users /opt/conda/lib/python3.7/site-packages/pgadmin4

USER $NB_USER 	
RUN python /opt/conda/lib/python3.7/site-packages/pgadmin4/setup.py && \
#	printf 'zjia@ksmconsulting.com\nSimple123!\nSimple123!\n' |  python /opt/conda/lib/python3.7/site-packages/pgadmin4/setup.py && \
	fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER

RUN cd /opt/conda/pdadmin4/jupyter-pgadmin-proxy && \
	pip install .
	
# python /opt/conda/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py
