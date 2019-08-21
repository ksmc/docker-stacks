ARG BASE_CONTAINER=mphanaenvacr.azurecr.io/base-notebook:latest
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends ubuntu-desktop && \
    apt-get install -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal && \
    apt-get install -y tightvncserver && \
    mkdir /root/.vnc

RUN apt-get install -y --no-install-recommends \
	net-tools \
	novnc websockify supervisor xinit && \
    rm -rf /var/lib/apt/lists/*
    
USER $NB_USER

RUN pip install nbserverproxy==0.8.1 && \
	jupyter serverextension enable --py --sys-prefix nbserverproxy

RUN pip install git+https://github.com/ryanlovett/nbnovnc && \
	jupyter serverextension enable  --py --sys-prefix nbnovnc && \
	jupyter nbextension     install --py --sys-prefix nbnovnc && \
	jupyter nbextension     enable  --py --sys-prefix nbnovnc

	
COPY jupyter_notebook_config.py /etc/jupyter/

USER root

ADD xstartup /root/.vnc/xstartup
ADD passwd /root/.vnc/passwd

RUN chmod 600 /root/.vnc/passwd

RUN fix-permissions /etc/jupyter && \
	fix-permissions /usr/bin/vncserver

USER $NB_USER
ENV USER=$NB_USER
# CMD /usr/bin/vncserver :1 -geometry 1280x800 -depth 24 && tail -f /root/.vnc/*:1.log

EXPOSE 5901



