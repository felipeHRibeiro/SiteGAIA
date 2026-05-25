from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Mapeamento dos grupos para os arquivos de planilha
PLANILHAS = {
    'grupo3': 'Grupo 3 - Agências de Cooperação e Fomento Bilaterais.xlsx',
    'grupo4': 'Grupo 4 - Bancos de Fomento Nacionais  Regionais - Mapeamento de Oportunidades (1).xlsx',
    'grupo5': 'Grupo 5 - Fundos Privados de impacto - Mapeamento_de_Oportunidades (1).xlsx',
    'grupo6': 'Grupo 6 - Incentivos Fiscais e Politicas Publicas de Fomento -  Mapeamento de Oportunidades - Grupo 6 (1).xlsx',
    'grupo7': 'Grupo 7 - Fundos Climáticos Internacionais - Mapeamento de Oportunidades - Daniell Positivo - Grupo 7 (1).xlsx',
    'grupo8': 'Grupo 8 - Fundações Filantrópicas e ONGs -  Mapeamento de Oportunidades - Kerolyn Mello (1).xlsx',
    'grupo9': 'Grupo 9 - Bancos comerciais nacionais - Mapeamento de Oportunidades 1 - Luiz Hoffmann (1).xlsx',
}

@app.route('/')
def home():
    return render_template('site.html')

@app.route('/planilha/<grupo>')
def baixar_planilha(grupo):
    if grupo not in PLANILHAS:
        return 'Planilha não encontrada.', 404

    nome_arquivo = PLANILHAS[grupo]
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(base_dir, 'planilhas', nome_arquivo)

    return send_file(caminho, as_attachment=True, download_name=nome_arquivo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)