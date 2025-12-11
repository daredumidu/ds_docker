Step1: create the initial base image.

follow instrctions on "https://hub.docker.com/_/httpd" for creating the SSL/https base image. 

Use "dockerfile-bk" to create the base image (rename as required)
~~~
docker build -t [image-name] .
~~~

Step2: use the initial image to host the webpage. Use the "container_build_compose.py" file to create the updated image.

Use "dockerfile" and "docker-compose.yaml" to create the container
