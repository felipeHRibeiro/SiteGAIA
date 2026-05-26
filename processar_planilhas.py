import pandas as pd
import os
import json

PASTA_PLANILHAS = 'planilhas'
PASTA_OUTPUT = 'generated'

os.makedirs(PASTA_OUTPUT, exist_ok=True)

resultado_final = []

for arquivo in os.listdir(PASTA_PLANILHAS):

    if arquivo.endswith('.xlsx'):

        caminho = os.path.join(PASTA_PLANILHAS, arquivo)

        print(f'Processando: {arquivo}')

        try:

            df = pd.read_excel(caminho, header=None)

            df = df.fillna('')

            linhas = df.values.tolist()

            oportunidades = {}

            # percorre linhas
            for linha in linhas:

                if len(linha) < 4:
                    continue

                campo = str(linha[1]).strip()

                # pega oportunidades da coluna 3 em diante
                for col in range(3, len(linha)):

                    valor = str(linha[col]).strip()

                    if valor == '':
                        continue

                    if col not in oportunidades:
                        oportunidades[col] = {}

                    # Nome da oportunidade
                    if campo == 'Nome da Oportunidade':
                        oportunidades[col]['nome'] = valor

                    # Instituição
                    elif campo == 'Instituição':
                        oportunidades[col]['instituicao'] = valor

                    # Descrição
                    elif campo == 'Descrição da Oportunidade':
                        oportunidades[col]['descricao'] = valor

            # adiciona ao resultado final
            for op in oportunidades.values():

                op['link'] = '#'

                if 'nome' in op:
                    resultado_final.append(op)

        except Exception as e:

            print(f'Erro: {e}')

# salva json limpo
with open('generated/bancos.json', 'w', encoding='utf-8') as f:

    json.dump(
        resultado_final,
        f,
        ensure_ascii=False,
        indent=4
    )

print('JSON LIMPO GERADO')