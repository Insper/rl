# Aprendizado por Reforço em ambientes não-determinísticos
    
O ambiente [Frozen Lake](https://gymnasium.farama.org/environments/toy_text/frozen_lake/) é um ambiente não determinístico onde um agente deve encontrar um caminho do lugar onde ele está para outro lugar passando por buracos. Se ele chegar no objetivo sem cair no buraco então ele termina a tarefa e tem 1 ponto de reward. Se ele cair em um dos buracos então ele termina a tarefa com 0 pontos de reward. Cada ação que não leva para um estado terminal tem reward igual a 0.  

Neste ambiente o agente consegue executar 4 ações: ir para cima, ir para baixo, ir para esquerda e ir para direita. **Como o chão é de gelo, não necessariamente a ação de ir para baixo vai levar o agente para baixo**, por exemplo. Isto acontece com todas as quatro ações. Por isso que este ambiente é não determinístico.

O ambiente Frozen Lake está disponível no pacote `gymnasium` com duas configurações: 4x4 e 8x8. 

```python
import gymnasium as gym
env = gym.make('FrozenLake-v1', map_name="4x4", is_slippery=True).env
env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True).env
```

## Perguntas

* É possível treinar um agente capaz de atuar no ambiente do Frozen Lake? Ou seja, é possível treinar um agente capaz de atuar em um mundo **não-determinístico**?

* Qual é o melhor algoritmo e os melhores hiperparâmetros para treinar um agente capaz de atuar no ambiente do Frozen Lake?

Para determinar 

## Algoritmo e hiperparâmetros utilizados para o treinamento

| Atributo        |  Valor     |
|:----------------|:----------:|
| Algoritmo       |            |
| alpha           |            |
| gamma           |            |
| epsilon         |            |
| epsilon_dec     |            |
| epsilon_min     |            |
| qtd_episodios   |            |


### Rubrica de avaliação

* Deixou de entregar um dos artefatos: q-table, implementação na forma de arquivo python ou arquivo README.md atualizado com os hiperparâmetros: igual a **Insuficiente (I)** - nota 2. 

* Entregou todos os artefatos mencionados acima então a nota é calculada de acordo com o número de testes aprovados: 
    * 1 teste aprovado = 2.5, 
    * 2 testes aprovados = 5.0, 
    * 3 testes aprovados = 7.5, 
    * 4 testes aprovados = 9.0

* Foi aprovado em todos os testes e entregou o gráfico comparando a curva de aprendizagem de diversas abordagens utilizadas ao longo do treinamento então nota igual a **10 (dez)**. 

### Deadline

O deadline para a entrega desta atividade é 8 de março de 2023 às 23:30 horas. 