from flask import Flask
from textblob import TextBlob
from flask_basicauth import BasicAuth
import os


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

Basic_Auth = BasicAuth(app)

@app.route('/')
def home():
    return 'Análise de Sentimentos'


@app.route('/sentiment/<sentence>')
@Basic_Auth.required
def sentiment(sentence):
    tb = TextBlob(sentence)
    polarity = tb.sentiment.polarity
    return 'Polaridade: {}'.format(polarity)


app.run(debug=True, host='0.0.0.0')