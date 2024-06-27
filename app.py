from flask import Flask, render_template
from functions.utils import get_global_crypto_data, get_crypto_market_data

app = Flask(__name__)

@app.route('/')
def home():
    list = get_crypto_market_data()
    return render_template('index.html', list=list)

if __name__ == '__main__':
    app.run(debug=True)