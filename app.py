from flask import Flask, render_template
from functions.utils import get_crypto_market_data, get_crypto_data

app = Flask(__name__)

@app.route('/')
def home():
    list = get_crypto_market_data()
    return render_template('index.html', list=list)

@app.route('/<crypto>')
def about(crypto):
    data = get_crypto_data(crypto)
    return render_template('crypto.html', crypto=crypto, data=data)

if __name__ == '__main__':
    app.run(debug=True)