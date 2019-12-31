## Copyright (c) Jupyter Development Team.
## Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=uindyanaenvacr.azurecr.io/datascience-notebook:latest
FROM $BASE_CONTAINER

USER $NB_USER

## Install django and its dependencies
RUN pip install Django

USER root

## Copy pilot webapp 
ADD uindy_pilot /home/$NB_USER/uindy_pilot

COPY jupyter-pilot-proxy /opt/conda/pilot/jupyter-pilot-proxy
RUN chown -R jovyan:users /opt/conda/pilot && \
	fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER

USER $NB_USER
RUN cd /opt/conda/pilot/jupyter-pilot-proxy && \
	pip install . && \
	cd /home/$NB_USER/uindy_pilot && \
	pip install -r requirements.txt && \
	fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER

