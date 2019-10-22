# Login mphjphk8sacr
az login 
az acr login -n mphjphk8sacr

# build jupyter-k8s-hub
cd jupyter-k8s-hub
docker build -t mphjphk8sacr.azurecr.io/k8s-hub:latest .
docker push mphjphk8sacr.azurecr.io/k8s-hub:latest
cd ..

# build the base-notebook
cd base-notebook
docker build -t mphjphk8sacr.azurecr.io/base-notebook:latest .
docker push mphjphk8sacr.azurecr.io/base-notebook:latest
cd ..

# drived from base-notebook
cd r-notebook
docker build -t mphjphk8sacr.azurecr.io/r-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/base-notebook:latest .
docker push mphjphk8sacr.azurecr.io/r-notebook:latest
cd ..

cd scipy-notebook
docker build -t mphjphk8sacr.azurecr.io/scipy-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/base-notebook:latest .
docker push mphjphk8sacr.azurecr.io/scipy-notebook:latest
cd ..

cd openrefine-notebook
docker build -t mphjphk8sacr.azurecr.io/openrefine-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/base-notebook:latest .
docker push mphjphk8sacr.azurecr.io/openrefine-notebook:latest
cd ..

# drived from scipy-notebook & r-notebook
cd datascience-notebook
docker build -t mphjphk8sacr.azurecr.io/datascience-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/scipy-notebook:latest .
docker push mphjphk8sacr.azurecr.io/datascience-notebook:latest
cd ..

cd tensorflow-notebook
docker build -t mphjphk8sacr.azurecr.io/tensorflow-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/scipy-notebook:latest .
docker push mphjphk8sacr.azurecr.io/tensorflow-notebook:latest
cd ..

cd pyspark-notebook
docker build -t mphjphk8sacr.azurecr.io/pyspark-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/scipy-notebook:latest .
docker push mphjphk8sacr.azurecr.io/pyspark-notebook:latest
cd ..

cd rstudio-notebook
docker build -t mphjphk8sacr.azurecr.io/rstudio-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/r-notebook:latest .
docker push mphjphk8sacr.azurecr.io/rstudio-notebook:latest
cd ..

cd arcgis-notebook
docker build -t mphjphk8sacr.azurecr.io/gis-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/scipy-notebook:latest .
docker push mphjphk8sacr.azurecr.io/gis-notebook:latest
cd ..

cd sas-notebook
docker build -t mphjphk8sacr.azurecr.io/sas-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/scipy-notebook:latest .
docker push mphjphk8sacr.azurecr.io/sas-notebook:latest
cd ..

cd theia-notebook
docker build -t mphjphk8sacr.azurecr.io/theia-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/scipy-notebook:latest .
docker push mphjphk8sacr.azurecr.io/theia-notebook:latest
cd ..

# drived from pyspark-notebook
cd all-spark-notebook
docker build -t mphjphk8sacr.azurecr.io/all-spark-notebook:latest --build-arg BASE_CONTAINER=mphjphk8sacr.azurecr.io/pyspark-notebook:latest .
docker push mphjphk8sacr.azurecr.io/all-spark-notebook:latest
cd ..
