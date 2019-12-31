# Login mphanaenvacr
az login 
az acr login -n uindyanaenvacr

# build jupyter-k8s-hub
cd jupyter-k8s-hub
docker build -t uindyanaenvacr.azurecr.io/k8s-hub:latest .
docker push uindyanaenvacr.azurecr.io/k8s-hub:latest
cd ..

# drived from base-notebook
cd r-notebook
docker build -t uindyanaenvacr.azurecr.io/r-notebook:latest --build-arg BASE_CONTAINER=jupyter/minimal-notebook:latest .
docker push uindyanaenvacr.azurecr.io/r-notebook:latest
cd ..

cd scipy-notebook
docker build -t uindyanaenvacr.azurecr.io/scipy-notebook:latest --build-arg BASE_CONTAINER=jupyter/minimal-notebook:latest .
docker push uindyanaenvacr.azurecr.io/scipy-notebook:latest
cd ..

# drived from scipy-notebook & r-notebook
cd datascience-notebook
docker build -t uindyanaenvacr.azurecr.io/datascience-notebook:latest --build-arg BASE_CONTAINER=uindyanaenvacr.azurecr.io/scipy-notebook:latest .
docker push uindyanaenvacr.azurecr.io/datascience-notebook:latest
cd ..

cd rstudio-notebook
docker build -t uindyanaenvacr.azurecr.io/rstudio-notebook:latest --build-arg BASE_CONTAINER=uindyanaenvacr.azurecr.io/r-notebook:latest .
docker push uindyanaenvacr.azurecr.io/rstudio-notebook:latest
cd ..
