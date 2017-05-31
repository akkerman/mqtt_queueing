FROM python:3.5-alpine
MAINTAINER Marcel Akkerman <MarcelAkkerman@creetion.com>
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
