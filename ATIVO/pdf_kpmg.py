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

# Replace '-' with 0 in the '2023', '2024' and '2_semestre_2024' columns.
# The replace method works directly on Series, and is more efficient than iterating.
dre['2023'] = dre['2023'].replace('-', '0')
dre['2024'] = dre['2024'].replace('-', '0')
dre['2_semestre_2024'] = dre['2_semestre_2024'].replace('-', '0')

for col in ['2024', '2023', '2_semestre_2024']:
    if col in dre.columns:
        dre[col] = dre[col].astype(str)
        dre[col] = dre[col].str.replace('.', '', regex=False)
        dre[col] = dre[col].str.replace(r'^\((.*)\)$', r'-\1', regex=True)
        dre[col] = pd.to_numeric(dre[col], errors='coerce')

for col in ['2024', '2023', '2_semestre_2024']:
    if col in dre.columns:
        # Convert to string to ensure string methods can be applied
        dre[col] = dre[col].astype(str)
        # Remove thousands separators ('.')
        dre[col] = dre[col].str.replace('.', '', regex=False)
        # Handle negative numbers wrapped in parentheses, e.g., "(123)" becomes "-123"
        dre[col] = dre[col].str.replace(r'^\((.*)\)$', r'-\1', regex=True)
        # Convert to numeric, coercing errors (e.g., NaN values or other non-numeric strings) to NaN
        dre[col] = pd.to_numeric(dre[col], errors='coerce')

ativo['2023'] = ativo['2023'].replace('-', '0')
ativo['2024'] = ativo['2024'].replace('-', '0')

for col in ['2024', '2023']:
    if col in ativo.columns:
        # Convert to string to ensure string methods can be applied
        ativo[col] = ativo[col].astype(str)
        # Remove thousands separators ('.')
        ativo[col] = ativo[col].str.replace('.', '', regex=False)
        # Handle negative numbers wrapped in parentheses, e.g., "(123)" becomes "-123"
        ativo[col] = ativo[col].str.replace(r'^\((.*)\)$', r'-\1', regex=True)
        # Convert to numeric, coercing errors (e.g., NaN values or other non-numeric strings) to NaN
        ativo[col] = pd.to_numeric(ativo[col], errors='coerce')

passivo['2023'] = passivo['2023'].replace('-', '0')
passivo['2024'] = passivo['2024'].replace('-', '0')

for col in ['2024', '2023']:
    if col in passivo.columns:
        # Convert to string to ensure string methods can be applied
        passivo[col] = passivo[col].astype(str)
        # Remove thousands separators ('.')
        passivo[col] = passivo[col].str.replace('.', '', regex=False)
        # Handle negative numbers wrapped in parentheses, e.g., "(123)" becomes "-123"
        passivo[col] = passivo[col].str.replace(r'^\((.*)\)$', r'-\1', regex=True)
        # Convert to numeric, coercing errors (e.g., NaN values or other non-numeric strings) to NaN
        passivo[col] = pd.to_numeric(passivo[col], errors='coerce')

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

for col in ['2024', '2023']:
    if col in dra.columns:
        # Convert to string to ensure string methods can be applied
        dra[col] = dra[col].astype(str)
        # Remove thousands separators ('.')
        dra[col] = dra[col].str.replace('.', '', regex=False)
        # Handle negative numbers wrapped in parentheses, e.g., "(123)" becomes "-123"
        dra[col] = dra[col].str.replace(r'^\((.*)\)$', r'-\1', regex=True)
        # Convert to numeric, coercing errors (e.g., NaN values or other non-numeric strings) to NaN
        dra[col] = pd.to_numeric(dra[col], errors='coerce')

dra.columns=['Descricao', '2024', '2023']

print(dra)
print(dre)
print(ativo)
print(passivo)

