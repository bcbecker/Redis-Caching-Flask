FROM python:3.9

#makes sure pip is up to date
RUN /usr/local/bin/python -m pip install --upgrade pip

#creates/runs command from this dir
WORKDIR /dockerized_flask_cache

#copy contents of flask_cache dir to workdir
COPY flask_cache/. ./

#install the dependencies
RUN pip install -r ./requirements.txt

#expose port 5000
EXPOSE 5000