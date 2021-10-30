FROM python:3.9

#runs command from this dir (sorta like cd), expose port 5000
WORKDIR /flask_cache
EXPOSE 5000

#copy requirements.txt to image in dir
COPY requirements.txt /flask_cache

#install the dependencies
RUN pip3 install -r requirements.txt --no-cache-dir

#copy all from workdir to image
COPY . .
