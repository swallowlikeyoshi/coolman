from flask import Flask, request, render_template
from route import audio

app = Flask(__name__)
app.register_blueprint(audio.Audio)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)