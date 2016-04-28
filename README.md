# Dados Abertos - Câmara dos Deputados
---

Um projeto para recuperar e armazenar de forma estruturada os dados abertos da cãmara dos deputados do Brasil.

### Dependências
* psycopg2
* sqlalchemy

### Instruções

1. Primeiro crie o banco de dados de acordo com as informações no arquivo `models.py`
1. execute o script `create.py` para criar as tabelas do schema
1. execute o script `import_from_xml.py` para importar os dados dos arquivos no servidor da câmara
