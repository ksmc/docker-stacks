ARG BASE_CONTAINER=mphanaenvacr.azurecr.io/base-notebook:latest
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
	net-tools \
	tightvncserver novnc websockify supervisor xinit && \
    rm -rf /var/lib/apt/lists/*
    
USER $NB_USER

RUN pip install nbserverproxy==0.8.1 && \
	jupyter serverextension enable --py --sys-prefix nbserverproxy

RUN pip install git+https://github.com/ryanlovett/nbnovnc && \
	jupyter serverextension enable  --py --sys-prefix nbnovnc && \
	jupyter nbextension     install --py --sys-prefix nbnovnc && \
	jupyter nbextension     enable  --py --sys-prefix nbnovnc

	
COPY jupyter_notebook_config.py /etc/jupyter/
# COPY xinitrc /.xinitrc

# USER root

RUN fix-permissions /etc/jupyter && \
	fix-permissions $CONDA_DIR

# XPOSE 8080




