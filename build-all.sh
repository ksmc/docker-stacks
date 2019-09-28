# Login sandboxmphanaenvacr 
az acr login -n sandboxmphanaenvacr

# build jupyter-k8s-hub
cd jupyter-k8s-hub
docker build -t sandboxmphanaenvacr.azurecr.io/k8s-hub:latest .
docker push sandboxmphanaenvacr.azurecr.io/k8s-hub:latest
cd ..

# build the base-notebook
cd base-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/base-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/base-notebook:latest
cd ..

# drived from base-notebook
cd r-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/r-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/r-notebook:latest
cd ..

cd scipy-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/scipy-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/scipy-notebook:latest
cd ..

# drived from scipy-notebook & r-notebook
cd datascience-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/datascience-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/datascience-notebook:latest
cd ..

cd tensorflow-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/tensorflow-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/tensorflow-notebook:latest
cd ..

cd pyspark-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/pyspark-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/pyspark-notebook:latest
cd ..

cd rstudio-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/rstudio-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/rstudio-notebook:latest
cd ..

cd arcgis-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/gis-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/gis-notebook:latest
cd ..

cd sas-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/sas-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/sas-notebook:latest
cd ..

# drived from pyspark-notebook
cd all-spark-notebook
docker build -t sandboxmphanaenvacr.azurecr.io/all-spark-notebook:latest .
docker push sandboxmphanaenvacr.azurecr.io/all-spark-notebook:latest
cd ..




