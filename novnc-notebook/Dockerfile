ARG BASE_CONTAINER=mphanaenvacr.azurecr.io/base-notebook:latest
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root
EXPOSE 5901

RUN apt-get update -q && \
	export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y --no-install-recommends wget curl rsync netcat mg vim bzip2 zip unzip && \
    apt-get install -y --no-install-recommends libx11-6 libxcb1 libxau6 && \
    apt-get install -y --no-install-recommends firefox net-tools lxde tightvncserver novnc nginx xinit xterm xvfb dbus-x11 x11-utils && \
    apt-get install -y --no-install-recommends xfonts-base xfonts-75dpi xfonts-100dpi && \
    apt-get install -y --no-install-recommends python-pip python-dev python-qt4 && \
    apt-get install -y --no-install-recommends libssl-dev && \
    pip install supervisor && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


#RUN mkdir -p /home/$NB_USER/.vnc
#RUN touch /home/$NB_USER/.vnc/passwd
#RUN /bin/bash -c "echo -e 'password\npassword\nn' | vncpasswd /home/$NB_USER/.vnc/passwd"
#RUN chmod 400 /home/$NB_USER/.vnc/passwd
#RUN chmod go-rwx /home/$NB_USER/.vnc
#RUN touch /home/$NB_USER/.Xauthority

RUN echo "mycontainer" > /etc/hostname
RUN echo "127.0.0.1	localhost" > /etc/hosts
RUN echo "127.0.0.1	mycontainer" >> /etc/hosts
   
USER $NB_USER

RUN wget https://github.com/novnc/websockify/archive/v0.9.0.tar.gz && tar -xvzf v0.9.0.tar.gz && cd websockify-0.9.0 && \
	python setup.py install && cd .. && rm -rf websockify-0.9.0

#RUN	cd /tmp && \
#	git clone https://github.com/ksmc/nbnovnc.git && \
#	cd nbnovnc && \
#	git checkout develop && \
#	pip install . 

RUN pip install git+https://github.com/ryanlovett/nbnovnc

RUN jupyter serverextension enable  --py --sys-prefix nbnovnc && \
	jupyter nbextension     install --py --sys-prefix nbnovnc && \
	jupyter nbextension     enable  --py --sys-prefix nbnovnc
	
COPY jupyter_notebook_config.py /etc/jupyter/
COPY jupyter-server-proxy/nbserverproxy/handlers.py /opt/conda/lib/python3.7/site-packages/nbserverproxy/handlers.py
COPY nbnovnc/nbnovnc/handlers.py /opt/conda/lib/python3.7/site-packages/nbnovnc/handlers.py

#COPY .ky /home/$NB_USER
#RUN chmod 644 /home/$NB_USER/.kv
#RUN chown $NB_USER:$NB_GID /home/$NB_USER/.kv

USER root
RUN fix-permissions $CONDA_DIR
#RUN chmod +x /home/$NB_USER/.vnc/passwd
#RUN chmod +x /home/$NB_USER/.vnc
#RUN chown $NB_USER:$NB_GID /home/$NB_USER/.vnc
#RUN echo /home/$NB_USER/.vnc/passwd
COPY .xinitrc /home/$NB_USER/

COPY default /etc/nginx/sites-enabled/default
RUN chown -R $NB_USER:$NB_GID /var/log/nginx
RUN chown -R $NB_USER:$NB_GID /var/lib/nginx
RUN chown -R $NB_USER:$NB_GID /run
RUN chown -R $NB_USER:$NB_GID /etc/nginx

EXPOSE 6081
USER $NB_USER
