from flask import Flask
import requests

app = Flask(__name__)

@app.route("/<digits>", methods = ["GET"])
def specified_number(digits):
    url = "http://numbersapi.com/"+digits
    response = requests.get(url)
    return response.text
@app.route("/xd", methods = ["GET"])
def random_number():
    url = "http://numbersapi.com/random"
    response = requests.get(url)
    return response.txt

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
