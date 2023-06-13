#!/bin/bash
docker stop my_fastapi
docker rm my_fastapi
docker run -d --name my_fastapi -p 8089:80 microwave88/fastapi:v1.0
