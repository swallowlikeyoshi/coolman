from flask import Flask, request, render_template
from route import audio
from route import gpt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(audio.Audio)
app.register_blueprint(gpt.LLM)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)