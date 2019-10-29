# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=mphanaenvacr.azurecr.io/scipy-notebook:latest
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# Install Dependencies
USER root    
RUN apt-get update && apt-get install -y \
	build-essential \
	libssl-dev \
	libffi-dev \
	libgmp3-dev \
	virtualenv \
	python-pip \
	libpq-dev \
	python-dev \
	postgresql

USER $NB_USER 
RUN conda install --quiet --yes \
	'dask=2.3.*' && \
	fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER	
	
RUN pip install \
	gunicorn \
	psycopg2 \
	jupyter-server-proxy && \
	#jupyter labextension install jupyterlab-server-proxy --no-build && \
	#jupyter lab build --source-build=True && \
    #npm cache clean --force && \
    #rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    #rm -rf /home/$NB_USER/.cache/yarn && \
    #rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
	
RUN cd $CONDA_DIR && \
	mkdir pgadmin4 && \
	cd pgadmin4 && \
	wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.1/pip/pgadmin4-4.1-py2.py3-none-any.whl && \
	pip install pgadmin4-4.1-py2.py3-none-any.whl && \
	mkdir -p /home/$NB_USER/.jupyter/
	
ADD config_local.py /opt/conda/lib/python3.7/site-packages/pgadmin4
ADD jupyter_notebook_config.py /home/$NB_USER/.jupyter
ADD postgresql-logo.svg /home/$NB_USER/.jupyter

USER root
RUN chown -R jovyan:users /opt/conda/lib/python3.7/site-packages/pgadmin4 && \
	chown -R jovyan:users /home/$NB_USER

USER $NB_USER 	
ENV PGADMIN_SETUP_EMAIL=jovyan@localhost PGADMIN_SETUP_PASSWORD=secret
RUN python /opt/conda/lib/python3.7/site-packages/pgadmin4/setup.py && \
	fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER

#RUN cd /opt/conda/pdadmin4/jupyter-pgadmin-proxy && \
#	pip install .
	
# python /opt/conda/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py
