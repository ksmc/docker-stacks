# Login mphanaenvacr
az login 
ARC_NAME = mphanaenvacr
az acr login -n $ARC_NAME

# build jupyter-k8s-hub
cd jupyter-k8s-hub
docker build -t $ARC_NAME.azurecr.io/k8s-hub:latest .
docker push $ARC_NAME.azurecr.io/k8s-hub:latest
cd ..

# build the base-notebook
cd base-notebook
docker build -t $ARC_NAME.azurecr.io/base-notebook:latest .
docker push $ARC_NAME.azurecr.io/base-notebook:latest
cd ..

# build the novnc-notebook
cd novnc-notebook
git clone --recurse-submodules --branch k8s-vdi https://github.com/zjiaksmc/docker-ubuntu-vnc-desktop.git
cd docker-ubuntu-vnc-desktop
docker build -t $ARC_NAME.azurecr.io/novnc-notebook:latest .
docker push $ARC_NAME.azurecr.io/novnc-notebook:latest
cd ..

# drived from base-notebook
cd r-notebook
docker build -t $ARC_NAME.azurecr.io/r-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/base-notebook:latest .
docker push $ARC_NAME.azurecr.io/r-notebook:latest
cd ..

cd scipy-notebook
docker build -t $ARC_NAME.azurecr.io/scipy-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/base-notebook:latest .
docker push $ARC_NAME.azurecr.io/scipy-notebook:latest
cd ..

cd openrefine-notebook
docker build -t $ARC_NAME.azurecr.io/openrefine-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/base-notebook:latest .
docker push $ARC_NAME.azurecr.io/openrefine-notebook:latest
cd ..

# drived from scipy-notebook & r-notebook
cd datascience-notebook
docker build -t $ARC_NAME.azurecr.io/datascience-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/scipy-notebook:latest .
docker push $ARC_NAME.azurecr.io/datascience-notebook:latest
cd ..

cd tensorflow-notebook
docker build -t $ARC_NAME.azurecr.io/tensorflow-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/scipy-notebook:latest .
docker push $ARC_NAME.azurecr.io/tensorflow-notebook:latest
cd ..

cd pyspark-notebook
docker build -t $ARC_NAME.azurecr.io/pyspark-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/scipy-notebook:latest .
docker push $ARC_NAME.azurecr.io/pyspark-notebook:latest
cd ..

cd rstudio-notebook
docker build -t $ARC_NAME.azurecr.io/rstudio-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/r-notebook:latest .
docker push $ARC_NAME.azurecr.io/rstudio-notebook:latest
cd ..

cd arcgis-notebook
docker build -t $ARC_NAME.azurecr.io/gis-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/scipy-notebook:latest .
docker push $ARC_NAME.azurecr.io/gis-notebook:latest
cd ..

cd sas-notebook
docker build -t $ARC_NAME.azurecr.io/sas-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/scipy-notebook:latest .
docker push $ARC_NAME.azurecr.io/sas-notebook:latest
cd ..

cd theia-notebook
docker build -t $ARC_NAME.azurecr.io/theia-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/scipy-notebook:latest .
docker push $ARC_NAME.azurecr.io/theia-notebook:latest
cd ..

# drived from pyspark-notebook
cd all-spark-notebook
docker build -t $ARC_NAME.azurecr.io/all-spark-notebook:latest --build-arg BASE_CONTAINER=$ARC_NAME.azurecr.io/pyspark-notebook:latest .
docker push $ARC_NAME.azurecr.io/all-spark-notebook:latest
cd ..









