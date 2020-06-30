# Login mphanaenvacr
az login 
az acr login -n zus2fssacrdev

# build jupyter-k8s-hub
cd jupyter-k8s-hub
docker build -t zus2fssacrdev.azurecr.io/k8s-hub:latest .
docker push zus2fssacrdev.azurecr.io/k8s-hub:latest
cd ..

cd scipy-notebook
docker build -t zus2fssacrdev.azurecr.io/scipy-notebook:latest --build-arg BASE_CONTAINER=jupyter/minimal-notebook:latest .
docker push zus2fssacrdev.azurecr.io/scipy-notebook:latest
cd ..

# drived from scipy-notebook & r-notebook
cd datascience-notebook
docker build -t zus2fssacrdev.azurecr.io/datascience-notebook:latest --build-arg BASE_CONTAINER=zus2fssacrdev.azurecr.io/scipy-notebook:latest .
docker push zus2fssacrdev.azurecr.io/datascience-notebook:latest
cd ..

cd tensorflow-notebook
docker build -t zus2fssacrdev.azurecr.io/tensorflow-notebook:latest --build-arg BASE_CONTAINER=zus2fssacrdev.azurecr.io/scipy-notebook:latest .
docker push zus2fssacrdev.azurecr.io/tensorflow-notebook:latest
cd ..
