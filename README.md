[README_GAIA.md](https://github.com/user-attachments/files/33719299/README_GAIA.md)
# GAIA

> Plataforma que reúne editais e linhas de financiamento, nacionais e internacionais, para empresas com projetos sustentáveis.

O GAIA é o site de um escritório de advocacia voltado a ajudar empresas com projetos sustentáveis a conseguir recursos. Ele funciona como um catálogo de oportunidades de financiamento: fundos climáticos, bancos de desenvolvimento, editais públicos, fundações e linhas de crédito verde, com informações organizadas para a empresa encontrar onde pedir recursos.

## Status

Projeto em desenvolvimento, executado apenas em ambiente local (ainda não publicado).

## Funcionalidades

- Catálogo de oportunidades de financiamento com nome, instituição e descrição
- Cartões que expandem para mostrar mais detalhes de cada oportunidade
- Filtro por setor
- API que entrega os dados em JSON
- Cadastro das oportunidades em planilhas Excel, convertidas automaticamente para o formato que o site lê

## Tecnologias

- Python 3
- Flask (servidor web e API)
- pandas e openpyxl (leitura das planilhas)
- HTML, CSS e JavaScript (interface)

## Como funciona

Os editais não ficam em um banco de dados. O fluxo é este:

```
planilhas/*.xlsx  →  processar_planilhas.py  →  generated/bancos.json  →  API Flask  →  site
 (cadastro manual)      (conversão)               (dados prontos)       (/api/bancos)   (cartões)
```

1. As oportunidades são cadastradas manualmente em planilhas `.xlsx`.
2. O script `processar_planilhas.py` lê todas as planilhas e gera o arquivo `generated/bancos.json`.
3. O `app.py` publica esse JSON em `/api/bancos`.
4. O `script.js` consome a API e desenha os cartões na página.

## Estrutura do projeto

```
GAIA/
├── app.py                    # Servidor Flask e API
├── processar_planilhas.py    # Converte as planilhas em JSON
├── planilhas/                # Planilhas .xlsx com os editais
├── generated/
│   └── bancos.json           # Dados gerados (saída do script)
├── templates/
│   └── site.html             # Página principal
└── static/
    └── script.js             # Lógica da página (cartões e filtro)
```

## Como rodar

### 1. Pré-requisitos

- Python 3.8 ou superior

### 2. Instalar as dependências

```bash
pip install flask pandas openpyxl
```

### 3. Gerar os dados a partir das planilhas

Coloque as planilhas `.xlsx` na pasta `planilhas/` e execute:

```bash
python processar_planilhas.py
```

Isso cria (ou atualiza) o arquivo `generated/bancos.json`.

### 4. Iniciar o site

```bash
python app.py
```

Abra no navegador: <http://localhost:5000>

## Como cadastrar um novo edital

Cada planilha segue um formato em que cada **coluna** (a partir da quarta) é uma oportunidade, e cada **linha** é um campo. O nome do campo fica na segunda coluna:

| Campo (segunda coluna) | O que preencher |
|------------------------|-----------------|
| `Nome da Oportunidade` | Nome do edital ou linha de financiamento |
| `Instituição` | Quem oferece o recurso |
| `Descrição da Oportunidade` | Resumo: objetivo, valores, prazos e quem pode participar |

Depois de editar as planilhas, rode `python processar_planilhas.py` de novo para atualizar o site.

## API

| Método | Rota | O que faz |
|--------|------|-----------|
| `GET` | `/` | Abre a página principal |
| `GET` | `/api/bancos` | Retorna todas as oportunidades em JSON |

Exemplo de item retornado:

```json
{
    "nome": "Fundo Clima 2026 – Linha Inovação e Carbono Neutro",
    "instituicao": "BNDES (Gestor)",
    "descricao": "Financiamento para projetos de redução de emissões de gases de efeito estufa e adaptação às mudanças climáticas.",
    "link": "#"
}
```

## Próximos passos

- Preencher o link oficial de cada oportunidade (hoje o campo `link` está como `#`)
- Incluir no cadastro os campos que a página já prevê exibir: país, moeda, valor, setor e site
- Remover oportunidades duplicadas e revisar textos do catálogo
- Publicar o site

## Aviso

As informações sobre prazos, valores e disponibilidade dos editais mudam com frequência. Confirme sempre na fonte oficial de cada instituição antes de iniciar uma candidatura.

## Autor

Felipe Henrique Ribeiro
