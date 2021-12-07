from flask import Flask, render_template, request
from speechTest import speechToText
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='template')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/api/audio", methods=['POST'])
@cross_origin()
def Index():
    if request.method == 'POST':
        return speechToText(request.files['audio'], request.form['languageCode'])


if __name__ == '__main__':
    app.run(debug=True)
