import tabulate
import pandas as pd

t1 = pd.read_excel('lessons_plan.xlsx')
t1['Date'] = t1['Date'].apply(lambda x: x.strftime('%m/%d'))

with open('docs/_snippets/plan.md', 'w') as f:
    tabela_str = tabulate.tabulate(t1[['Data', 'Conteúdo','Programação/Atividade']], headers=['Data', 'Conteúdo','Programação/Atividade'], tablefmt='pipe', showindex=False)
    f.write(tabela_str)
