FROM jupyterhub/k8s-hub:0.8.2

USER root
RUN pip3 install --no-cache-dir -U \
    PyJWT \
    jupyterhub-dummyauthenticator

COPY jupyterhub/share/jupyterhub/static/images/mph-logo.svg /usr/local/share/jupyterhub/static/images/mph-logo.svg
COPY jupyterhub/share/jupyterhub/static/images/DataInsightsInitiative.png /usr/local/share/jupyterhub/static/images/DataInsightsInitiative.png
COPY jupyterhub/share/jupyterhub/static/css/style.min.css /usr/local/share/jupyterhub/static/css/style.min.css
COPY jupyterhub/share/jupyterhub/templates/spawn.html /usr/local/share/jupyterhub/templates/spawn.html
COPY jupyterhub/share/jupyterhub/templates/page.html /usr/local/share/jupyterhub/templates/page.html
COPY jupyterhub/jupyterhub/orm.py /usr/local/lib/python3.6/dist-packages/jupyterhub/orm.py

USER ${NB_USER}