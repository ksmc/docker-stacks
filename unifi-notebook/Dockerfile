# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root

# ffmpeg for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

# Increase JavaScript heap memory
ENV NODE_OPTIONS=--max-old-space-size=16000

# Install facets which does not have a pip or conda package at the moment
RUN cd /tmp && \
    git clone https://github.com/PAIR-code/facets.git && \
    cd facets && \
    jupyter nbextension install facets-dist/ --sys-prefix && \
    cd && \
    pip install facets-overview && \
    rm -rf /tmp/facets && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Install Python 3 packages
RUN conda install --quiet --yes \
    'beautifulsoup4=4.8.*' \
    'conda-forge::blas=*=openblas' \
    'bokeh=1.3*' \
    'cloudpickle=1.2*' \
    'cython=0.29*' \
    'dask=2.2.*' \
    'dill=0.3*' \
    'h5py=2.9*' \
    'hdf5=1.10*' \
    'ipywidgets=7.5*' \
    'matplotlib-base=3.1.*' \
    'numba=0.45*' \
    'numexpr=2.6*' \
    'pandas=1.1*' \
    'patsy=0.5*' \
    'protobuf=3.9.*' \
    'scikit-image=0.15*' \
    'scikit-learn=0.21*' \
    'scipy=1.3*' \
    'seaborn=0.9*' \
    'sqlalchemy=1.3*' \
    'statsmodels=0.10*' \
    'sympy=1.4*' \
    'vincent=0.4.*' \
    'dash=1.8.*' \
    'xlrd' \
    'ipython-sql' && \
    pip install jupyterlab_sql==0.3.0 && \
    pip install jupyterlab-git==0.8.1 && \
    pip install jupyterlab_iframe && \
    conda clean --all -f -y && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    jupyter serverextension enable jupyterlab_sql --py --sys-prefix && \
	jupyter serverextension enable jupyterlab_git --py --sys-prefix && \
	jupyter serverextension enable jupyterlab_iframe --py  --sys-prefix && \
    # Also activate ipywidgets extension for JupyterLab
    # Check this URL for most recent compatibilities
    # https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@^1.0.1 --no-build && \
    jupyter labextension install jupyterlab_bokeh@1.0.0 --no-build && \
    jupyter labextension install @jupyterlab/dataregistry-extension --no-build && \
    jupyter labextension install jupyterlab_voyager --no-build && \
	jupyter labextension install @jupyterlab/git --no-build && \
	jupyter labextension install jupyterlab_iframe --no-build && \
    jupyter lab build && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER

USER root
# R pre-requisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    unixodbc \
    unixodbc-dev \
    r-cran-rodbc \
    gfortran \
    gcc && \
    rm -rf /var/lib/apt/lists/*

# Fix for devtools https://github.com/conda-forge/r-devtools-feedstock/issues/4
RUN ln -s /bin/tar /bin/gtar

USER $NB_USER

# R packages
RUN conda install --quiet --yes \
    'r-flexdashboard' \
    'r-shinydashboard' \
    'r-base=3.6.1' \
    'r-caret=6.0*' \
    'r-crayon=1.3*' \
    'r-devtools=2.1*' \
    'r-forecast=8.7*' \
    'r-hexbin=1.27*' \
    'r-htmltools=0.3*' \
    'r-htmlwidgets=1.3*' \
    'r-irkernel=1.0*' \
    'r-nycflights13=1.0*' \
    'r-plyr=1.8*' \
    'r-randomforest=4.6*' \
    'r-rcurl=1.95*' \
    'r-reshape2=1.4*' \
    'r-rmarkdown=1.14*' \
    'r-rsqlite=2.1*' \
    'r-shiny=1.3*' \
    'r-sparklyr=1.0*' \
    'r-tidyverse=1.2*' \
    'rpy2=2.9*' \
    'r-ggplot2' \
    'r-usmap' \
    'r-dplyr' \
    'r-rjson' \
    'r-tm' \
    'r-ggmap' \
    'r-maps' \
    'r-mapdata' \
    'r-hexbin' && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR

# Install e1071 R package (dependency of the caret R package)
RUN conda install --quiet --yes r-e1071

# Install from conda-forge
RUN conda install --quiet --yes -c conda-forge r-qdaptools r-qdapregex

# Install Ployly
RUN conda install -c plotly plotly=4.1.0 && \
	conda install -c plotly plotly-geo=1.0.0 && \
	conda install -c conda-forge colorlover r-plotly && \
	jupyter labextension install @jupyterlab/plotly-extension --no-build && \
	jupyter labextension install jupyterlab-chart-editor --no-build && \ 
	jupyter lab build && \
	npm cache clean --force && \
	rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN conda install --quiet --yes -c r r-rjava r-xlsxjars r-xlsx r-venneuler r-opennlpdata

ENV LD_LIBRARY_PATH=/opt/conda/lib/server

RUN R CMD javareconf -e && \
    R -e 'install.packages("openNLP", repos = "http://cran.us.r-project.org")' && \
    R -e 'install.packages("qdap", repos = "http://cran.us.r-project.org")'

# Install CoLab
RUN conda install --quiet --yes \
    'r-appliedpredictivemodeling' \
    'r-broom' \
    'r-nycflights13' \
    'r-car' \
    'r-corrplot' \
    'r-e1071' \
    'r-factoextra' \
    'r-ggplot2' \
    'r-randomforest' \
    'r-rpart' \
    'r-snowballc' \
    'r-visnetwork' \
    'r-ggmap' \
    'r-maps' \
    'r-mapdata' \
    'r-wordcloud' && \
    conda clean --all -f -y && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN conda install -c pdiakumis --quiet --yes \
    'r-rock' && \
    conda clean --all -f -y && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

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

# install jupyter-server-proxy extension
RUN conda install -yq -c conda-forge 'jupyter-server-proxy=1.2.*' 'jupyter-rsession-proxy=1.2*' && \
    conda clean -tipsy && \
    jupyter labextension install @jupyterlab/server-proxy

# RUN conda install --quiet --yes -c conda-forge -c anaconda cookiecutter nodejs

# USER root
# COPY rstudio-launcher /opt/conda/rstudio-launcher
# RUN chown -R jovyan:users /opt/conda/rstudio-launcher

# USER $NB_USER
# RUN cd /opt/conda/rstudio-launcher && jlpm install && jupyter labextension install .

