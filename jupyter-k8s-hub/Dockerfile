FROM jupyterhub/k8s-hub:0.8.2

USER root
RUN pip3 install --no-cache-dir -U \
    PyJWT

COPY jupyterhub/share/jupyterhub/static/images/hhs-logo.png /usr/local/share/jupyterhub/static/images/hhs-logo.png
COPY jupyterhub/share/jupyterhub/static/images/mph-logo.svg /usr/local/share/jupyterhub/static/images/mph-logo.svg
COPY jupyterhub/share/jupyterhub/static/css/style.min.css /usr/local/share/jupyterhub/static/css/style.min.css
#COPY jupyterhub/share/jupyterhub/static/js/home.js /usr/local/share/jupyterhub/static/js/home.js
COPY jupyterhub/share/jupyterhub/templates/spawn.html /usr/local/share/jupyterhub/templates/spawn.html
COPY jupyterhub/share/jupyterhub/templates/page.html /usr/local/share/jupyterhub/templates/page.html
#COPY jupyterhub/share/jupyterhub/templates/home.html /usr/local/share/jupyterhub/templates/home.html
COPY jupyterhub/jupyterhub/orm.py /usr/local/lib/python3.6/dist-packages/jupyterhub/orm.py
#COPY jupyterhub/jupyterhub/user.py /usr/local/lib/python3.6/dist-packages/jupyterhub/user.py
#COPY jupyterhub/jupyterhub/handlers/pages.py /usr/local/lib/python3.6/dist-packages/jupyterhub/handlers/pages.py

USER ${NB_USER}