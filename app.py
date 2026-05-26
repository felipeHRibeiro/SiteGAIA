from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('site.html')

@app.route('/api/bancos')
def bancos():

    caminho = os.path.join('generated', 'bancos.json')

    with open(caminho, encoding='utf-8') as f:
        dados = json.load(f)

    return jsonify(dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)