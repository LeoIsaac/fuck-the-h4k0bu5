from flask import Flask, request, jsonify

from suggest import Suggest

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"

@app.route("/suggest-stop")
def index_suggest():
    origin = request.args.get('origin', '')
    destination = request.args.get('destination', '')
    json = Suggest().getSuggest(origin, destination)
    return jsonify(json)

@app.route("/decision-stop")
def index_decision():
    origin = request.args.get('origin', '')
    destination = request.args.get('destination', '')
    json = Suggest().getDecision(origin, destination)
    return jsonify(json)

if __name__ == "__main__":
    app.run()
