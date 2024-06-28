from flask import Flask, render_template, jsonify
from functions.utils import get_crypto_market_data, get_crypto_data, get_crypto_market_chart,get_global_crypto_data

app = Flask(__name__)

@app.route('/')
def home():
    list = get_crypto_market_data()
    return render_template('index.html', list=list)

@app.route('/<crypto>')
def about(crypto):
    data = get_crypto_data(crypto)
    return render_template('crypto.html', crypto=crypto, data=data)

@app.route('/api/chart_data/<crypto>', methods=['GET'])
def chart_data(crypto):
    data = get_crypto_market_chart(crypto)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "No data found"}), 404

@app.route('/global_market_cap')
def global_market_cap():
    data = get_global_crypto_data()
    if data:
        return render_template('global_market_cap.html', data=data, error=None)
    else:
        return render_template('global_market_cap.html', data=None, error="Rate limit exceeded. Please try again in a minute.")

@app.route('/api/global_market_cap_data', methods=['GET'])
def global_market_cap_data():
    data = get_global_crypto_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "No data found"}), 404


if __name__ == '__main__':
    app.run(debug=True)