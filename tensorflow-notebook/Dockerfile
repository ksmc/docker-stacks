# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

RUN pip install biopython fasttext sentencepiece

RUN conda install --quiet --yes -c conda-forge \
    'nltk' \
    'seaborn' \
    'tensorflow=1.13*' \
    'keras=2.2*' && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# RUN python -m nltk.downloader -d /opt/conda/share/nltk_data all && \
#     fix-permissions $CONDA_DIR


