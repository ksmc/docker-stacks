ARG BASE_CONTAINER=mphanaenvacr.azurecr.io/base-notebook:latest
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root
EXPOSE 5901

RUN apt-get update -q && \
	export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y --no-install-recommends wget curl rsync netcat mg vim bzip2 zip unzip && \
    apt-get install -y --no-install-recommends libx11-6 libxcb1 libxau6 && \
    apt-get install -y --no-install-recommends firefox net-tools lxde tightvncserver novnc supervisor xinit xterm xvfb dbus-x11 x11-utils && \
    apt-get install -y --no-install-recommends xfonts-base xfonts-75dpi xfonts-100dpi && \
    apt-get install -y --no-install-recommends python-pip python-dev python-qt4 && \
    apt-get install -y --no-install-recommends libssl-dev && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN mkdir -p /home/$NB_USER/.vnc
# COPY xstartup /home/$NB_USER/.vnc/
# RUN chmod a+x /home/$NB_USER/.vnc/xstartup
RUN touch /home/$NB_USER/.vnc/passwd
RUN /bin/bash -c "echo -e 'password\npassword\nn' | vncpasswd /home/$NB_USER/.vnc/passwd"
RUN chmod 400 /home/$NB_USER/.vnc/passwd
RUN chmod go-rwx /home/$NB_USER/.vnc
RUN touch /home/$NB_USER/.Xauthority

#COPY start-vncserver.sh /home/$NB_USER/
#RUN chmod a+x /home/$NB_USER/start-vncserver.sh

RUN echo "mycontainer" > /etc/hostname
RUN echo "127.0.0.1	localhost" > /etc/hosts
RUN echo "127.0.0.1	mycontainer" >> /etc/hosts

COPY cert.pem /home/$NB_USER
RUN chmod 644 /home/$NB_USER/cert.pem


   
USER $NB_USER
RUN wget https://github.com/novnc/websockify/archive/v0.9.0.tar.gz && tar -xvzf v0.9.0.tar.gz && cd websockify-0.9.0 && \
	python setup.py install && cd .. && rm -rf websockify-0.9.0

RUN pip install nbserverproxy==0.8.1 && \
	jupyter serverextension enable --py --sys-prefix nbserverproxy

RUN pip install git+https://github.com/ryanlovett/nbnovnc && \
	jupyter serverextension enable  --py --sys-prefix nbnovnc && \
	jupyter nbextension     install --py --sys-prefix nbnovnc && \
	jupyter nbextension     enable  --py --sys-prefix nbnovnc

	
COPY jupyter_notebook_config.py /etc/jupyter/
# COPY xinitrc /.xinitrc

# USER root

RUN fix-permissions $CONDA_DIR

USER root
RUN chmod +x /home/$NB_USER/.vnc/passwd
RUN chmod +x /home/$NB_USER/.vnc
RUN chown $NB_USER:$NB_GID /home/$NB_USER/.vnc
RUN chown $NB_USER:$NB_GID /home/$NB_USER/cert.pem
RUN echo /home/$NB_USER/.vnc/passwd
COPY .xinitrc /home/$NB_USER/
EXPOSE 8787
USER $NB_USER
# XPOSE 8080
