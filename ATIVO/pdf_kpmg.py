import tabula
import pandas as pd

caminho_pdf = "Banco-Master-balanco-consolidado-dez.2024.pdf"

tabelas = tabula.read_pdf(caminho_pdf,
    pages='21-26',
    stream=True,
    guess=True)

ativo = tabelas[0].copy()
ativo = ativo.dropna(how='all', axis=0).dropna(how='all', axis=1)
ativo.drop("Nota", axis=1, inplace=True)
ativo.columns=['Descricao', '2024', '2023']
ativo.drop(52, inplace=True)

passivo = tabelas[1].copy()
passivo = passivo.dropna(how='all', axis=0).dropna(how='all', axis=1)
passivo.drop("Nota", axis=1, inplace=True)
passivo.columns=['Descricao', '2024', '2023']

dre = tabelas[2].copy()
dre = dre.dropna(how='all', axis=0).dropna(how='all', axis=1)
dre.columns = dre.iloc[0]
dre.drop(dre.index[0], inplace=True)
dre.drop("Nota", axis=1, inplace=True)
dre.columns=['Descricao', '2_semestre_2024', '2024', '2023']


def limpar_coluna(df, colunas):
    for col in colunas:
        if col in df.columns:
            df[col] = df[col].replace('-', '0')
            df[col] = df[col].astype(str)
            df[col] = df[col].str.replace('.', '', regex=False)
            df[col] = df[col].str.replace(r'^\((.*)\)$', r'-\1', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


dre    = limpar_coluna(dre,    ['2024', '2023', '2_semestre_2024'])
ativo  = limpar_coluna(ativo,  ['2024', '2023'])
passivo= limpar_coluna(passivo,['2024', '2023'])

dra_tabela = tabula.read_pdf(caminho_pdf,
    pages='24',
    stream=True,
    guess=False)

dra = dra_tabela[0].copy()
dra.columns = dra.iloc[3]

dra.drop(dra.index[0], inplace=True)
dra.drop(dra.index[1], inplace=True)
dra.drop(dra.index[2], inplace=True)
dra.drop(dra.index[3], inplace=True)
dra.drop(dra.index[0], inplace=True)
dra.drop(dra.index[1], inplace=True)
dra.drop(dra.index[0], inplace=True)

dra = dra.dropna(how='all', axis=0).dropna(how='all', axis=1)
dra = dra.dropna(subset=['2024'])
dra = limpar_coluna(dra, ['2024', '2023'])
dra.columns=['Descricao', '2024', '2023']

print(dra)
print(dre)
print(ativo)
print(passivo)