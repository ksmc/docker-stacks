# Login novncacr
az login 
ACR_NAME=novncacr
az acr login -n $ACR_NAME

# build jupyter-k8s-hub
cd jupyter-k8s-hub
docker build -t $ACR_NAME.azurecr.io/k8s-hub:latest .
docker push $ACR_NAME.azurecr.io/k8s-hub:latest
cd ..

# build the novnc-desktop
cd docker-ubuntu-vnc-desktop
docker build -t $ACR_NAME.azurecr.io/novnc-notebook:latest .
docker push $ACR_NAME.azurecr.io/novnc-notebook:latest
cd ..

# build the base-notebook
cd base-notebook
docker build -t $ACR_NAME.azurecr.io/base-notebook:latest .
docker push $ACR_NAME.azurecr.io/base-notebook:latest
cd ..

# drived from base-notebook
cd scipy-notebook
docker build -t $ACR_NAME.azurecr.io/scipy-notebook:latest --build-arg BASE_CONTAINER=$ACR_NAME.azurecr.io/base-notebook:latest .
docker push $ACR_NAME.azurecr.io/scipy-notebook:latest
cd ..

# drived from scipy-notebook
cd datascience-notebook
docker build -t $ACR_NAME.azurecr.io/datascience-notebook:latest --build-arg BASE_CONTAINER=$ACR_NAME.azurecr.io/scipy-notebook:latest .
docker push $ACR_NAME.azurecr.io/datascience-notebook:latest
cd ..

cd tensorflow-notebook
docker build -t $ACR_NAME.azurecr.io/tensorflow-notebook:latest --build-arg BASE_CONTAINER=$ACR_NAME.azurecr.io/scipy-notebook:latest .
docker push $ACR_NAME.azurecr.io/tensorflow-notebook:latest
cd ..

cd pyspark-notebook
docker build -t $ACR_NAME.azurecr.io/pyspark-notebook:latest --build-arg BASE_CONTAINER=$ACR_NAME.azurecr.io/scipy-notebook:latest .
docker push $ACR_NAME.azurecr.io/pyspark-notebook:latest
cd ..

cd arcgis-notebook
docker build -t $ACR_NAME.azurecr.io/gis-notebook:latest --build-arg BASE_CONTAINER=$ACR_NAME.azurecr.io/scipy-notebook:latest .
docker push $ACR_NAME.azurecr.io/gis-notebook:latest
cd ..

# drived from pyspark-notebook
cd all-spark-notebook
docker build -t $ACR_NAME.azurecr.io/all-spark-notebook:latest --build-arg BASE_CONTAINER=$ACR_NAME.azurecr.io/pyspark-notebook:latest .
docker push $ACR_NAME.azurecr.io/all-spark-notebook:latest
cd ..

# vscode image
cd theia-vscode
docker build -t $ACR_NAME.azurecr.io/theia-vscode:latest .
docker push $ACR_NAME.azurecr.io/theia-vscode:latest
cd ..









