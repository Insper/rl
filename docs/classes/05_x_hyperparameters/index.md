# Hiperparâmetros em Q-Learning

Ainda considerando o exemplo a implementação do `TaxiDriver`, responda as perguntas abaixo.

Para responder as questões abaixo utilize as implementações do `TaxiDriverGym.py` e `QLearning.py` que você implementou na atividade anterior.

## Manipulando $\alpha$ e $\gamma$

* Se $\alpha$ for um valor muito próximo de zero? Explique o comportamento encontrado.

* Se $\gamma$ for zero? Explique o comportamento encontrado. 

Para fundamentar a sua resposta, use os plots gerados na pasta `results` depois do treinamento. 

## Considerando uma escolha de ação sempre aletatória

O que acontece se a escolha das ações em cada estado for sempre aleatória? Ou seja, se a função `select_action` ao invés de ser definida como abaixo:

````python
def select_action(self, state):
    rv = random.uniform(0, 1)
    if rv < self.epsilon:
        return self.env.action_space.sample() # Explore action space
    return np.argmax(self.q_table[state]) # Exploit learned values
````

É definida assim:

````python
def select_action(self, state):
    return self.env.action_space.sample() # Explore action space
````

Qual o comportamento do agente? **Novamente**: use os plots gerados na pasta `results` depois do treinamento para fundamentar a sua resposta. 

## Considerando um agente que nunca explora novas ações

O que acontece se a escolha das ações em cada estado for sempre buscando a melhor ação? Ou seja:

````python
def select_action(self, state):
    return np.argmax(self.q_table[state]) # Exploit learned values
````  

## Sumarizando os resultados através de imagens

Como podemos sumarizar os diferentes resultados através de imagens?

Neste momento, você já deve ter percebido que uma ferramenta muito útil para visualizar e sumarizar o aprendizado do agente são gráficos que mostram a evolução de alguma métrica ao longo dos diversos episódios.

* Quais foram as métricas utilizadas no caso do `TaxiDriver`?

* Quais foram os hiperparâmetros utilizados? 

* O aprendizado dos agentes implementados para este caso **convergem** rapidamente? 

* O **desempenho** do agente se mantem ao longo dos episódios? 

## Atividade

Este exercício é composto por duas partes. 

### Parte 1

Faça uso de uma única imagem para sumarizar o aprendizado do agente. Você deve escolher a melhor métrica para o eixo $y$ do gráfico. O eixo $x$ deve ser a quantidade de episódios utilizado no treinamento. Você também deve definir qual é o melhor *zoom* (foco) no gráfico. Crie um documento que tem esta única imagem e a legenda dela.

Na legenda é necessário ter o título da imagem e um texto explicativo. O texto explicativo pode ser longo e deve ter as informações sobre os hiperparâmetros utilizados. 

O gráfico deve possuir 3 linhas distintas. Cada uma destas linhas deve apresentar uma variação possível considerando os hiperparâmetros $\alpha$, $\gamma$ e $\epsilon$. Deverá ficar a critério do estudante quais valores utilizar. 

Um exemplo de imagem que sumariza dados ou apresenta resultados de experimentos é apresentada abaixo: 

<img src="figures/graph_anatomy.png" alt="Elementos de um gráfico" style="height: 400px;"/>

Todas as informações relevantes para entender o resultado do treinamento precisam estar auto-contidas na imagem e na legenda da imagem. 

### Parte 2

O objetivo desta parte é entender a evolução da *Q-table* ao longo dos episódios. Para isso, você deve escolher um estados específicos e mostrar a evolução da *Q-table* para estes estados. Mais especificamente, você deve escolher um estado que corresponde a um episódio inicial, um estado que corresponde a um episódio intermediário e um estado que corresponde a um episódio final.

Para cada uma destas versões da *Q-table* você deve gerar um heatmap. Crie uma única imagem que contenha os três heatmaps. Na legenda desta imagem descreva o que cada um dos heatmaps representa, por exemplo, descrevendo o que são as colunas e linhas do heatmap.

### Entrega

Um documento com estas duas imagens e legendas deve ser entregue via Blackboard até o dia **29/02/2023**. A atividade já foi criada no Blackboard e o nome dela é *Exercício 4*. Esta atividade é individual.

### Rubrica de avaliação

| Conceito | Descrição |
|:---------|:----------|
| A+       | Entregou duas imagens com qualidade alta e legenda. Os textos das legendas possuem todas as informações necessárias para entender os resultados alcançados pelo experimento. Uma das imagens é uma imagem que consegue mostrar a diferença entre os hiperparâmetros escolhidos e a outra imagem consegue mostrar bem a evolução da Q-table. |
| B        | Entregou duas imagens com qualidade média e legenda. Os textos das legendas possuem todas as informações necessárias para entender os resultados alcançados pelo experimento. As imagens não conseguem mostrar bem a diferença entre os hiperparâmetros escolhidos e a evolução da Q-table. |
| D        | Entregou apenas uma imagem ou entregou imagens incompletas ou sem legenda. |

<!--
## Um exemplo de gráfico muito bem feito :new: 

Segue abaixo um exemplo de gráfico muito bem formatado e completo. Este gráfico foi feito pela Letícia. 

<center>
<img src="figures/leticia.png" alt="Exemplo de gráfico" style="height: 500px;"/>
</center>
-->