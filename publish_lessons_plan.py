import tabulate
import pandas as pd

t1 = pd.read_excel('lessons_plan.xlsx')
#t1['Data'] = t1['Data'].apply(lambda x: x.strftime('%d/%m'))

with open('docs/_snippets/plan.md', 'w') as f:
    tabela_str = tabulate.tabulate(t1[['Date', 'Content']], headers=['Date', 'Content'], tablefmt='pipe', showindex=False)
    f.write(tabela_str)
