from flask import Flask, request, jsonify
from flask_caching import Cache
import requests

app = Flask(__name__)
app.config.from_object('config.Config')
cache = Cache(app)

@app.route("/universities", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    query_param = request.args.get('country')
    res = requests.get(f'{API_URL}{query_param}')
    return res.json()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")