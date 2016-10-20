from flask import Flask
from twilio import twiml

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#tells Twilio how to respond to text messages
@app.route("/sms", methods=["GET", "POST"])
def sms():

    """Responds to incoming text messages"""


    response = twiml.Response()
    response.message('Hello from SF Python!')
    return str(response)

if __name__ == "__main__":
    app.run()