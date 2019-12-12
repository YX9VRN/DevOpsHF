from flask import Flask
import requests

app = Flask(__name__)

@app.route("/<digits>", methods = ["GET"])
def specified_number(digits):
    url = "http://numbersapi.com/"+digits
    response = requests.get(url)
    return response.text
if __name__ == "__main__":
    app.run()