# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER
FROM $BASE_CONTAINER

USER root
RUN apt-get update && \
	apt-get install -y --no-install-recommends curl \
	gnupg2

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
	echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list && \
	apt-get update && apt-get install -y yarn
	
# install jupyter-server-proxy extension
RUN conda install -yq jupyter-server-proxy -c conda-forge && \
    conda clean -tipsy && \
    pip install jupyter-theia-proxy && \
    fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER

ADD package.json /home/$NB_USER/package.json
RUN cd /home/$NB_USER && yarn
COPY theia_jupyterhub_patch/vscode-uri/lib/esm/index.js /home/$NB_USER/node_modules/vscode-uri/lib/esm/index.js
COPY theia_jupyterhub_patch/@theia/core/lib/browser/messaging/ws-connection-provider.js /home/$NB_USER/node_modules/@theia/core/lib/browser/messaging/ws-connection-provider.js
RUN cd /home/$NB_USER && \	
	yarn theia build

COPY __init__.py /opt/conda/lib/python3.7/site-packages/jupyter_theia_proxy/__init__.py
ENV PATH=$PATH:/home/$NB_USER/node_modules/.bin
 	 
USER $NB_USER
