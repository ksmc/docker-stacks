# drived from base-notebook
cd r-notebook
docker build -t mphanaenvacr.azurecr.io/r-notebook:latest .
docker push mphanaenvacr.azurecr.io/r-notebook:latest
cd ..

cd scipy-notebook
docker build -t mphanaenvacr.azurecr.io/scipy-notebook:latest .
docker push mphanaenvacr.azurecr.io/scipy-notebook:latest
cd ..

# drived from scipy-notebook & r-notebook
cd datascience-notebook
docker build -t mphanaenvacr.azurecr.io/datascience-notebook:latest .
docker push mphanaenvacr.azurecr.io/datascience-notebook:latest
cd ..

cd tensorflow-notebook
docker build -t mphanaenvacr.azurecr.io/tensorflow-notebook:latest .
docker push mphanaenvacr.azurecr.io/tensorflow-notebook:latest
cd ..

cd pyspark-notebook
docker build -t mphanaenvacr.azurecr.io/pyspark-notebook:latest .
docker push mphanaenvacr.azurecr.io/pyspark-notebook:latest
cd ..

cd rstudio-notebook
docker build -t mphanaenvacr.azurecr.io/rstudio-notebook:latest .
docker push mphanaenvacr.azurecr.io/rstudio-notebook:latest
cd ..

# drived from pyspark-notebook
cd all-spark-notebook
docker build -t mphanaenvacr.azurecr.io/all-spark-notebook:latest .
docker push mphanaenvacr.azurecr.io/all-spark-notebook:latest
cd ..




