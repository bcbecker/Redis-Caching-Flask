# Redis-Caching-Flask
Dockerized app using a simple cache (Redis), querying the hipolabs universities API (https://github.com/Hipo/university-domains-list-api), which allows us to search with a country parameter and get back a JSON response of all the universities in that country.


## Setup
Ensure you have docker installed.
```bash
docker --version
```

Create the .env file in the flask_cache dir
```bash
cd flask_cache
touch .env
```

These are the .env variables, if your host/port/url etc vary, change it accordingly. Note that your CACHE_REDIS_HOST will be the name of your service as defined in the docker-compose file, not localhost.
```bash
CACHE_TYPE=redis
CACHE_REDIS_HOST=redis
CACHE_REDIS_PORT=6379
CACHE_REDIS_DB=0
CACHE_REDIS_URL=redis://redis:6379/0
CACHE_DEFAULT_TIMEOUT=500
```

Start the docker daemon and build the containers (sudo if Linux). You may not need to use sudo, or start the daemon, depending on your configuration
```bash
sudo dockerd
sudo docker-compose up -d --build
```

To ensure everything is up and running, run docker ps
```bash
sudo docker ps
```

You can start/stop containers using the following:
```bash
sudo docker container <start/stop> <container-name>
```

Or, stop and remove running containers with:
```bash
sudo docker-compose down
```


## Making Requests
Using Postman or cURL, send a GET request to the universities endpoint on localhost port 5000 (http://127.0.0.1:5000/universities?country=<COUNTRY>) with your desired country parameter.

You will get back a JSON response in around 200-300ms. Submit the request again, and you'll see the lightning fast cached response. In most cases, sub 10ms!

Since we are caching by query string, if you change the country parameter, submit a request, then switch back to your original parameter within the 30 second expiration time, it'll still be in the cache, giving you that super fast response.
