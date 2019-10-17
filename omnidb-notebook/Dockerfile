# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=mphanaenvacr.azurecr.io/base-notebook:latest
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# Install OMNIDB
USER root
ENV OMNIDB_VERSION=2.16.0
    
RUN apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y wget dumb-init \
  && if [ ! -e '/bin/systemctl' ]; then ln -s /bin/echo /bin/systemctl; fi \
  && rm -rf /var/lib/apt/lists/*

#RUN wget -q https://omnidb.org/dist/${OMNIDB_VERSION}/omnidb-server_${OMNIDB_VERSION}-debian-amd64.deb && \
#	dpkg -i omnidb-server_${OMNIDB_VERSION}-debian-amd64.deb && \
#	rm -rf omnidb-server_${OMNIDB_VERSION}-debian-amd64.deb

COPY jupyter-omnidb-proxy /opt/conda/omnidb/jupyter-omnidb-proxy
COPY OmniDB  /opt/conda/omnidb/OmniDB
RUN chown -R jovyan:users /opt/conda/omnidb && \
	fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER

USER $NB_USER
RUN conda install -yq jupyter-server-proxy -c conda-forge && \
    conda clean -tipsy

RUN pip install -r /opt/conda/omnidb/OmniDB/requirements.txt
 	
RUN cd /opt/conda/omnidb/jupyter-omnidb-proxy && \
	pip install . && \
	fix-permissions $CONDA_DIR && \
	fix-permissions /home/$NB_USER


#ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]
#CMD ["omnidb-server", "-H", "0.0.0.0"]