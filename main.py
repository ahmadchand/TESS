import aiml
from flask import Flask,render_template,request
from tokens import create_tags
from Semantic_Networks import Semantics


# Create the kernel and learn AIML files
kernel = aiml.Kernel()
files = ["tess.aiml", "convo.aiml"]
for x in files:
    kernel.learn(x)

#Flask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    Semantics(userText)
    return kernel.respond(userText)



if __name__ == "__main__":
    app.run()







