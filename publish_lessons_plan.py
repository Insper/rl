import pandas as pd
from pretty_html_table import build_table

def redefine_strong(tabela):
    tabela = tabela.replace('&lt;strong&gt;','<strong>')
    tabela = tabela.replace('&lt;/strong&gt;','</strong>')
    return tabela

df = pd.read_excel('lessons_plan_EN.xlsx')

parte1 = build_table(df.iloc[0:3][['Date', 'Content','Activities']], 
    color='blue_dark')
parte1 = redefine_strong(parte1)
with open('docs/_snippets/plano_aula_1.md', 'w') as f:
    f.write(parte1)

parte2 = build_table(df.iloc[3:9][['Date', 'Content','Activities']], 
    color='yellow_dark')
parte2 = redefine_strong(parte2)
with open('docs/_snippets/plano_aula_2.md', 'w') as f:
    f.write(parte2)

parte3 = build_table(df.iloc[9:16][['Date', 'Content','Activities']], 
    color='green_dark')
parte3 = redefine_strong(parte3)
with open('docs/_snippets/plano_aula_3.md', 'w') as f:
    f.write(parte3)


parte4 = build_table(df.iloc[16:19][['Date', 'Content','Activities']], 
    color='red_dark')
parte4 = redefine_strong(parte4)
with open('docs/_snippets/plano_aula_4.md', 'w') as f:
    f.write(parte4)


parte5 = build_table(df.iloc[19:][['Date', 'Content','Activities']], 
    color='yellow_dark')
parte5 = redefine_strong(parte5)
with open('docs/_snippets/plano_aula_5.md', 'w') as f:
    f.write(parte5)
