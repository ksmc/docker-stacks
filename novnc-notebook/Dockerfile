ARG BASE_CONTAINER
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root
RUN apt-get update -q && \
	export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y --no-install-recommends wget curl rsync netcat mg vim bzip2 zip unzip && \
    apt-get install -y --no-install-recommends libx11-6 libxcb1 libxau6 && \
    apt-get install -y --no-install-recommends firefox net-tools supervisor lxde tightvncserver novnc nginx xinit xterm xvfb dbus-x11 x11-utils && \
    apt-get install -y --no-install-recommends xfonts-base xfonts-75dpi xfonts-100dpi && \
    apt-get install -y --no-install-recommends python-pip python-dev python-qt4 && \
    apt-get install -y --no-install-recommends libssl-dev && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#RUN apt-get update -q && \
#	export DEBIAN_FRONTEND=noninteractive && \
#  	apt-get install -y --no-install-recommends snapd \
#   	novnc \
#	tigervnc-standalone-server \
#	xfonts-base \
#	xterm \
#	xfce4 \
#	supervisor \
#	x11-xserver-utils \
#	xinit && \
#	apt-get autoclean -y && \
#   apt-get autoremove -y && \
#    apt-get clean && \
#   rm -rf /var/lib/apt/lists/*

#RUN wget https://github.com/novnc/websockify/archive/v0.9.0.tar.gz && tar -xvzf v0.9.0.tar.gz && cd websockify-0.9.0 && \
#	python setup.py install && cd .. && rm -rf websockify-0.9.0

#RUN git clone https://github.com/novnc/websockify.git && \
#	cd websockify && \
#	python setup.py install 

USER $NB_USER
RUN conda install jupyter-server-proxy -c conda-forge
RUN pip install git+https://github.com/novnc/websockify@master

# RUN pip install git+https://github.com/ryanlovett/nbnovnc@master

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
