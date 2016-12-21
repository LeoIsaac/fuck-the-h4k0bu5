from flask import Flask, request, jsonify

from suggest import Suggest

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"

@app.route("/suggest-stop")
def index_suggest():
    ori = request.args.get('origin', '')
    des = request.args.get('destination', '')
    json = Suggest(ori, des).getSuggest()
    return jsonify(json)

@app.route("/decision-stop")
def index_decision():
    ori = request.args.get('origin', '')
    des = request.args.get('destination', '')
    json = Suggest(ori, des).getDecision()
    return jsonify(json)

if __name__ == "__main__":
    app.run()
