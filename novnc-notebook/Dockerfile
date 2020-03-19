# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/base-notebook:latest
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root
RUN apt-get update -q && \
	export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y --no-install-recommends wget curl rsync netcat mg vim bzip2 zip unzip git && \
    apt-get install -y --no-install-recommends libx11-6 libxcb1 libxau6 && \
    apt-get install -y --no-install-recommends firefox net-tools supervisor lxde tightvncserver novnc nginx xinit xterm xvfb dbus-x11 x11-utils && \
    apt-get install -y --no-install-recommends xfonts-base xfonts-75dpi xfonts-100dpi && \
    apt-get install -y --no-install-recommends python-pip python-dev python-qt4 && \
    apt-get install -y --no-install-recommends libssl-dev && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER
RUN conda install jupyter-server-proxy -c conda-forge
RUN pip install git+https://github.com/novnc/websockify@master

COPY nbnovnc /opt/conda/nbnovnc
RUN cd /opt/conda/nbnovnc && \
	pip install .

RUN jupyter serverextension enable  --py --sys-prefix nbnovnc && \
	jupyter nbextension     install --py --sys-prefix nbnovnc && \
	jupyter nbextension     enable  --py --sys-prefix nbnovnc
	
COPY jupyter_notebook_config.py /etc/jupyter/
COPY nbnovnc/nbnovnc/handlers.py /opt/conda/lib/python3.7/site-packages/nbnovnc/handlers.py

USER root
RUN fix-permissions $CONDA_DIR
USER $NB_USER