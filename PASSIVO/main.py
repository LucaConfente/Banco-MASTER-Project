import pandas as pd

df = pd.read_csv('dado-Instituições-Individuais-passivo.csv', sep=';')

df_filtrado = df[
    (df['Instituição'] == 'BANCO MASTER S/A') |
    (df['Conglomerado Prudencial'] == "BANCO MASTER - PRUDENCIAL")
]

print(df_filtrado)

df_filtrado['Data'] = pd.to_datetime(df_filtrado['Data'], format='%d/%m/%Y')

print(df_filtrado.dtypes)

df_filtrado.drop(columns=['Column1'], inplace=True)

print(df_filtrado.dtypes)

print(df_filtrado.isna().sum())

df_filtrado.to_csv('dados-tratados-banco-master.csv', sep=';', index=False, encoding='utf-8-sig')
print("✅ Arquivo salvo: dados-tratados-banco-master-passivo.csv")