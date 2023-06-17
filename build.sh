#!/bin/bash
docker stop my_fastapi
docker rm my_fastapi
docker rmi microwave88/fastapi:v1.1
docker build -t microwave88/fastapi:v1.1 .
docker run -d --name my_fastapi -p 8089:80 microwave88/fastapi:v1.1
