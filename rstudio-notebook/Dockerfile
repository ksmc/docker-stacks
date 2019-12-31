# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER
FROM $BASE_CONTAINER

# install nbrsessionproxy extension
RUN conda install -yq -c conda-forge nbrsessionproxy && \
    conda clean -tipsy

# install rstudio-server
USER root
RUN apt-get update && \
    curl --silent -L --fail https://download2.rstudio.org/rstudio-server-1.1.419-amd64.deb > /tmp/rstudio.deb && \
    echo '24cd11f0405d8372b4168fc9956e0386 /tmp/rstudio.deb' | md5sum -c - && \
    apt-get install -y /tmp/rstudio.deb && \
    rm /tmp/rstudio.deb && \
    apt-get clean
ENV PATH=$PATH:/usr/lib/rstudio-server/bin

RUN mkdir /etc/rstudio/user-settings -p
ADD user-settings /etc/rstudio/user-settings/user-settings
ADD config-rstudio.sh /etc/rstudio/config-rstudio.sh
RUN fix-permissions /etc/rstudio/

USER $NB_USER