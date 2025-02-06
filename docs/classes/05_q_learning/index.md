# Algoritmo Q-Learning

## Definições e conceitos chave    

Nesta aula vamos utilizar os slides abaixo:

<embed src="q_learning.pdf" type="application/pdf" width="800" height="400">

## Implementação

Depois de uma breve conversa sobre os principais conceitos, vamos implementar o primeiro agente utilizando aprendizado por reforço. Por favor, siga as instruções abaixo:

1. Utilize como base o código que você implementou na [aula anterior](../04_toolings_envs/index.md).
1. Considere apenas o ambiente do *Taxi Driver*.
1. Na linha 8 `agent.update(action, state, reward)`, implemente a equação de Bellman para atualizar os valoes da Q-table. 
1. Implemente a linha 6 `action = agent.select_action(state)` para selecionar a ação com base na política epsilon-greedy.
1. Detalhe importante: a variável `state` da linha 6 é o estado atual, e a variável `state` da linha 7 é  de fato o `next_state`. 
1. Implemente alguma forma para persistir a Q-table. Pode ser um arquivo CSV, JSON, ou qualquer outro formato que você preferir.
1. Para cada episódio use uma variável que armazena a recompensa acumulada da trajetória executada naquele episódio. Basicamente, você vai ter que inicializar esta variável com zero no início de cada episódio e atualizá-la a cada ação tomada com o reward recebido. 
1. Ao final de cada ação executada pelo agente não esqueça de atualizar o estado atual com o `next_state`. 
1. Ao final de cada episódio, registre a recompensa acumulada em um arquivo de log onde você irá informar o número do episódio e a recompensa acumulada.

O script implementado acima deve gerar:

* um arquivo de log com o número do episódio e a recompensa acumulada, e;
* um arquivo com a Q-table.

Crie mais dois artefatos de software que: 

* imprime a curva de aprendizado do agente. A curva de aprendizado do agente precisa ser um gráfico que mostra o número do episódio no eixo x e a recompensa acumulada no eixo y.
* faz uso da Q-table para executar o agente no ambiente do *Taxi Driver*. O agente deve ser capaz de executar o ambiente sem treinamento.

## Entrega

Coloque todos os arquivos em um mesmo projeto e submeta-os para o [https://classroom.github.com/a/TMjBraJx](https://classroom.github.com/a/TMjBraJx). Esta atividade é individual ou em dupla e o **prazo é 10/02/2024 15:30.** Eventualmente, você não conseguirá terminar a atividade no tempo estipulado. Neste caso, submeta o que você conseguiu fazer. No arquivo README.md você deve informar o que está faltando. 