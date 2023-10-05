import basedosdados as bd
import pandas as pd

# api gratuita que consome dados de usuarios de bandalarga fixa no brasil contendo a média por mês
df = bd.read_table(dataset_id='br_anatel_banda_larga_fixa',
                   table_id='densidade_brasil',
                   billing_project_id="projetobandalargafixa")

# Transforma o DataFrame em um arquivo JSON
df.to_json('dados.json', orient='records', lines=True)
print("Dados exportados para dados.json")