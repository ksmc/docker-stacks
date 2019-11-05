# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=mphddapracr.azurecr.io/scipy-notebook-gpu:latest
FROM $BASE_CONTAINER

LABEL maintainer="Emmanuel Benazera <emmanuel.benazera@jolibrain.com>"

# Install Tensorflow
RUN conda install --quiet --yes \
    'tensorflow-gpu=1.14*' \
    'keras=2.2*' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN pip install --pre jupyter-tensorboard && \
	jupyter serverextension enable jupyter_tensorboard --py --sys-prefix && \
	jupyter nbextension enable jupyter_tensorboard --py --sys-prefix && \
    jupyter labextension install jupyterlab_tensorboard --no-build && \
    jupyter lab build --source-build=True && \
    conda clean --all -f -y && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Allow drivers installed by the nvidia-driver-installer to be located
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64
# Also, utilities like `nvidia-smi` are installed here
ENV PATH=${PATH}:/usr/local/nvidia/bin:/usr/local/cuda/bin