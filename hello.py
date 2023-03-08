from flask import Flask

app = Flask(__name__)


"""@app.route("/japan/<city>") #可変URLルーティング
def japan(city):
    return f"<p>Hello,{city} japan!!</p>" """

@app.route("/") 
def hello():
    return "Hello World!!"
