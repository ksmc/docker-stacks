FROM jupyterhub/k8s-hub:0.8.2

USER root
RUN pip3 install --no-cache-dir -U \
    PyJWT

COPY static/images/ksmc-logo-300x78.png /usr/local/share/jupyterhub/static/images/ksmc-logo-300x78.png
COPY static/css/style.min.css /usr/local/share/jupyterhub/static/css/style.min.css
COPY templates/spawn.html /usr/local/share/jupyterhub/templates/spawn.html
COPY jupyterhub/jupyterhub/orm.py /usr/local/lib/python3.6/dist-packages/jupyterhub/orm.py

USER ${NB_USER}